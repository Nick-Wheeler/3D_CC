#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import threading
import os
import glob
import time
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from picamera import PiCamera


GPIO.setmode(GPIO.BCM)

mat_lst = ['ABS', 'PLA', 'PVA', 'PP', 'PVC', 'HIPS']
default_t = [[21,30,30,25],[22,30,28,25],[23,30,24,25],
             [24,35,28,25],[25,40,28,25],[26,29,28,25]]

def power():
    if btn_var.get() == 'Power On':
        GPIO.output(Relay8, GPIO.LOW)
        #print("On")
    else:
        GPIO.output(Relay8, GPIO.HIGH)
        #print("Off")
        
def lighton():
    if btn2_var.get() == 'Light On':
        GPIO.output(Relay7, GPIO.LOW)
       # print("On")
    else:
        GPIO.output(Relay7, GPIO.HIGH)
       # print("Off")

def camera():
    camera = PiCamera()
    
    try:
        camera.start_preview()
        time.sleep(10)
    except KeyboardInterrupt:
            camera.stop_preview()
    finally:
            camera.stop_preview()
            camera.close()
#    camera.vflip = True
#    camera.hflip = True
#    camera.brightness = 60

def clicked():
    if (selected.get() == 1):
        tmp = messagebox.askokcancel("ABS", """Nozzle Temp: 240°C\nBed Temp: 80 - 100°C\nActive Cooling Fan: 25%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 80mm/s
                            \nCabinet Temp: 30°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[0][0]]))
        if tmp is True:
            z1.set(default_t[0][0])
            z2.set(default_t[0][1])
            z3.set(default_t[0][2])
            z4.set(default_t[0][3])
            return True
        else:
            return False
    elif (selected.get() == 2):
        tmp = messagebox.askokcancel("PLA", """Nozzle Temp: 220°C\nBed Temp: 60°C\nActive Cooling Fan: 100%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 80mm/s
                            \nCabinet Temp: <28°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[1][0]]))
        if tmp is True:
            z1.set(default_t[1][0])
            z2.set(default_t[1][1])
            z3.set(default_t[1][2])
            z4.set(default_t[1][3])
            return True
        else:
            return False
    elif (selected.get() == 3):
        tmp = messagebox.askokcancel("PVA", """Nozzle Temp: 220°C\nBed Temp: 60°C\nActive Cooling Fan: 100%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 80mm/s
                            \nCabinet Temp: <28°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[2][0]]))
        if tmp is True:
            z1.set(default_t[2][0])
            z2.set(default_t[2][1])
            z3.set(default_t[2][2])
            z4.set(default_t[2][3])
            return True
        else:
            return False                           
    elif (selected.get() == 4):
        tmp = messagebox.askokcancel("PP", """Nozzle Temp: 220°C\nBed Temp: 85° - 100°C\nActive Cooling Fan: 50%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 80mm/s
                            \nCabinet Temp: 45°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[3][0]]))
        if tmp is True:
            z1.set(default_t[3][0])
            z2.set(default_t[3][1])
            z3.set(default_t[3][2])
            z4.set(default_t[3][3])
            return True
        else:
            return False                    
    elif (selected.get() == 5):
        tmp = messagebox.askokcancel("PVC", """Nozzle Temp: 245°C\nBed Temp: 90° - 110°C\nActive Cooling Fan: 25%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 80mm/s
                            \nCabinet Temp: 45°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[4][0]]))
        if tmp is True:
            z1.set(default_t[4][0])
            z2.set(default_t[4][1])
            z3.set(default_t[4][2])
            z4.set(default_t[4][3])
            return True
        else:
            return False            
    elif (selected.get() == 6):
        tmp = messagebox.askokcancel("PP", """Nozzle Temp: 240°C\nBed Temp: 90° - 110°C\nActive Cooling Fan: 0 - 10%
                            \nLayer Height: 0.08 - 0.2mm\nShell Thickness: 0.4 - 0.8mm\nPrint Speed: 40 - 60mm/s
                            \nCabinet Temp: 45°C\n\nSet Default Temperatures ?\nDefault Zone Temp: """ + str(default_t[[5][0]]))
        if tmp is True:
            z1.set(default_t[5][0])
            z2.set(default_t[5][1])
            z3.set(default_t[5][2])
            z4.set(default_t[5][3])
            return True
        else:
            return False           
    else:
        messagebox.showerror("Error", "Choose Material")

def default():
    if (selected.get() == 1):
        z1.set(default_t[0][0])
        z2.set(default_t[0][1])
        z3.set(default_t[0][2])
        z4.set(default_t[0][3])
    elif (selected.get() == 2):
        z1.set(default_t[1][0])
        z2.set(default_t[1][1])
        z3.set(default_t[1][2])
        z4.set(default_t[1][3])
    elif (selected.get() == 3):
        z1.set(default_t[2][0])
        z2.set(default_t[2][1])
        z3.set(default_t[2][2])
        z4.set(default_t[2][3])
    elif (selected.get() == 4):
        z1.set(default_t[3][0])
        z2.set(default_t[3][1])
        z3.set(default_t[3][2])
        z4.set(default_t[3][3])
    elif (selected.get() == 5):
        z1.set(default_t[4][0])
        z2.set(default_t[4][1])
        z3.set(default_t[4][2])
        z4.set(default_t[4][3])
    elif (selected.get() == 6):
        z1.set(default_t[5][0])
        z2.set(default_t[5][1])
        z3.set(default_t[5][2])
        z4.set(default_t[5][3]) 
    else:
        z1.set(18)
        z2.set(18)
        z3.set(18)
        z4.set(18)
        
def dht22():
    global stor
    sensor = Adafruit_DHT.DHT22
    pin = 6
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        stor = str('Temp={0:0.1f}°C  \nHumidity={1:0.1f}%'.format(temperature, humidity))       

def tempnow():
    dht22()
    temp1 = read_temp(0)
    while temp1 == 0:
        temp1 = read_temp(0)
        time.sleep(0.01)
                
    temp2 = read_temp(1)
    while temp2 == 0:
        temp2 = read_temp(1)
        time.sleep(0.01)
            
    temp3 = read_temp(2)
    while temp3 == 0:
        temp3 = read_temp(2)
        time.sleep(0.01)
            
    temp4 = read_temp(3)
    while temp4 == 0:
        temp4 = read_temp(3)
        time.sleep(0.01)
            
    temp5 = read_temp(4)
    while temp5 == 0:
        temp5 = read_temp(4)
        time.sleep(0.01)
        
    messagebox.showinfo("Current Temperature", "Zone 1: " + str(temp1)+ "°C" +
                        "\nZone 2: " + str(temp2) + "°C" + "\nZone 3: " + str(temp3) + "°C" +
                        "\nZone 4: " + str(temp4) + "°C" + "\n\nRoom Temp: " + str(temp5) + "°C            " +
                        "\n\n Storage Box: \n" + stor)

def Display():
    window = Tk()
    
    def quit():
        GPIO.cleanup()
        exit(0)
            
#    def ac_t(zn = IntVar, co = IntVar, ro = IntVar):
#        zn = str(zn)
#        lbl = Label(window, text='Actual: ' + zn + '°C') 
#        lbl.grid(column=co, row=ro)       
    
    window.title("3D Printer Cabinet Control")
    
    global selected   
    selected = IntVar()

    #Material choice
    rad1 = Radiobutton(window,text=mat_lst[0], value=1, variable=selected)
    rad1.grid(column=0, row=0)
         
    rad2 = Radiobutton(window,text=mat_lst[1], value=2, variable=selected)
    rad2.grid(column=1, row=0)

    rad3 = Radiobutton(window,text=mat_lst[2], value=3, variable=selected)
    rad3.grid(column=2, row=0)

    rad4 = Radiobutton(window,text=mat_lst[3], value=4, variable=selected)
    rad4.grid(column=3, row=0)

    rad5 = Radiobutton(window,text=mat_lst[4], value=5, variable=selected)
    rad5.grid(column=4, row=0)

    rad6 = Radiobutton(window,text=mat_lst[5], value=6, variable=selected)
    rad6.grid(column=5, row=0)
    
    global z1
    z1 =IntVar()
    z1.set(20)
    lbl = Label(window, text="Zone 1")
    lbl.grid(column=0, row=4)
    spin = Spinbox(window, from_=0, to=100, width=5,textvariable=z1) 
    spin.grid(column=1,row=4)
   
    global z2
    z2 =IntVar()
    z2.set(20)
    lbl = Label(window, text="Zone 2")
    lbl.grid(column=3, row=4)
    spin = Spinbox(window, from_=0, to=100, width=5,textvariable=z2)
    spin.grid(column=4,row=4)
    
    global z3
    z3 =IntVar()
    z3.set(20)
    lbl = Label(window, text="Zone 3")
    lbl.grid(column=0, row=9)
    spin = Spinbox(window, from_=0, to=100, width=5,textvariable=z3) 
    spin.grid(column=1,row=9)

    global z4
    z4 =IntVar()
    z4.set(20)
    lbl = Label(window, text="Zone 4")
    lbl.grid(column=3, row=9)
    spin = Spinbox(window, from_=0, to=100, width=5,textvariable=z4)
    spin.grid(column=4,row=9)           
    
    #Menu Buttons
    global btn_var, btn2_var
    
    LABEL0, LABEL1 = 'Power Off', 'Power On'
    LABEL2, LABEL3 = 'Light Off', 'Light On'
    
    btn_var = StringVar(window, LABEL0)
    btn2_var = StringVar(window, LABEL2)    
    pbtn = Checkbutton(window, textvariable=btn_var, width=10, height = 2, bg = "green", fg = "white", variable=btn_var,
                           offvalue=LABEL0, onvalue=LABEL1, selectcolor = "red", command=power, indicator=False)
    mbtn = Button(window, text="Mat. Data", command=clicked)    
    dbtn = Button(window, text="Default", command=default)
    sbtn = Button(window, text="Temp. Now", command=tempnow)
    cbtn = Button(window, text="Camera", command=camera)
    #lbtn = Button(window, text="Light", command=lighton)
    lbtn = Checkbutton(window, textvariable=btn2_var, width=8, height = 2, variable=btn2_var,
                          offvalue=LABEL2, onvalue=LABEL3, command=lighton, indicator=False)   
    qbtn = Button(window, text="Quit", command=quit)

 
    pbtn.grid(column=0, row=12)
    mbtn.grid(column=1, row=12)
    dbtn.grid(column=2, row=12)
    sbtn.grid(column=3, row=12)
    cbtn.grid(column=4, row=12)
    lbtn.grid(column=2, row=8)    
    qbtn.grid(column=5, row=12)    

    window.mainloop()

#Relay List
Relay1 = 19
Relay2 = 26
Relay3 = 20
Relay4 = 21
Relay5 = 25
Relay6 = 27
Relay7 = 13
Relay8 = 12

pinList = [Relay1, Relay2, Relay3 , Relay4, Relay5, Relay6, Relay7 , Relay8] #Make sure to add spaces

# Turn both relays off to start with
GPIO.setwarnings(False)
for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# Enable the linux modules to read the one-wire temp devices 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
#add more  glob.glob(base_dir + '28*') "to add more sensors" [0] <--Making sure to change this number to the correct number where it is located
device_folder = [glob.glob(base_dir + '28*')[0],glob.glob(base_dir + '28*')[1],
                 glob.glob(base_dir + '28*')[2],glob.glob(base_dir + '28*')[3],glob.glob(base_dir + '28*')[4]]
#same for device file
device_file = [device_folder[0] + '/w1_slave', device_folder[1] + '/w1_slave',
               device_folder[2] + '/w1_slave',device_folder[3] + '/w1_slave', device_folder[4] + '/w1_slave']

# Reads the temp 
def read_temp_raw(device): 
    """Pass this function either 0 or 1 to get the raw data from the
        Temperature Sensor"""
    f = open(device_file[device], 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(device):
    """Pass 0 or 1 to get the temperature in celcius of either sensor"""
    lines = read_temp_raw(device)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

#Displayy Menu    
d = threading.Thread(name='Display', target=Display)
d.start()
# This tells the relays at what temp to activate and deactivate.   
while True:
    try:
        global temp1, temp2, temp3, temp4, temp5
       # temp1 = temp2 = temp3 = temp4 = temp5 = 0
        
        temp1 = read_temp(0)
        while temp1 == 0:
            temp1 = read_temp(0)
            time.sleep(0.05)
                
        temp2 = read_temp(1)
        while temp2 == 0:
            temp2 = read_temp(1)
            time.sleep(0.05)
            
        temp3 = read_temp(2)
        while temp3 == 0:
            temp3 = read_temp(2)
            time.sleep(0.05)
            
        temp4 = read_temp(3)
        while temp4 == 0:
            temp4 = read_temp(3)
            time.sleep(0.05)
            
        temp5 = read_temp(4)
        while temp5 == 0:
            temp5 = read_temp(4)
            time.sleep(0.05)
        
        if (temp1 > z1.get()+3):
            GPIO.output(Relay1, GPIO.LOW)
        if (temp1 <= z1.get()-3):
            GPIO.output(Relay1, GPIO.HIGH)           
        if (temp2 > z2.get()+3):
            GPIO.output(Relay2, GPIO.LOW)
        if (temp2 <= z2.get()-3):
            GPIO.output(Relay2, GPIO.HIGH)           
        if (temp3 > z3.get()+3):
            GPIO.output(Relay3, GPIO.LOW)
        if (temp3 <= z3.get()-3):
            GPIO.output(Relay3, GPIO.HIGH)
        if (temp4 > z4.get()+3):
            GPIO.output(Relay4, GPIO.LOW)
        if (temp4 <= z4.get()-3):
            GPIO.output(Relay4, GPIO.HIGH)
        power()
        time.sleep(1)
        
    # Stop on Ctrl+C and clean up GPIO pins
    except KeyboardInterrupt:
        GPIO.cleanup()
        
