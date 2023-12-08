# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:45:05 2023

@author: BHuang
"""

import pyautogui
import time
import random
from datetime import datetime

# Set the interval (in seconds) between mouse movements
interval = 60  # Adjust this as needed

ddl=datetime(2023,6,27,13,20)
now=datetime.now()


# Continuously move the mouse to prevent the computer from sleeping
while now<ddl:
    hor=1*random.uniform(0, 1)
    ver=1*random.uniform(0, 1)
    # print(pos)
    try:
        # Move the mouse slightly to trigger activity
        pyautogui.FAILSAFE=False
        pyautogui.moveRel(hor, ver)
        pyautogui.moveRel(-hor, -ver)
        time.sleep(interval)
        now=datetime.now()
    except KeyboardInterrupt:
        break

print(datetime.now())
