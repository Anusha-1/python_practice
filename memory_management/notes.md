c , c++ automatic memory management is not there
stack memory and heat memory

static methods, global variables : stack
objects(classes) : heap
only objects needs garbage collection and memory collection
if space is all over, garbage collector invoked by python at run time

when gc is going on , appl is blocked
garbage collection
1. generation
2. threshold

gen0 object survives kept to gen 1 it also survives gc keeps in gen 2

gc.collect() # cleaning the memory
gc.get_count() # 18 0 0 means gen0 gen1 gen 2 objects ... based on generations it will be long running jobs
gc.get_threshold() #700 10 10 is the python default threshold 

gc.set_threshold(1000 15 15) we can also set threshold if large volume of data is there