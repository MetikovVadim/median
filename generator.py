#!/usr/bin/python3

import random
import datetime
from time import sleep

today = datetime.date.today()

while True:
    print(str(today) + '\t' + str(random.randint(-2**63-1,2**63-1)))
    sleep(0.01)
