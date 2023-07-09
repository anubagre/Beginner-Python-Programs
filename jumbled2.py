import random

def choose():
    words=['rainbow', 'brownie', 'blackhole','silver','habit', 'chocolate','coffee', 'sunsilk','mathematics','universe','shakespeare','technology','photosynthesis','pshycology']
    selected=random.choice(words)
    return selected

def jumble(word):
    jumbled=random.sample(word, len(word))
    return jumbled

def play():
    p1=input('Player 1:')
    p2=input('Player 2:')
    pp1=0; pp2=0; turn=0
    while(True):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1+", It is your turn!")
            ans=input("Enter Answer:")
            if ans==picked_word:
                pp1+=1
                print(p1,",Your Score:",pp1)
            else:
                print("The answer is:", picked_word)
        c=int(input("Continue?(0/1)"))
        if c==0:
            print('Scores-', p1,':',pp1,'and', p2,':',pp2)
            if pp1>pp2:
                print(p1,"won")
            elif pp1==pp2:
                print("It is draw")
            else:
                print(p2,'won')
            break

        else:
            print(p2+", It is your turn!")
            picked_word=choose()
            qn=jumble(picked_word)
            print(qn)
            ans=input("Enter Answer:")
            if ans==picked_word:
                pp2+=1
                print(p2,",Your Score:",pp2)
            else:
               print("The answer is:", picked_word)
            c=input("Continue?(0/1)")
            if c==0:
                print('Scores-', p1,':',pp1,'and', p2,':',pp2)
                if pp1>pp2:
                    print(p1,"won")
                else:
                    print(p2,'won')
                break
        turn+=1
    
play()
