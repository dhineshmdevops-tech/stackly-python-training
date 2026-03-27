def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

result = calculate_total(10, 20, 30, 40)

print("total:", result[0])
print("average:", result[1])