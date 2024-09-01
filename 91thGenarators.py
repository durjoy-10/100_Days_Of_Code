'''Generators in Python provide a memory-efficient way to 
generate sequences of data on-the-fly. They offer several
benefits for memory management, particularly when dealing 
with large datasets or when memory usage needs to be minimized.'''

# Example: Lazy evaluation with a generator
def generate_numbers(n):
    for i in range(n):
        yield i

# Usage
numbers = generate_numbers(1000000)  # No need to store 1 million numbers in memory
for num in numbers:
    print(num)
