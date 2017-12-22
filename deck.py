
##throws out randomm cards out of the deck 
## update 2 checks if the Ace value is 1 or 10 depending on the user 
import random
list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list2=['heart','spade','club','diamond']
def checku():
   try:
    dec=int(input("Its an ACE decide between 1 & 10"))
    return dec
   except:
    print("please enter a number")
def card1():
    y=random.randint(0,12)
    z=random.randint(0,3)

    cardval=list[y]
    ty=list2[z]
    if cardval==1:
        i=checku()
        cardval=i
        denom='A'
    elif cardval==11:
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
    y = random.randint(0, 12)
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
