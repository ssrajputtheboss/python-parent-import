import sys
import os
#add path to parent directory in sys.path list
sys.path.append('C:\\Users\\shash\\Desktop\\pycooks\\parent\\')
#or use below 
#sys.path.append(os.path.abspath(__file__).rstrip('dir1\\'+__file__))
from parent import parent
from dir2.dir2 import dir2
parent()
dir2()