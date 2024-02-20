# -*- coding: utf-8 -*-
import numpy as np
import random
import os
from ase.io import read,write
from ase.io.vasp import read_vasp,write_vasp
from ase.visualize import view
from ase.geometry import wrap_positions
from scipy import sparse
from ase import neighborlist

l1=read_vasp("CONTCAR")
xyz=l1.get_positions()
print(xyz)
s=l1.get_chemical_symbols()
print(s)
for i in range (2,12,2):
  f=open("%s-info"%(i+3),mode="w")
  tmp=[]
  r=[]
  while len(r) < 2000:
    random.seed()
    c = random.sample(range(0,123),i)
    c.sort()
    #  distance
    tmpc=[]
    for m in range(i):
      for n in range(i):
        if m!=n:
          tmpc.append(float("%6.3f"%l1.get_distance(c[m],c[n],mic=True)))
    for m in range(i):
      for n in range(4):
        tmpc.append(float("%6.3f"%l1.get_distance(c[m],n+123,mic=True)))
    print(min(tmpc))
    if min(tmpc)<2:
      ok=0
    else:
      ok=1
    # 
    if c in r:
      print("again")
    elif ok==1:
      r.append(c)
      l2=l1.copy()
      s2=l2.get_chemical_symbols()
      line0=" "
      for m in range(i):
        s2[c[m]]="N"
        line0=line0+" %4d "%c[m]
      line="%4s "%(len(r))+line0+"\n"
      f.writelines(line)
      l2.set_chemical_symbols(s2)
      os.system("mkdir -p %s-%s"%(i+3,len(r)))
      write_vasp("CONTCAR-2",l2,sort=True,label='C N Ir')
      os.system("mv CONTCAR-2 %s-%s/POSCAR"%(i+3,len(r)))    
      os.system("cp INCAR POTCAR KPOINTS vdw* %s-%s/"%(i+3,len(r)))    
      os.system("cp 541.sh %s-%s/"%(i+3,len(r)))    
