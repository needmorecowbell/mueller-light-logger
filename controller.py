import serial
import datetime
import sys
import glob
import time
import progressbar

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def lightControl():
    print("***********************************")
    print("Light Controller")
    print("Developed by: Adam Musciano")
    print("Property of: Iglesias-Prieto Laboratories")
    print("***********************************\n")
    print("Available Ports: ")

    print(serial_ports())
    print("\n\n")
    intensityPercentage= 0
    timeDelay = 0 #in minutes

    #Get inputs
    port = input("[>] Enter port address (ex: COM11): ")
    baudrate=int(input("[>] Enter buadrate(ex: 9600): "))


    logFile= open("logging_template.csv","r")
    logFile.readline() #skip first line

    print("[+] Connecting to Serial Port...")
    s=None
    try:
        s= serial.Serial(port,baudrate,timeout=5)
        if(s.is_open):
            #We successsfully connected to the serial port...
            print("[+] Connected!\n")
            print("[+] Controlling system on: "+str(port)+":"+str(baudrate))

            chunk = logFile.readline()
            while(s.is_open and chunk ): #while the serial port is open for communication and the user hasn't quit...

                intensityPercentage = int(chunk.split(';')[0])
                timeDelay = int(chunk.split(';')[1])



                chunk = logFile.readline()
                print("[+] Intensity Level (%"+ str(intensityPercentage)+") being sent to arduino...")
                s.write(str(intensityPercentage).encode()) # Write level to arduino

                print("[+] Intensity Level Sent.")
                print("[+] Delaying for "+str(timeDelay)+" minutes..\n")

                pbar = progressbar.ProgressBar(widgets=[progressbar.ETA(), progressbar.Bar(), progressbar.Percentage()], maxval=timeDelay*60).start()
                for i in range(timeDelay*60):
                    time.sleep(1)
                    pbar.update(i+1)

                pbar.finish()

                print("\n")




            print("[+] Closing Connections...")
            logFile.close()
            s.close()
            print("[+] Closed and Ready to Exit")

    except serial.serialutil.SerialException :
        print("[-] Connection Error, is deviced properly addressed and plugged in?")

if __name__ == '__main__':
    lightControl()
