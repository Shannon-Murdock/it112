import random 

###################################

choices = ["rock","paper","scissors"]
stage.set_background_color("HotPink")

#
computer = codesters.Sprite("dracula",-150,0)
user = codesters.Sprite("ghost",150,0)

####################################

#
user_choice = user.ask("Please enter rock, paper, scissors")


while user_choice not in choices:
    user_choice = user.ask("You did not enter rock, paper, scissors. Please re-enter")
    
user.load_image(user_choice)

#####################################
#Computer Choice

for i in range(random.randint(10,25)):
    
    comp_choice = random.choice(choices)
     
    computer.load_image(comp_choice)
    

winner = codesters.Text("",0,150)

############################################
#Game Logic - Conditional and Nested Conditionals. 

#
if user_choice == comp_choice:
    winner.set_text("Tie")
    
    
elif user_choice == "rock":
    if comp_choice == "paper":
        winner.set_text("Computer Wins")
    else:
        winner.set_text("End User Wins!")
        


elif user_choice == "paper":
    if comp_choice == "scissors":
        winner.set_text("Computer Wins!")
    else:
        winner.set_text("End User Wins")


else:
    
    if comp_choice == "rock":
        winner.set_text("Computer Wins!")
    else:
        winner.set_text("Scissors Beats Paper End User Wins")