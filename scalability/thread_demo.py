#multi threading and multi processing , multi processing is better .. but this demonstrates multi threading

import threading ,time

threadLock=threading.Lock() #semaphore/mutex
def longRunningTask():#like taking backup or sending batch emails 
    x=1
    print("Doingomplex work in the background")
    while(True):
        print("in Child Thread:",x)
        threadLock.acquire() #semaphore programming
        x+=1
        time.sleep(1)
        threadLock.release()
        if(x==5):
            break


#mainprocess /main thread:
if __name__=='__main__':
    #longRunningTask() --bad practice if function is blocking main thread for a long time, instead do instantiate the thread class like below
    t1=threading.Thread(target=longRunningTask)
    t1.start()
    print("I am doing something else.....")
    t1.join()  # this joins the main thread after finishes its task. since then main thread will be locked
    print("All work done")
    #sys.exit() here is meaningless
