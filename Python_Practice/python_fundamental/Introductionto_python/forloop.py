
print('Iterating Over Lists and Ranges with for Loop')

for item in [1, 2, 3, 4]:
    print(item)
print("break")

for item in ['A', 'B', 'C']:
    print(item)
print("break")


for item in range(10):
    print(item)
print("break")


for item in range(5, 10):
    print(item)
print("break")

for item in range(5, 10, 2):
    print(item)
print("break")



print("Calculating Total Prices with for Loop")
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price

print(f"Total: {total}")




print('Nested Loops for Pattern Printing')

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)


numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print("*" * item)