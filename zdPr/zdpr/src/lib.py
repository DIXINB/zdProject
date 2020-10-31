import os
import numpy as np
import csv
import matplotlib.pyplot as plt
import collections
from collections import OrderedDict

class GetData():
    default_filename=os.path.join(os.path.dirname(__file__),
        '..','data','external','train_46189_1Left_0.csv')
    def __init__(self,name):
        self.nm=name
        self.x=np.arange(1500)
        self.filename=os.path.join(os.path.dirname(__file__),
            '..','data','external',self.nm)
		 
    @staticmethod
    def open_file(filename=default_filename):
        with open (filename) as fin:
            return (fin,GetData.preplt_read(fin))
    @staticmethod
    def preplt_read(seq=None):		
        i=0
        fieldnames=['TL','U','T']
        reader=csv.DictReader(seq,fieldnames=fieldnames,delimiter=';')
        num=len(list(reader))
        u=np.zeros(num,dtype=int)
        seq.seek(0)
        print("Всего строк",num)
        for row in reader:
            iitems=list(list(row.items()))
            u[i]=iitems[1][1]
            i+=1
        return (num,u)
		
    def finish_up(self,NAME):
        path=os.path.join(os.path.dirname(__file__),
            '..','data','external')
        _,(num,u)=self.open_file(self.filename)
        a=np.empty(num)
        index_split_point=np.arange(1,num//1500+1,1)
        iterable=(1500*i for i in index_split_point)	
        b=np.fromiter(iterable,np.int)
        a=np.split(u,b[:],axis=0)       
        return a


class Lump():
    lump_count=0
    def __init__(self,alump):
        self.al=alump
        Lump.lump_count +=1
    def comp_t_single_peak(self):
        med=np.median(self.al)
        std=np.std(self.al)
        bar=int(med+std)
        index_peak=np.where(self.al>bar)
        d=np.array(index_peak[0][1:])-np.array(index_peak[0][:-1])
        index_peak=np.array(index_peak[0])
        l=index_peak.size 
        num_peak=0
        single_peak=[[]]
        global t_single_peak
        t_single_peak=[]
        for i in range(l-1):    
            if d[i]<100:
                single_peak[num_peak].append(index_peak[i])
            else:       
                if len(single_peak[num_peak])>2:
                    t_single_peak.append((single_peak[num_peak][0]+single_peak[num_peak][-1])//2)
                single_peak.append([])
                num_peak+=1       
        try:
            t_single_peak.append((single_peak[-1][0]+single_peak[-1][-1])//2)
        except:
            None
        return t_single_peak
		
    def plot_lump(self,t_single_peak,ymin,ymax):
        x=np.arange(1500)
        fig, ax = plt.subplots()
        ax.set_xlim(0,1500)                                                                                                          
        ax.set_ylim(ymin,ymax)
        line, = ax.plot(x,self.al)
        line.set_linewidth(2)
        line.set_linestyle('-')
        line.set_color("red")
        line.set_data(x, self.al)
        eps=2
        mask=[np.abs(x-t_single_peak[i])<eps for i in range(len(t_single_peak))]
        for i in range(len(t_single_peak)):
            plt.scatter(x[mask[i]],self.al[mask[i]],color='blue',s=20,marker='o')
        plt.show()





    
     