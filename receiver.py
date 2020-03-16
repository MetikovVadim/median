#!/usr/bin/python3
import datetime
import sys
import fileinput
import time
import numpy as np
import requests
from decimal import Decimal

createDB_request ='http://localhost:8123/?query=CREATE%20TABLE%20IF%20NOT%20EXISTS%20result%0A%28%0A%20%20%20%20timestamp%20DateTime%2C%0A%20%20%20%20p_25%20Int64%2C%0A%20%20%20%20median%20Int64%2C%0A%20%20%20%20p_75%20Int64%0A%29%0AENGINE%20%3D%20MergeTree%28%29%0APARTITION%20BY%20toYYYYMMDD%28timestamp%29%0AORDER%20BY%20timestamp%0ASETTINGS%20index_granularity%3D8192'
resDB = requests.get(createDB_request)
if resDB.status_code != 200:
  print(resDB, resDB.text)



values_list = []
current_time=time.time()
for line in fileinput.input():
  elements = line.rstrip().split()
  value = int(elements[1])
  values_list.append(value)
  if time.time()-current_time>=5.0:
   current_median = Decimal(np.percentile(values_list,50))
   current_percentile25 = Decimal(np.percentile(values_list,25))
   current_percentile75 = Decimal(np.percentile(values_list,75))
   print(current_median, current_percentile25, current_percentile75)
   request ='http://localhost:8123/?query=INSERT INTO result(timestamp, p_25, median, p_75) VALUES(now(),'+str(current_percentile25)+', '+str(current_median)+', '+str(current_percentile75)+')'
   print(request)
   result = requests.get(request)
   if result.status_code != 200:
     print(result, result.text)
   current_time = time.time()
   values_list.clear
  





