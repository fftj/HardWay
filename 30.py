people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take care the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print  "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take buses."
else:
    print "We still can't decide."

if people > buses:
    print "Allright, let's just take buses."
else: 
    print "Fine, let's stay home then"