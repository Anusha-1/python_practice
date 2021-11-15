import numpy as np
import time
#dot product multipication u *v: [u1 u2 u3]x[v1 v2 v3] ={...}
if __name__=='__main__':
    a=np.arange(100000)
    b=np.arange(100000)

#pure python product impl
tic=time.process_time()
dot_product=0
for i in range(len(a)):
    dot_product+= a[i] * b[i]
toc= time.process_time()

##### profiling , start the processing time, do the calculation ,stop the processing time

print("python dot product = "+ str(dot_product))
print("time_taken =" +str( (toc-tic)*1000)+"ms\n")


#numpy python outer product impl
n_tic=time.process_time()
dot_product=np.dot(a,b)
n_toc= time.process_time()
print("with numpy python dot product = "+ str(dot_product))
print("with numpy time_taken =" +str( (n_toc-n_tic)*1000)+"ms\n")

#can see how fast is numpy compared to normal python product for large volume of data
