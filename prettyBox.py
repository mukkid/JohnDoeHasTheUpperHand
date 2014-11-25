#!/usr/bin/python

import curses
import time
import os

msg = raw_input('type it in: ')

os.system('setterm -cursor off')
myscreen = curses.initscr()
myscreen.border(0)
for n in range (len(msg)):

    myscreen.addstr(12,40-len(msg)/2+n, msg[n])
    myscreen.refresh()
    time.sleep(0.2)

for n in range(len(msg)+4):
    myscreen.addstr(13,40-(len(msg)+4)/2+n,'=')
    myscreen.addstr(11,40-(len(msg)+4)/2+n,'=')
    myscreen.refresh()
    time.sleep(0.1)
myscreen.addstr(12,40-len(msg)/2-2,'|')
myscreen.addstr(12,40-len(msg)/2+len(msg)+1,'|')
myscreen.getch()
os.system('setterm -cursor on')
curses.endwin()
