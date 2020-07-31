#!/usr/bin/env python3
dict = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
char_name = input('Which hero do you want to know more about? Flash, Batman, Superman: ')
char_stat = input(' What statistic do you want to know about? strength, speed, or intelligence: ')
answer = 0
while True:
    if char_name == "flash" and char_stat == "speed":
        print(dict["flash"]["speed"])
        break
    elif char_name == "flash" and char_stat == "intelligence":
        print(dict["flash"]["intelligence"])
        break
    elif char_name == "flash" and char_stat == "strength":
        print(dict["flash"]["strenght"])
        break


    if char_name == "batman" and char_stat == "speed":
        print(dict["batman"]["speed"])
        break
    elif char_name == "batman" and char_stat == "intelligence":
        print(dict["batman"]["intelligence"])
        break
    elif char_name == "batman" and char_stat == "strength":
        print(dict["batman"]["strength"])
        break


    if char_name == "superman" and char_stat == "speed":
        print(dict["superman"]["speed"])
        break
    elif char_name == "superman" and char_stat == "intelligence":
        print(dict["superman"]["intelligence"])
        break
    elif char_name == "superman" and char_stat == "strength":
        print(dict["superman"]["strength"])
        break