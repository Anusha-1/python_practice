import time


def profiler(func):
    def wrap_timer(*args,**kwargs):
        start= time.perf_counter()
        print(args[0])
        value=func(*args,**kwargs)
        end=time.perf_counter()
        runtime=end-start
        print(f'numtimes {args[0]}')
        print(f'Finished task {func.__name__} in{runtime:.4f}')
        return value
    return wrap_timer

@profiler
def task(num_times):
    for _ in range (num_times): #throwaway variable : which wont take value but it iterates
        sum([i**2 for i in range(100000)])


task(1)
task(999)