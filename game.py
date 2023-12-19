print("************************* WELCOME TO THE ROCK-PAPER-SCISSORS *************************")
enter=""
start=input("\nPress Enter to Start the game ")
print("Let's see the Instructions/Rules of the game\n1.Rock beats Scissors\n2.Scissors beat Paper\n3.Paper beats Rock.\n")
import random
import speech_recognition as sr
import win32com
import win32com.client as wi
speaker = win32com.client.Dispatch("SAPI.SpVoice")
import time
import os

def win32cm(text):
    os.system(f" {text}")
    
def game_play():
    choice=['Rock','Paper','Scissors']
    user_choice=input("Choose the option as \n1.Rock\n2.Paper\n3.Scissors\n\n-> ")
    computer_choice=random.choice(choice)
    player_score=0
    computer_score=0
    
    print("Your Choice is ", user_choice ," and Computer choice is ",computer_choice)
    
    while True:
        if user_choice=="Rock" and computer_choice=="Rock":
            print("->Tie")
            s=("It's a Tie")
            speaker.Speak(s)
                        
        elif user_choice=="Rock" and computer_choice=="Paper":
            computer_score+=1
            print("->You Lose")
            s=("O You lose")
            speaker.Speak(s)
                        
        elif user_choice=="Rock" and computer_choice=="Scissors":
            player_score+=1
            print("->You Win")
            s=("you win")
            speaker.Speak(s)
                        
        elif user_choice=="Paper" and computer_choice=="Paper":
            print("->Tie")
            s=("It's a Tie")
            speaker.Speak(s)
                    
        elif user_choice=="Paper" and computer_choice=="Scissors":
            computer_score+=1
            print("->You Lose")
            s=("O You lose")
            speaker.Speak(s)
                    
        elif user_choice=="Paper" and computer_choice=="Rock":
            player_score+=1
            print("->You Win")
            s=("you win")
            speaker.Speak(s)
                    
        elif user_choice=="Scissors" and computer_choice=="Scissors":
            print("->Tie")
            s=("It's a Tie")
            speaker.Speak(s)
                        
        elif user_choice=="Scissors" and computer_choice=="Rock":
            computer_score+=1
            print("->You Lose")
            s=("O You lose")
            speaker.Speak(s)
                
        elif user_choice=="Scissors" and computer_choice=="Paper":
            player_score+=1
            print("->You Win")
            s=("you win")
            speaker.Speak(s)
                        
        else:
            print("You have made a wrong choice\n Please enter a valid choice ")
        
        break
    print("\n----------Score----------")
    print("Your score: ",player_score,"\nComputer Score: ",computer_score)
game_play()
t=1
time.sleep(t)

while True:
    play_again=str(input("\nDo you want to Play Again?\nYes\nNo\n\n->"))
    if play_again=="Yes":
        print("---------------------------------------------------------------------------------------\n")
        games=game_play()
        continue
    else:
        print("Thank you for playing ROCK-PAPER-SCISSORS")
    break

feedback=input("Please provide your feedback for the game ")
print("Thank You for your vauable feedback")

print("---------------------------------------------------------------------------------------")