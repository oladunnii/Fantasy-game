print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the legendary Gem of Power, hidden deep within the ancient ruins of Eldoria.\nMany have tried, but none have returned. Will you succeed?")
choice1 = input('You stand at the entrance of a mysterious forest. The towering trees cast long shadows,'
                'and the air is thick with the scent of damp earth and hidden secrets.In front of you, the path splits into two:? '
                'Type "left" or "right".\n').lower()
if choice1 =="left":
    choice2=input("As you step forward, the air shimmers, and suddenly, the world around you shifts. "
          "You find yourself standing before an ancient willow tree, its hollow trunk glowing faintly. A ghostly figure appears. "
          "The ghost introduces itself as Liora, the Guardian of the Woods. She offers you a choice: take the Elixir of the Moon, which grants knowledge of the forest, or a Silver Dagger,"
          " which can cut through dark magic."
           'Type "Elixir" or "Dagger".\n').lower()
    if choice2 == "elixir":
        choice3=input(" you survived, you enter the ruins, a vast temple with cracked stone pillars and faded murals depicting a powerful gemstone. "
                      "Three tunnels lead deeper inside:the Left Tunnel: A narrow passage filled with thick spiderwebs and faint clicking sounds."
                      "The Middle Tunnel: A long hallway lit by eerie blue torches. Strange symbols glow on the walls."
                      "The Right Tunnel: A dark corridor where the air smells of sulfur and something growls in the distance."
                      'Type "left" or "middle" or "right"\n').lower()
    elif choice2 == "dagger":
        choice3 = input("you survived, you enter the ruins, a vast temple with cracked stone pillars and faded murals depicting a powerful gemstone. "
                        "Three tunnels lead deeper inside:the Left Tunnel: A narrow passage filled with thick spiderwebs and faint clicking sounds."
                        "The Middle Tunnel: A long hallway lit by eerie blue torches. Strange symbols glow on the walls."
                        "The Right Tunnel: A dark corridor where the air smells of sulfur and something growls in the distance."
                        'Type "left" or "middle" or "right"\n').lower()
    if choice2 == "dagger" and  choice3 == "right":
         choice4= input("The growling grows louder. A monstrous shadow beast lunges at you!"
                           "If you have the Silver Dagger, you stab it, and it howls before vanishing."
                           "You arrive at a grand chamber. In the center, on a pedestal, lies the Gem of Power, pulsing with ancient energy."
                           "But as you step forward, three statues come to life, blocking your path."
                           "The Guardian of Wisdom: 'Prove your mind!'"
                           "The Guardian of Shadows: 'Prove your courage!'"
                            'Type "wisdom"  or "shadows"\n').lower()
    if choice2 == "elixir" and  choice3 == "middle":
            choice4 = input("The glowing symbols pulse as you step forward. Suddenly, a voice echoes:"
                            "Speak the word of power, or be lost forever."
                            "If you have the Elixir of the Moon, you recall the ancient word: 'Eldorath'. The path opens."
                            "You arrive at a grand chamber. In the center, on a pedestal, lies the Gem of Power, pulsing with ancient lenergy."
                           "But as you step forward, three statues come to life, blocking your path."
                           "The Guardian of Wisdom: 'Prove your mind!'"
                           "The Guardian of Shadows: 'Prove your courage!'"
                           'Type "wisdom"  or "shadows"\n').lower()
            if choice4== "wisdom":
                choice5=input("The Wisdom Guardian presents a riddle:"
                              "I have keys but open no locks, I have space but no room, you can enter but not go outside. What am I?").lower()
                if choice5=="keyboard":
                    print("The Guardian nods and steps aside the path is clear. You step forward, grasp the Gem of Power, and feel its energy surge through you. "
                          "The temple rumbles, but before it collapses, a secret door opens, leading you safely outside."
                          "Congratulations! You have won the game.")
                else:
                    print("Wrong answer kindly try again")
            elif choice4=="shadows":
                print("The Shadow Guardian surrounds you with illusions of your deepest fears. If you stand still and refuse to be deceived, "
                      "the illusion fades, and you move forward, you are lost in the darkness. Game Over.")
            else:
                print("Invalid choice.Game over.")
    else:
            print("oops Game over!!!")
else:
    print("Ooops Game over!!!")

