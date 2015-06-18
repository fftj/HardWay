from random import randint

number_of_rooms = 3

gold_in_rooms = [2, 40, 99]
hp_in_rooms = [5, 7, 10]
hero_hp = 25
hero_mp = 0

def room_message(room_number):
    print "The hero walks into a room number %s" % room_number
    print "There's a big ugly grue in the room!"
    print "The grue has %s HP and seems to be very evil!"
    print "Hero has no choice but take a sword and kill the creature."

def die(string):
    print(string)
    exit(0)

def room_fight(room_number, hero_hp):
    hero_hp -= randint(0,7*(room_number+1))
    if hero_hp > 0:
        print "Hero won a battle! He got %s gold and still owns %s HP." % (gold_in_rooms[room_number],hero_hp)
    else:
        die("The hero dies!")
    return(hero_hp)

print """ The dark dungeon awaits.
There are %s rooms in the dungeon, and you have to crawl all of them.
In each room you'll see the treasure and the monster. Of course, 
you have to kill treasure and get the monster. Or vice versa!

Descend!
""" % number_of_rooms

i = 0
while i < number_of_rooms:
    hero_hp=room_fight(i, hero_hp)
    i+=1
