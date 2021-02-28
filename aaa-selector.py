#!/usr/bin/python3

# Antenna selector routine
# Serial port: toggle DTR +  RTS

from serial import Serial
from sys import exit
from time import sleep
import curses

serial_dev = "/dev/ttyUSB2"
    
def main(scrn, port):
    # Main loop
    scrn.clear()
    while True:
        # Status output
        scrn.addstr(0,0,"Antenna selector")
        scrn.addstr(1,0,"A: Toggle loop A")
        scrn.addstr(2,0,"B: Toggle loop B")
        scrn.addstr(3,0,"Q,X: exit")
        scrn.addstr(4,0,"")
        scrn.addstr(5,0,"Input:  ")
        if port.dtr:
            scrn.addstr("A ON", curses.A_STANDOUT)
            scrn.addstr(" ")
        else:
            scrn.addstr("A OFF")
        scrn.addstr("  ")
        if port.rts:
            scrn.addstr("B ON", curses.A_STANDOUT)
            scrn.addstr(" ")
        else:
            scrn.addstr("B OFF")
        scrn.refresh()
        # Get selection
        inp = scrn.getkey().upper()
        if inp in ['Q','X']:
            break
        if inp == 'A':
            port.setDTR(not(port.dtr))
        if inp == 'B':
            status = port.rts
            port.setRTS(not(port.rts))

port = Serial(serial_dev)
port.setDTR(True) #init to ON avoids short glitch at open
port.setRTS(True)
curses.wrapper(main, port)
port.close()
exit(0)



