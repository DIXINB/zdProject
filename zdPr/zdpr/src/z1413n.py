import os
import numpy as np
import csv
from zdpr import NAME
from zdpr.src.lib import GetData
from zdpr.src.lib import Lump

print(f'to egg\zdpr\data\output\{NAME}')
data1=GetData(NAME)
a=data1.finish_up(NAME)    
num_lump=0
all_peaks=[]
for ac in a:
    lump=Lump(ac)
    t_single_peak=lump.comp_t_single_peak()
    if len(t_single_peak) == 0:
                print('continue')
                num_lump+=1
                continue            
    t_single_peak1=[j+num_lump*1500 for j in t_single_peak]  
    all_peaks.append(t_single_peak1)
    num_lump += 1
all=sum(all_peaks,[])
fieldnames=['TL','U','T']
with open (os.path.join(os.path.dirname(__file__),
     '..','data','external',NAME)) as file_obj:        
        reader = csv.DictReader(file_obj,fieldnames=fieldnames,delimiter=';')
        field_names = reader.fieldnames 
        newline=[]
        row_num=0                    
        for line in reader:
            del line['T']
            if row_num+2 in all:
                u_label=1
            else:
                u_label=0                
            line.update({'Label':u_label})
            newline.append(line)
            row_num+=1   

if(not(os.path.isdir(os.path.join(os.path.dirname(__file__),
     '..','data','output')))):
    os.makedirs(os.path.join(os.path.dirname(__file__),
     '..','data','output'))
with open (os.path.join(os.path.dirname(__file__),
     '..','data','output',NAME),'w',newline='') as file_obj:         
        fieldnames=[t for i,t in enumerate(newline[0])]      
        filewriter=csv.DictWriter(file_obj,delimiter=';',fieldnames=fieldnames)
        filewriter.writeheader()    
        for row in newline:
            filewriter.writerow(row)
print('All done')