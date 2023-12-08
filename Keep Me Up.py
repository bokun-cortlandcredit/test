# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 07:37:14 2023

@author: BHuang
"""

import time, pyautogui
import multiprocessing
from datetime import datetime
import random

def KeepUI():

    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:

        if datetime.now()>=datetime(2023,12,8,12,4): # if user closes window or clicks cancel

            if p2.is_alive(): 
                p2.terminate()
            break


def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        
        hor=1*random.uniform(0, 1)
        ver=1*random.uniform(0, 1)
        
        pyautogui.FAILSAFE=False
        pyautogui.moveRel(hor, ver)
        time.sleep(1)
        pyautogui.moveRel(-hor, -ver)
        time.sleep(5)
        

if __name__ == '__main__':

    p1 = multiprocessing.Process(target = KeepUI)
    p1.start()
