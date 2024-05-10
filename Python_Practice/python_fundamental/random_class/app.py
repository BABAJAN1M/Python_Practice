import random 
for i in range(3):
    print(random.random())  
    print('break')  
    print(random.randint(10, 50))  

members = ['a', 'b', 'c', 'd', 'e']  
leader = random.choice(members) 
print(leader)  

class Dice:
    def roll(self):
      
        first = random.randint(1, 6)  
        second = random.randint(1, 6)  
        return first, second  ss
dice = Dice()


print(dice.roll())