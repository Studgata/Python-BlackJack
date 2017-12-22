import random
list=["spades","hearts","diamond","clubs"]
def card1():

    for x in range(1):
      y=random.randint(1,11)

    for x in range (1):
      y1=random.randint(0,3)
      z=list[y1]
    return ("%s %s"%(y,z))

def card2():
    for x in range(1):
        y = random.randint(1, 11)
        if y==1 or y==11:
            print("if you want the Ace as 1 or 11")
            y=int(input("."))
    for x in range(1):
        y1 = random.randint(0, 3)
        z = list[y1]
        if y == 1 or y == 11:
            print("if you want the Ace as 1 or 11")
            y = int(input("."))


    return ("%s %s" % (y, z))


c1=card1()
c2=card2()

print(c1,c2)
