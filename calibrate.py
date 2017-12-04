import serial
import datetime
import sys
import glob
import time
import progressbar
# Calibration Procedure
# 1. Get serial port (possibly list outputs)
# 2. Loop for calibration
# 3. Inside loop, ask for percentage to measure to
# 4. convert percentage to value of 255
# 5. Send converted percentage to  arduino via serial
# 6. Ask what value in micromol quanta is being read
# 7. log values into csv (percentage,micromol quanta)
# 8. continue until user says to stop

# Logging Procedure
# 1. Retrileve Templated CSV for timing (percentage,time in minutes at that percentage)
# 2. for each percentage...
# 3. convert percentage to value of 255
# 4. send converted percentage to arduino via serial
# 5. wait for the given time in minutes
# 6. continue to the next percentage until there are no more

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

def calibrate():
    print("***********************************")
    print("Light Calibration")
    print("Developed by: Adam Musciano")
    print("Property of: Iglesias-Prieto Laboratories")
    print("***********************************\n")
    print("Available Ports: ")

    print(serial_ports())
    print("\n\n")
    intensityPercentage= 0
    intensityValue = 0

    #Get inputs
    port = input("[>] Enter port address (ex: COM11): ")
    baudrate=int(input("[>] Enter buadrate(ex: 9600): "))
    filename=str(datetime.datetime.now().strftime('%m-%d-%Y_%H-%M'))
    log= open(filename+"_calibration_log.csv","w")

    print("[+] Connecting to Serial Port...")
    s=None

    try:
        s= serial.Serial(port,baudrate,timeout=5)
        if(s.is_open):
            #We successsfully connected to the serial port...
            print("[+] Connected!\n")
            print("[+] Calibrating system using: "+str(port)+":"+str(baudrate))
            intensityInput=""
            print("[+] Enter 'q' to stop calibration")

            while(s.is_open and intensityInput is not "q" ): #while the serial port is open for communication and the user hasn't quit...
                intensityInput = input("[>] Enter Light Intensity Percentage (1-100 / 'q'): ")


                if(intensityInput is 'q'):
                    print("[+] Calibration Halted")
                else:
                    print("[+] Intensity Level ("+ intensityInput+") being sent to arduino...")
                    s.write(intensityInput.encode()) # Write level to arduino

                    print("[+] Intensity Level Sent.\n")
                    intensityValue = input("[>] Enter micromol quanta at this level: ")

                    print("[+] Logging...")
                    log.write(intensityInput+";"+intensityValue+"\n")




            print("[+] Closing Connections...")
            log.close()
            s.close()
            print("[+] Closed and Ready to Exit")
            print("[+] Log file is availabe as: "+filename+"_log.csv in current directory")

    except serial.serialutil.SerialException :
        print("[-] Connection Error, is deviced properly addressed and plugged in?")






if __name__ == '__main__':
    calibrate()
