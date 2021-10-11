#import random

print("***First letter of every word in CAPS***")
fav_car = str(input("FAV. CAR:")).title()
fav_city =str(input("FAV. CITY:")).title()
mother_name =str(input("MOTHER'S NAME:")).title()
father_name = str(input("FATHER'S NAME:")).title()
fav_rapper = str(input("FAV. RAPPER:")).title()

numbers = random.randint(0,99)
spc_character = random.choice("_@#$%&*-")
names = [fav_car,fav_rapper,fav_city,mother_name,father_name , numbers ,spc_character]
name1 = random.choice(names)
name2 = random.choice(names)
if name1 != name2:
    print(f'{name2}{spc_character}{name1}{numbers}')