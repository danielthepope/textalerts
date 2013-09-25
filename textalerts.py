#!/usr/bin/env python

import datetime
import os
from time import sleep

alertLocation = '/home/pi/apps/textalerts/alerts.txt'
alertList = open(alertLocation, 'r').read().split('\n')

for s in alertList:
    print s
