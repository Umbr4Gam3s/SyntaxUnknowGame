import random

player_name = ""
player_age = 0
year_time = 0
day_time = 0
month_time = 0

skills = {
    "Hacking": 5, 
    "Charisma": 5, 
    "Strength": 5, 
    "Defense": 5, 
    "Dexterity": 5, 
    "Agility": 10
}

inventory = {
    "laptop": 1, 
    "phone": 1, 
    "cash": 500
}

class Character:
    def __init__(self, name, description, dialogue):
        self.name = name
        self.description = description
        self.dialogue = dialogue

byte = Character(
    "ByTeR", 
    "Byte, short for ByTeR a child prodigy, was recruited by a shadowy hacker group at 14. Now in their mid-20s, they are feared underground hackers known for bypassing firewalls and working cryptically.", 
    "Hey, I'm Byte. Don't expect me to hold your hand, okay?"
)

vox = Character(
    "Voxol", 
    "Vox, short for Voxol once a top-tier security firm member, now works independently to combat illegal surveillance and corporate espionage, exposing corrupt organizations' secrets and breaking the law for justice.", 
    "The system is broken, but it's my job to fix it."
)

luna = Character(
    "Luna", 
    "Luna, a mathematician with a deep understanding of algorithms and cryptographic systems, left corporate life after a tragedy to expose malicious encryption exploiters, obsessed with cracking unbreakable codes.", 
    "If you want to talk encryption, I'm your person."
)

def intro():
    global player_name, player_age, year_time, month_time, day_time
    
    print("\nWelcome to Syntax: Unknown.")
    print("\nYou awaken in an alleyway, the last thing you remember is running from a police officer.")
    print("\n'Hey! Hey! Wake up!'")
    player_name = input("\n'Welcome back, are you okay? What's your name, friend?' > ")

    while True:
        player_age_input = input(f"'Well, hello {player_name}! How old are you?' > ")
        try:
            player_age = int(player_age_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid age (number).")

    while True:
        year_time_input = input(f"'Well, {player_name}... Do you remember what year it is?' > ")
        try:
            year_time = int(year_time_input)
            if year_time < 2030 or year_time > 2400:
                print("Please enter a reasonable year (2030-2400).")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid year (number).")

    while True:
        month_time_input = input(f"'That's right! It's {year_time}! Do you remember what month it is?' > ")
        try:
            month_time = int(month_time_input)
            if month_time < 1 or month_time > 12:
                print("Please enter a valid month (1-12).")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid month (1-12).")

    while True:
        day_time_input = input(f"'That's right! It's {month_time}! Do you remember what day it is?' > ")
        try:
            day_time = int(day_time_input)
            if day_time < 1 or day_time > 31:
                print("Please enter a valid day (1-31).")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid day (1-31).")

    print("\n'Well, I think your head is fine, but physically....' Luna examines your body, 'Bah! You'll be fine... Probably.'")

def luna_intro():
    while True:
        go_with_luna = input(f"Well, {player_name}, do you wanna come with me? (yes/no or y/n) > ").lower()

        if go_with_luna in ["no", "n"]:
            print("\nOh.. Okay, I understand.")
            break
        elif go_with_luna in ["yes", "y"]:
            print("\nOkay! Let's go!")
            break
        else:
            print("\nPlease answer with 'yes', 'y', 'no', or 'n'.")

def replay_game():
    while True:
        intro()
        luna_intro()

        play_again = input("\nWould you like to play again? (yes/no or y/n) > ").lower()
        if play_again in ["no", "n"]:
            print("Thank you for playing!")
            break
        elif play_again in ["yes", "y"]:
            print("Restarting the game...\n")
        else:
            print("Invalid input! Please answer with 'yes', 'y', 'no', or 'n'.")

replay_game()