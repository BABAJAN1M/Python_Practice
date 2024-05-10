course = "Python's course for Beginners"
print(course)  


course = 'Python course for "Beginners"'
print(course)  

course = '''Hi Mr.Khan,
Here is our first email to you.
Thank you,
Support Team
'''
print(course) 


course = "Python course for Beginners"

print(course[1:]) 
print(course[:5])  


another = course[:]  
print(another)

name = 'Mr_Khan'
print(name[1:-1])  

first = 'Mr_'
last = 'Khan'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message) 
print(msg)     


course = 'Python for Beginners'

print(len(course))                          
print(course.upper())                       
print(course.lower())                       
print(course.find('o'))                     
print(course.replace('Beginners', 'Absolute Beginners'))  
print('Python' in course)                   