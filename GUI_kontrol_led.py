import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
GPIO.setup(14, GPIO.OUT)
from Tkinter import *

def on(): # Fungsi saat tombol "on" ditekan
	GPIO.output(14, True) # led menyala
def off(): # Fungsi saat tombol "off" ditekan
	GPIO.output(14, False) # led mati

GUI_led = Tk() # membuat aplikasi GUI
GUI_led.wm_title("KONTROL LED") #Membuat Judul GUI Di Bagian Kiri Atas

var = IntVar()

tombol_on = Radiobutton(GUI_led, text="LED ON", variable = var, value = 1, \
                        command=on)
tombol_on.pack( anchor = W )
tombol_off = Radiobutton(GUI_led, text="LED OFF", variable = var, value = 2,\
                         command=off)
tombol_off.pack( anchor = W )

GUI_led.mainloop() # membentuk looping program
