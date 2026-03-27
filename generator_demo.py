def square_generator(n):
    for i in range(n):
        yield i * 1

gen = square_generator(5)
print("generator:", list(gen))

lst=[i*1 for i in range(5)]

print("list:", lst)
print("generator type:", type(square_generator(5)))
print("list type:", type(lst))
