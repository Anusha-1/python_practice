import gc,sys
def create_cycle(lst):
    #list=[10,20,30,40]
    #list.append(list)  this is an anti pattern
    lst.append(lst)
    print(lst)

def main():
    print("Creating garbage")
    mylist=[10,20,30,40,50]
    for i in range(8):
        create_cycle(mylist)

    print('in mainbfore gc, ref count is ',gc.get_count())
    print("collecting")
    n=gc.collect()
    print('no of unreachable objects collected by gc ',n)
    print('uncollectable garbage:',gc.garbage)
    print("in main, after gc, refcount:", gc.get_count())

main()
print("observe the result")
