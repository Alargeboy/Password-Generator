import random
letters = ['a','b','c','d','e','f','g','h','j','k','p']
def func():
    num = random.randint(1,2)
    if(num == 1):
        num = str(random.randint(1,999))
        return num
    else:
         num = str(random.choice(letters))
         return num

num1 = func()
num2 = func()
num3 = func()
num4 = func()
num5 = func()
num6 = func()
num7 = func()
num8 = func()
num9 = func()
num10 = func()



print(f"Şifreniz = {num1+num2+num3+num4+num5+num6+num7+num8+num9+num10}")



    
    
















