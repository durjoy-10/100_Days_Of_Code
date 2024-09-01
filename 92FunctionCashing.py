from functools import lru_cache
import time
 
@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(fx(10))
print("Done for 10")



import functools

@functools.lru_cache(maxsize=None)  # maxsize=None means the cache can grow indefinitely
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Now let's test the fibonacci function with some inputs
print(fibonacci(10))  # This will compute fibonacci(10) and cache intermediate results
print(fibonacci(8))   # This will use the cached result for fibonacci(8)
print(fibonacci(11))  # This will compute fibonacci(11), but reuse cached results for smaller values
