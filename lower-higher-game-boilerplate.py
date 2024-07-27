from game_data import data
import random
from art import logo, vs

def get_random_account():
  """Get data from random account"""
  #return a random element from data

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 


def game():
  print(logo)
  #Initialise score to zero
  
  game_should_continue = True
  #Assign random accounts to the account_a and account_b
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    #swap accounts, account_a becomes account_b and account_b get a random account.

    #while both accounts are same, give account_b a random account.

    #Intialise the prompts for the game.
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    #Ask for A or B, who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #Assign follower_count to two variables a_follower_count and b_follower_count from respective accounts
    
    
    #use check_answer function and pass it the respective values to assign a boolean to is_correct
    

    if is_correct:
      #increase the score and print you are right with the current score.
      pass

    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()