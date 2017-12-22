import random
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
list2=['heart','spade','club','diamond']
def card1():
    y=random.randint(1,14)
    z=random.randint(0,3)

    cardval=list[y]
    ty=list2[z]
    if cardval==11:
        denom='J'

    elif cardval==12:
        denom='Q'
    elif cardval==13:
        denom='K'

    elif cardval==14:
        denom='A'

    else:
        denom="%s"%(list[y])

    print("card 1:  %s %s"%(ty,denom))

def card2():
    y = random.randint(0, 13)
    z = random.randint(0, 3)

    cardval = list[y]
    ty = list2[z]
    if cardval == 11:
        denom = 'J'

    elif cardval == 12:
        denom = 'Q'
    elif cardval == 13:
        denom = 'K'

    elif cardval == 14:
        denom = 'A'

    else:
        denom = "%s" % (list[y])

    print("card 2:  %s %s" % (ty, denom))



card2()
card1()
