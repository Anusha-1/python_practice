import random,os,time,psutil,gc

names= ['Anusha','Chaitanya','chait','chaitu']
majors=['Math','Science','Commerce','Arts']

def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person

if __name__=='__main__':
    t1=time.process_time()
    people =people_list(10000000)
    t2=time.process_time()
    print(f"Time taken with List {t2-t1}")
    print(psutil.Process(os.getpid()).memory_info())

    print('\n With Generators')
    del people
    gc.collect()


    t1=time.process_time()
    people =people_generator(10000000)
    t2=time.process_time()
    print(f"Time taken with Generator {t2-t1}") # it took lot less time with generators like around 0 whereas 10 seconds in above case
    print(psutil.Process(os.getpid()).memory_info())


#summary : batch update like 100 records at a time go for list. but on demand 10 records better go with generators