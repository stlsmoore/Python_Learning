# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:45:17 2020

@author: moore
"""
import re

file = open('stats.txt', 'r')
contents = file.read()
conSplit = contents.split(',')

def sorter(netinfo):
    
    infoDict = {}
    
    devPat = 'switch..'
    intPat = 'te...'
    bpsPat = '\Ad+'
    
    devMatch = re.findall(devPat, netinfo)
    intMatch = re.findall(intPat, netinfo)
    bpsMatch = re.findall(bpsPat, netinfo)
    
    #print(devMatch)
    #print(intMatch)
    #print(bpsMatch)
    
    for index in devMatch:
        infoDict[index + ' inter'] = 'value'
        
    

    #print(contents)        
    print(infoDict)
    

sorter(contents)