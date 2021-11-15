import multiprocessing
def insert_record(record,records):
    records.append(record)
    print("new records inserted...")

def print_records(records):
    for rec in records:
        print(f"Name : {rec[0]},score:{rec[1]}")
        
#business data: server process is best 
#calculations: then array value shared memory is better


#parent process:
if __name__=='__main__':
    with multiprocessing.Manager() as manager: #server process having shared memory
        records=manager.list([('Murthy',10),('Sri',9),('Chaitu',10)])
        new_record=('Mallika',8)

        p1=multiprocessing.Process(target=insert_record, args=(new_record,records))
        p2=multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join() #synchronization until insertion is done , print cant be given
        p2.start()
        p2.join()
        print("db operation done")

 #4 processes are running here : 1 manager , 1 main , 2 child process

#                 child 1
#.   main manager child 2
#.                child 3
