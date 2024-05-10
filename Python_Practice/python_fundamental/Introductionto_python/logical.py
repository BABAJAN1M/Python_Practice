has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')


if has_good_credit and has_criminal_record != True:
    print('Eligible for loan')

name = 'Bfgh'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name must be a maximum of 50 characters')
else:
    print('Name looks good')

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")