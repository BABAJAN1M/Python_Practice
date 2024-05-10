try:

    age = int(input("Age: "))

    income = 2000
    

    risk = income / age

    print(age)

except ValueError:

    print("Invalid value. Please enter a valid integer for age.")

except ZeroDivisionError:

    print("Age cannot be zero. Please enter a non-zero value for age.")