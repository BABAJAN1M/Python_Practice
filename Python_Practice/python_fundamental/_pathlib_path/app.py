from pathlib import Path  
path = Path('ecommerce')


print(path.exists())  


path = Path('email')


path.mkdir()


path.rmdir()


path = Path()

for file in path.glob('*.py'):
    print(file)  