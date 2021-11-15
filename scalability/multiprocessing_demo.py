#multithreading is outdated
import multiprocessing
#result=[]  #global scope

def square_list(mylist,result,square_sum):
    for idx,num in enumerate(mylist):
        result[idx]=num*num
    square_sum.value=sum(result) #aggregate sum
    print(f"in the child process,result is  {result[:]}")
    print(f"in the child process,square_sum is  {square_sum.value}")

if __name__=='__main__':
    mylist=[1,2,3,4,5]  #square this in background process #real time 1 million records or something
    result=multiprocessing.Array('i',5)
    square_sum=multiprocessing.Value('i')
    p1=multiprocessing.Process(target=square_list,args=(mylist,result ,square_sum))  #leaving , as it is means nt expecting anything in return
    p1.start()
    print("I am doing something else in main process...")
    p1.join()
    print(f"result n main process:{result}")  # we cant see the result here even it is global ,
    # because in multiprocessing child process has its own memory and runs independently. Thats why it is more secure and good abstraction
    #if we want to get the child process result into main then we have controlled process called shared memory 
    #only after adding 14,15 lines
    print(f"in the main process,result is  {result[:]}")
    print(f"in the main process,square_sum is  {square_sum.value}")





