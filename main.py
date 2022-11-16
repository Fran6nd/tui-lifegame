#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from drawille import Canvas
import math

import curses
stdscr = curses.initscr()
stdscr.nodelay(1)
curses.noecho()
curses.cbreak()
import sys
import random
#stdscr.addstr(str( curses.LINES*3))
#stdscr.refresh()
#stdscr.getch()


s = Canvas()
alive = 0
#s.set(0,0)
#s.set(curses.COLS * 2-1, (curses.LINES) * 3)
def get_alive_neighbour(_from, x, y):
    output = 0
    for _x in range(-1, 2):
        for _y in range(-1, 2):

            if not (_x == _y and _y == 0):
                if _from.get(_x + x,_y + y) == True:
                    output = output + 1
    return output

size = [curses.COLS * 2 - 2, curses.LINES * 4]
#for x in range(0, size[0],   1):
#    for y in range(0, size[1], 1):
#           s.set(x, y)

if len(sys.argv) == 2:
    if sys.argv[1] == '-r':
        for x in range(size[0]):
            for y in range(size[0]):
                if random.randint(0, 2) == 0:
                    alive += 1
                    s.set(x,y)
else:
    s.set(10, 10)
    s.set(10, 9)
    s.set(9, 10)
    s.set(10,11)
    s.set(11,10)
    s.set(13,10)


    s.set(100,10)
    s.set(101,10)
    s.set(101,11)

def builf_canvas_next(_from):
    global alive
    alive = 0

    output = Canvas()
    for x in range(size[0]):
        for y in range(size[1]):
            nb = get_alive_neighbour(_from, x,y)
            if nb == 3:
                output.set(x,y)
            elif nb== 2:
                if _from.get(x, y):
                    output.set(x,y)
            elif nb < 2 or nb  > 3:
                #output.unset(x,y)
                pass
            else:
                pass
            if output.get(x,y):
                alive += 1
                #if _from.get(x,y):
                #    output.set(x,y)
    #_from.clear()
    return output

count = 0
while True:

    stdscr.addstr(0,0,str(s.frame(0,0, size[0], size[1])))
    stdscr.addstr(0,0,'Frame: ' + str(count))
    stdscr.addstr(1,0,'Alive : '+ str(alive))
    stdscr.refresh()
    stdscr.getch()
    s = builf_canvas_next(s)
    count = count + 1
s.clear()

curses.endwin()
