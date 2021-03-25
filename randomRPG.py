import random

print('    Colossal Cave')
print('The First Adventure')
name = input('What is your name?')
role = input('What is your role? [wizard,warrior,monk,mage]')
age = int(input('What is your age?'))
# if 20 years old and below considered young otherwise old
print('Hi',name,'Your role is',role)
if age > 20:
    print('You are old')
else:
    print('You are quite young')
playerHealth=random.randint(50,100)
monsterHealth =random.randint(50,100)
#if pH < mH print(danger) if ph = mH print(you will make) else print(sure win)

mHealths = [60,50,40,30]
# [nilai monster health]
# [monster is bleeding : health]
for x in mHealths:
    print("monster is bleeding",str(x))

if monsterHealth%age > 5 & playerHealth <65:
    print('You got chances to get gold')
elif monsterHealth%age >3 & playerHealth < 40:
    print('you got coins instead')
else:
    print('no treasure for you')