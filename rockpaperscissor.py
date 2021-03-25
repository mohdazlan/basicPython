computer_choice = 'scissors'
user_choice = input('Do you want a rock, paper or scissors?\n')
if computer_choice == user_choice:
    print("SERI")
elif user_choice == "rock" and computer_choice == "scissors":
    print("User win")
elif user_choice == "paper" and computer_choice == "rock":
    print("User Win")
elif user_choice =="scissors" and computer_choice =="paper":
    print("User Win")
else:
    print("You lose :( compuer Win :)")