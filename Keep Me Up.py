# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 07:37:14 2023

@author: BHuang
"""

import time, pyautogui
import PySimpleGUI as sg
import multiprocessing
from datetime import datetime
import random
# global ddl,p1,p2

def KeepUI():
    

    # time.sleep(3)
    # window.close()
    
    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:

        if datetime.now()>=datetime(2023,7,5,12,4): # if user closes window or clicks cancel

            if p2.is_alive(): 
                p2.terminate()
            break
        
        # elif datetime.now()>=datetime(2023,6,30,8,37):
        #     window.close()
        
        # elif datetime.now()>=ddl:
            
        #     if p2.is_alive(): 
        #         p2.terminate()
        #     break
            
            

def dontsleep():
    # print(test)
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
        
        # if datetime.now()>=datetime(2023,6,30,8,31):
        #     window.close()


if __name__ == '__main__':
    # ddl=datetime(2023,6,30,8,8)
    p1 = multiprocessing.Process(target = KeepUI)
    p1.start()
    
    # while datetime.now()<ddl:
    #     continue
    
    # p1.terminate()
