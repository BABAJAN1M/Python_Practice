
names = ['john', 'bob', 'mosh', 'sarah', 'mona']


print(names[2:4])

print(names[2:])

print(names[-2])

print(names)

names[0] = 'bharath'
print(names)


numbers = [3, 4, 100, 6, 8, 31]

max_number = numbers[0]  
for item in numbers:
    if max_number < item:
        max_number = item  


print(f"max number in list is: {max_number}")