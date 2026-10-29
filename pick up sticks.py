import random
sticks = 27
global play
play = True

def pick_up(sticks, num, play):
    while num>3 or num<1:
        print("You can only pick up 1-3 sticks! Try again")
        num = int(input(""))
    if num<=3 and num>=1 and sticks>num:
        sticks-=num
    elif sticks<=num:
        sticks = 0
    return sticks
def comp_pick_up(sticks, rand, play):
    if sticks>rand:
        sticks-=rand
    elif sticks<=rand:
        sticks = 0
    return sticks

while play == True:
    r = random.randint(1,3)
    #player picks up sticks
    n = int(input("How many sticks would you like to pick up?"))
    sticks = pick_up(sticks, n, play)
    print(sticks, "sticks left")
    if sticks == 0:
        #if player picks up last stick, they lose
        print("You lose")
        break
    #computer picks up sticks
    print("I picked up", r)
    sticks = comp_pick_up(sticks, r, play)
    print(sticks, "sticks left")
    if sticks == 0:
        #if computer picks up last stick, it loses
        print("You win")
        play = False
