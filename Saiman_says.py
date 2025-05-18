#Saiman-Says Game
import random
a=["Saiman",""]
print("\nLet's play Saiman Game")
print("Rule:Only enter when computer says Saiman")
print("Let's see who earns more points")
r=0
t=0
while True:
    comp=random.choice(a)
    print("{} says, press enter to continue or 'no' to skip".format(comp))
    g=input("")
    if(comp=="Saiman"):
        if(g==""):
            r=r+1
            print("Congrats! You got a point")
        else:
            t=t+1
            print("Oops! You missed a chance, that was Saiman")
    else:
        if(g==""):
            t=t+1
            print("Oops! You fell for the trick, That wasn't Saiman")
        elif(g=="no"):
            r=r+1
            print("Nice! You ignored the fake command and got a point")
    n=input("Do you want to continue?(yes/no):").lower()
    if(n=="yes"):
        continue
    else:
        print("Thanks for playing")
        print("Final Scores are: {} points and {} mistakes".format(r,t))
        break
            


