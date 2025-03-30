# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args,**kwargs)
    
        
#     return wrapper


# @log_decorator
# def add(a,b):
#     return a+b

# print(add(1,2))
# import functools
# import time

# def timer(func):
#   @functools.wraps(func)
#   def wrapper_timer(*args, **kwargs):
#     start_time = time.perf_counter()  # 1
#     value = func(*args, **kwargs)
#     end_time = time.perf_counter()  # 2
#     run_time = end_time - start_time  # 3
#     print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#     return value
#   return wrapper_timer

# @timer
# def slow_function(num_times):
#   for _ in range(num_times):
#     sum([i**2 for i in range(10000)])

# slow_function(200)


list1 = [1,2,3,4,5]

abc = iter(list1)
print(abc)

for item in abc:
    print(item)