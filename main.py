def my_enumerate(iterable):
    count = 1
    for item in iterable:
        yield count, item
        count += 1

numbers = list(range(1, 6))

for index, value in my_enumerate(numbers):
    print(f"Index: {index}, Value: {value}")
