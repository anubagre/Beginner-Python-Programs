#Dobble Game
import string
import random
while(True):
    symbol=list(string.ascii_letters)
    card1=[0]*8
    card2=[0]*8
    pos1=random.randint(0,7)
    pos2=random.randint(0,7)
    samesym=random.choice(symbol)
    symbol.remove(samesym)
    card1[pos1]=samesym
    card2[pos2]=samesym
    for i in range(8):
        if i!=pos1:
            card1[i]=random.choice(symbol)
            symbol.remove(card1[i])
        if i!=pos2:
            card2[i]=random.choice(symbol)
            symbol.remove(card2[i])
    print(card1,"\n",card2)
    ans=input("Enter symbol that is same on both the cards:")
    if ans==samesym:
        print("Right")
    else: print("Wrong")
    ch=input("Continue(Y/N)?")
    if ch.upper()=="N":
        break
    
