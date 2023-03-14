import random
print ("Do you want to play ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand=[]
computer_hand=[]
def deal_cards():
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    first_player_hand = player_hand[0] + player_hand[1]
    print(f"Your hand is: {player_hand}")
    print(f"The computer's hand for now is: {computer_hand}")
    choice=input("Would you like to 'stand' or 'hit'")
    if choice=="hit":
        hit_a_card(player_hand)
    else:
        deal_computer_cards()

def hit_a_card(player_hand_hit):
        player_hand.append(random.choice(cards))
        if (int(sum(player_hand))>21):
            check_if_ace()
        else:
            print (f"Your hand now is {player_hand}")
            choice2=input("Would you like to 'stand' or 'hit'")
            if choice2=="hit" and (int(sum(player_hand))<21) :
                 hit_a_card(player_hand)
            elif choice2=="stand" and (int(sum(player_hand))<21) :
                deal_computer_cards()
            
def check_if_ace():
    hasAce=0
    for i in range (0, len(player_hand)):
        if int(player_hand[i])==11:
            player_hand[i]=1
            print("Your ace has turned into a 1")
            hasAce=1
    if(hasAce==1):
        hit_a_card(player_hand)
    else:
        print(f"You busted with cards {player_hand}")
def check_if_ace_computer():
    hasAceComputer=0
    for j in range(0, len(computer_hand)):
        if int(computer_hand[j])==11 and hasAceComputer!=1:
            computer_hand[j]=1
            print(f"The computer's ace has been now turned into {computer_hand}")
            hasAceComputer=1
    if (hasAceComputer==1):
        deal_computer_cards()
    else:
        print(f"You win, the computer busts with a {sum(computer_hand)}")
        
    

def deal_computer_cards():
    while sum(computer_hand)<=17:
        computer_hand.append(random.choice(cards))
    print(f"The computer's next hand is: {computer_hand}")
    if sum(computer_hand)>21:
        check_if_ace_computer()
    else:
        compare()


def compare():
    if sum(computer_hand)>sum(player_hand):
        print("You lose, the computer wins")
    elif sum(computer_hand)<sum(player_hand):
        print("You win, the computer loses")
    else:
        print("Draw")

go_on=True
while go_on:

    deal_cards()
    go_on_choice=input("Would you like to play again? Type 'yes' or 'no': ")
    if go_on_choice == "yes":
        go_on=True
        player_hand=[]
        computer_hand=[]
    else:
        go_on=False