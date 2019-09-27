import  pandas as np
import numpy as np
import  sys
from toolkit.datapreprocessing.dataloading import getrawdatafromcsvfile
from toolkit.datashow.rawdatashow import plot5levelrawdata

filefullpath = "../maininsts/sn/sn0000/20190919Tgsn200120190919.csv"

rawdata = getrawdatafromcsvfile(filefullpath, 5)
plot5levelrawdata(rawdata.loc[:50,:])

print(rawdata.head(5))