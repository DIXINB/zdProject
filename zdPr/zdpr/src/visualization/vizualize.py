import numpy as np
from zdpr import NAME
from zdpr.src.lib import GetData
from zdpr.src.lib import Lump
print (NAME)

data1=GetData(NAME)
a=data1.finish_up(NAME)
almp=a[77]
ymin=np.amin(almp)
ymax=np.amax(almp)
lump1=Lump(almp)
t_single_peak=lump1.comp_t_single_peak()
lump1.plot_lump(t_single_peak,ymin,ymax)




    
     