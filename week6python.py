# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 22:27:49 2014

@author: Admin
"""

       
  # code to answer the first part of the question     

import re
filename = "C:\Users\jare\SkyDrive\WorkDocs\CUNY\Data_Analytics\Data_Programming\Week 6/week6python.txt"
hand = open(filename)
newPattern = "(\d+) (\w+)\s*\|\s*(\w\s*\d+)\s*\|\s*(\w\s*\d+)\s*\|\s*(\w\s*\d+)"
for line in hand:
    line =line.rstrip()
   # print line
    m = re.match(newPattern,line)
    if m:
        
        print "Rank:" + m.group(1)
        print "Country:"+ m.group(2)
        print "Results:"
        print m.group(3)
        print m.group(4)
        print m.group(5)
        break  #break out of the loop so that we only print one line


# The difficult part
 
    
import re
filename = "C:\Users\jare\SkyDrive\WorkDocs\CUNY\Data_Analytics\Data_Programming\Week 6/week6pythonTest.txt"
hand = open(filename)
newPattern = "(\d+) (\w+)" #"\s*\|\s*(\w\s*\d+)\s*\|\s*(\w\s*\d+)\s*\|\s*(\w\s*\d+)"

for line in hand:
    line =line.rstrip()
   # print line
    m = re.match(newPattern,line)
    if m:
        
        print "Rank:" + m.group(1)
        print "Country:"+ m.group(2)
        print "Results: "
        testPattern = "(\w\s*\d+)"
        m = re.findall(testPattern,line)
        if m:
            for x in range(len(m)):
                print m[x]
        
        break  #break out of the loop so that we only print one line