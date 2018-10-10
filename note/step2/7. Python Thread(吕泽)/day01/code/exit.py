import os 
import sys 

# os._exit(0)
try:
    sys.exit('结束了您内')
except SystemExit as e:
    print("+++",e)

print('process over')