
numbers = [5, 2, 1, 71, 1, 4]


numbers.append(20)
print(numbers)

numbers.insert(0, 78236)
print(numbers)

numbers.remove(5)
print(numbers)


numbers.pop()
print(numbers)


print(numbers.index(71))


print(numbers.count(1))


print(7 in numbers)


numbers.sort()
print(numbers)


numbers.reverse()
print(numbers)


numbers2 = numbers.copy()

numbers.append(10)


print(numbers)
print(numbers2)


numbers.clear()
print(numbers)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]


uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)