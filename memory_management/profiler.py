import gc 
#pip install emory_profiler

@profile
def myfunc():
    a=[1]*(10**6)
    b=[2]*(2*10**7)
    del b 
    gc.collect()
    return a

if __name__=="__main__":
    myfunc()
    print("done")
