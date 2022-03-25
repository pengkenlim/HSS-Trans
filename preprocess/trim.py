#setting sys.path for importing modules
import os
import sys
if __name__ == "__main__":
        abspath= os.getcwd()
        parent_module= os.path.join(abspath.split("LSTrAP-denovo")[0], "LSTrAP-denovo")
        sys.path.insert(0, parent_module)
        

import subprocess

from setup import constants

def launch_fastp(inputpath,outputpath,threads):
    subprocess.run([constants.fastppath, "-w", str(threads), "--in1",  inputpath, "--out1", outputpath],
    stdout=subprocess.DEVNULL, 
    stderr=subprocess.STDOUT)
    

__all__=["launch_fastp"]