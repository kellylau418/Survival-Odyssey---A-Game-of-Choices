'''
CYOA Squid Game
Kelly Lau
'''
import random
import sys


def character():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point


    character_options = "123"
    print("*"*20)
    print("\nChoose your character")

    print("\nYou have three choices.")
    print("-"*20)
    print("\n1 - Seong Gi-hun")
    print("2 - Ji-yeong")
    print("3 - Kang Sae-byeok")
    print("4 - Random")

    
    command = input("\nEnter your choice: ")

    if command == "1":
        character_seong_gi_hun()
        
    elif command == "2":
        character_ji_yeong()

    elif command == "3":
        character_kang_sae_byeok()

    elif command == "4":
        random_command = random.choice(character_options)
        random_character()

    else:
        print("\nThat choice does not exist, please try again")
        character()
        
def random_character():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point

    print(random_command)
    if random_command == "1":
        print("Randomly chosen character: Seong Gi-hun")
        character_seong_gi_hun()
        
    elif random_command == "2":
        print("Randomly chosen character: Ji Yeong")
        character_ji_yeong()

    elif random_command == "3":
        print("Randomly chosen character: Kang Sae-byeok")
        character_kang_sae_byeok()


def character_seong_gi_hun():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    
    health_point = 3
    evilness_point = 0
    goodness_point = 0
    print("\n\nStory:\nYou're middle-age man living near the poverty line with millions of debt.\nYou recently lost your job and your daughter would move to another country with her mother.\nYou have absolutely no clue what to do with your life.") 
    print(f'A mysterious man came up and offered you to take part in a game that allows you to win 45.6 billion won.\nWith no other choices in life, you accepted the offer.\nYou are then brought to the location of the game.\nYou start off with {health_point} health points, 0 evilness point and 0 goodness point.')

    game_intro()

def character_ji_yeong():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point

    health_point = 1
    evilness_point = 0
    goodness_point = 0

    print("\n\nStory:\nYou're a young woman who was just released from jail after 15 year sentence for a murder committed when you were a child.\nYou came out and realized that you know no one and have nothing.\nYou don't have a single clue what to do with your life.")  
    print(f'A mysterious man came up and offered you to take part in a game that allows you to win 45.6 billion won.\nWith no other choices in life, you accepted the offer.\nYou are then brought to the location of the game.\nYou start off with {health_point} health points, 0 evilness point and 0 goodness point.')

    game_intro()

def character_kang_sae_byeok():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    

    health_point = 2
    evilness_point = 0
    goodness_point = 0
    print("\n\nStory:\nYou're a young woman who lived a horrible life in North Korea.\nYou escaped to South Korea with your younger brother, but your mother was caught and imprisoned.\nYou want to live a happy life with your family, but a heavy ransom was placed on your mother.\nYou must find a way to collect the fund and you feel hopeless with life.")
    print(f'A mysterious man came up and offered you to take part in a game that allows you to win 45.6 billion won.\nWith no other choices in life, you accepted the offer.\nYou are then brought to the location of the game.\nYou start off with {health_point} health points, 0 evilness point and 0 goodness point.')

    game_intro()


def game_intro():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    game_intro_options = '123'

    gi_health_point = health_point
    gi_evilness_point = evilness_point
    gi_goodness_point = goodness_point

    print("*"*20)
    show_points()

    print("\nYou enter a room.\nYou see hundreds of other game contestants and the speaker introduces the first game as 'Red Light, Green Light'.\nThe rule is to reach the end within 2 minutes, without being caught.\nYou're allowed to move when Green Light is called.\nYou must stay still when Red Light is called, and would get eliminated if caught moving.\nGreen Light was just called, what do you do?")

    print("\nYou have three choices.")
    print("-"*20)
    print("1 - Run")
    print("2 - Walk steadily")
    print("3 - Stay still")
    print("4 - loop back")
    print("5 - Random")

    
    command = input("\nEnter your choice: ")

    if command == "1":
        health_point -= 1
        print("\nRed Light was suddenly called and you almost got caught.\n-1 health point")

        health_pointf()
        
        mass_shooting("")

    elif command == "2":
        
        message = "\nRed Light was suddenly called and you were able to stop in time."
        mass_shooting(message)

    elif command == "3":
        
        message = "\nRed Light was suddenly called and you didn't move."
        mass_shooting(message)

    elif command == "4":
        
        print("\nYou chose to loop back\n")
        character()

    elif command == "5":
        random_command = random.choice(game_intro_options)
        random_game_intro()

    else:
        print("\nThat choice does not exist, please try again\n")
        game_intro()

def random_game_intro():
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point

    
    print(random_command)
    
    if random_command == "1":
        print("Randomly chosen option: Run")
        print("\nRed Light was suddenly called and you almost got caught. -1 health point")
    
        health_point -= 1
        health_pointf()
        
        mass_shooting("")
        
    elif random_command == "2":
        print("Randomly chosen option: Walk steadily")
        message = "\nRed Light was suddenly called and you were able to stop in time."
        mass_shooting(message)
        
    elif random_command == "3":
        print("Randomly chosen option: Stay still")
        message = "\nRed Light was suddenly called and you didn't move."
        mass_shooting(message)

def mass_shooting(message):
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    mass_shooting_options = "12"
    
    print(message)
   
    print("*"*20)   
    show_points()

    ms_health_point = health_point
    ms_evilness_point = evilness_point
    ms_goodness_point = goodness_point
    
    print("\nA group of people were caught moving and shot death on sight.\nThe whole crowd of people were frightened and ran back to the entrance to escape from the game, while Red Light was still on.\nFear and confusion also engulfs you.\nWhat do you do?")

    print("\nYou have two choices.")
    print("-"*20)
    print("1 - Run")
    print("2 - Stay Still")
    print("3 - loop back")
    print("4 - Random")


    
    command = input("Enter your choice: ")

    if command == "1":
        print("\nYou are caught moving while Red Light is still on.\nYou are shot on site.\nYou are dead.")

    elif command == "2":
        message = "\nYou stay still and followed the rules.\nAs a reuslt, the machine didn't shoot you."
        struggling_old_man1(message)

    elif command == "3":
        print("\nYou chose to loop back")
        health_point = gi_health_point
        game_intro()

    elif command == "4":
        random_command = random.choice(mass_shooting_options)
        random_mass_shooting()

    else:
        print("\nThat choice does not exist, please try again")
        mass_shooting("")


def random_mass_shooting():
    global random_command
    
    print(random_command)

    if random_command == "1":
        print("Randomly chosen option: Run")
        print("\nYou are caught moving while Red Light is still on.\nYou are shot on site\nYou are dead.")

    elif random_command == "2":
        print("Randomly chosen option: Stay still")
        message = "\nYou stay still and followed the rules.\nAs a reuslt, the machine didn't shoot you."
        struggling_old_man1(message)
        
    
def struggling_old_man1(message):
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    struggling_old_man1_options = "12"

    print(message)

    print("*"*20)
    show_points()
    
    som1_health_point = health_point
    som1_evilness_point = evilness_point
    som1_goodness_point = goodness_point
    
    print("\nYou then see an elderly man struggling to keep up with the game.\nWhat will you do?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - Help the man")
    print("2 - Use the man as a shield and keep moving")
    print("3 - loop back")
    print("4 - Random")


    
    command = input("Enter your choice: ")

    if command == "1":
        message = "\nYou did a good deed.\n+1 goodness point"
        goodness_point += 1
        struggling_old_man2(message)
        
    elif command == "2":
        message = "\nYou did an evil deed.\n+1 evilness point"
        evilness_point += 1
        struggling_old_man2(message)

    elif command == "3":
        print("\nYou chose to loop back")
        health_point = ms_health_point
        goodness_point = ms_goodness_point
        evilness_point = ms_evilness_point
        mass_shooting("")

    elif command == "4":
        random_command = random.choice(struggling_old_man1_options)
        random_struggling_old_man1()
        

    else:
        print("\nThat choice does not exist, please try again")
        struggling_old_man1("")
        
def random_struggling_old_man1():
    global health_point, evilness_point, goodness_point, random_command
    
    print(random_command)
    
    if random_command == "1":
        print("Randomly chosen option: Help the man")
        message = "\nYou did a good deed.\n+1 goodness point"
        goodness_point += 1
        struggling_old_man2(message)
        
    elif random_command == "2":
        print("Randomly chosen option: Use the man as a shield and keep moving")
        message = "\nYou did an evil deed.\n+1 evilness point"
        evilness_point += 1
        struggling_old_man2(message)
    
        
def struggling_old_man2(message):
    global random_command, health_point, evilness_point, goodness_point, gi_health_point,gi_evilness_point, gi_goodness_point, ms_health_point,ms_evilness_point,ms_goodness_point,som1_health_point, som1_evilness_point,som1_goodness_point,som2_health_point,som2_evilness_point,som2_goodness_point
    struggling_old_man2_options = "1234"

    print(message)

    print("*"*20)
    show_points()
    
    som2_health_point = health_point
    som2_evilness_point = evilness_point
    som2_goodness_point = goodness_point
    
    print("\nRed Light was suddenly called and the old man loses his balance.\nWhat do you do?")
    print("\nYou have four choices.")
    print("-"*20)
    print("1 - Not help him")
    print("2 - Push him away from you")
    print("3 - Attempt to help him")
    print("4 - Help him with all your strength ")
    print("5 - Loop back")
    print("6 - Random")

    command = input("Enter your choice: ")

    if command == "1":
        message = "\nYou decided to not help him.\nHe died as a result.\nEventually, you reach the finish line.\n+1 evilness point"
        evilness_point += 1
        end_game1(message)
        
    elif command == "2":
        print("\nThe old man was eliminated as result.\nYou somewhat moved and was almost caught.\nEventually, you reach the finish line.\n-1 health point & +1 evilness point")
        health_point -= 1
        evilness_point += 1
        health_pointf()
        end_game1("")
        
    elif command == "3":
        message = "\nYou tried to help him, but failed.\nEventually, you reach the finish line.\n +1 goodness point"
        goodness_point += 1
        end_game1(message)

    elif command == "4":
        print("\nYou moved in effort in helping the old man.\nYou were caught and shot on sight.\nYou are dead")
        
    elif command == "5":
        print("\nYou chose to loop back")
        health_point = som1_health_point
        goodness_point = som1_goodness_point
        evilness_point = som1_evilness_point
        struggling_old_man1("")

    elif command == "6":
        random_command = random.choice(struggling_old_man2_options)
        random_struggling_old_man2()

    else:
        print("\nThat choice does not exist, please try again")
        struggling_old_man2("")

def random_struggling_old_man2():
    global health_point, evilness_point, goodness_point,random_command
    print(random_command)

    if random_command == "1":
        print("Randomly chosen option: Not help him")
        message = "\nYou decided to not help him.\nHe died as a result.\nEventually, you reach the finish line.\n+1 evilness point"
        evilness_point += 1
        end_game1(message)
        
    elif random_command == "2":
        print("Randomly chosen option: Push him away from you")
        print("\nThe old man was eliminated as result.\nYou somewhat moved and was almost caught.\nEventually, you reach the finish line.\n-1 health point & +1 evilness point")
        health_point -= 1
        evilness_point += 1
        health_pointf()
        end_game1("")
        
    elif random_command == "3":
        print("Randomly chosen option: Attempt to help him")
        message = "\nYou tried to help him, but failed.\nEventually, you reach the finish line.\n +1 goodness point"
        goodness_point += 1
        end_game1(message)

    elif random_command == "4":
        print("Randomly chosen option: Help him with all your strength")
        print("\nYou moved in effort in helping the old man.\nYou were caught and shot on sight.\nYou are dead")
        

def end_game1(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nCongratulation, you survived the first game, Red Light Green Light.")
    print("\nNow, you're moving onto the 2nd game-- the Sugar Comb Game.\nYou enter the new stadium and you're ordered to stand in front of a shape.\nThe options are: triangle and umbrella.\nWhat will you choose?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - The umbrella")
    print("2 - The triangle")
    print("3 - loop back")

    
    command = input("Enter your choice: ")

    if command == "1":
        message = "\nTurned out, the rules are to cut the shape out perfectly using a needle.\nIf the honey-comb breaks in the process or the cut-out shape is imperfect, you are eliminated (AKA death).\nYou're now supposed to cut the umbrella shape out, which is the harder shape to work with."
        young_child_steal(message)
        
    elif command == "2":
        message = "\nTurned out, the rules are to cut the shape out perfectly using a needle.\nIf the honey-comb breaks in the process or the cut-out shape is imperfect, you are eliminated (AKA death).\nYou're now supposed to cut the triangle shape out, which is fairly easy."
        young_child_switch(message)

    elif command == "3":
        print("\nYou chose to loop back")
        health_point = som2_health_point
        goodness_point = som2_goodness_point
        evilness_point = som2_evilness_point
        struggling_old_man2("")

    else:
        print("\nThat choice does not exist, please try again")
        end_game1("")

def young_child_steal(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nYou see a little child with the triangle shape, which is much easier to work with.\nDo you steal it?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - Yes")
    print("2 - No")
    print("3 - loop back")

    
    command = input("Enter your choice: ")

    if command == "1" and evilness_point > goodness_point:
        print("\nYou choose to steal the Honey-Comb from an innocent, young child.\nOthers see it and they all gang up on you.\nYour Honey-Comb is broken in the process.\nYou're eliminated and shot on sight.\nYou are dead.")        

    elif command == "1" and evilness_point <= goodness_point:
        print("\nYou successfully stole it but got injured in the process.\n +1 evilness point & -1 health point.")
        health_point -= 1
        evilness_point += 1
        health_pointf()
        others_struggle("")

    elif command == "2":
        message = "\nYou choose to not steal it and begin tracing your own shape out of your Honey-Comb."
        gangster(message)
        
    elif command == "3":
        print("\nYou chose to loop back")
        end_game1("")

    else:
        print("\nThat choice does not exist, please try again")
        young_child_steal("")


def young_child_switch(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nThere's a yound child  trying to swap honey combs with you.\nWhat do you do?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - Let them take it")
    print("2 - Don't let them take it")
    print("3 - loop back")

    
    command = input("Enter your choice: ")

    if command == "1" and evilness_point > goodness_point:
        print("\nThey give you one that's close to, but not yet broken.\n-1 health point & +1 goodness point.")
        goodness_point += 1
        health_point -= 1
        health_pointf()
        small_fight("")
        
    elif command == "1" and evilness_point <= goodness_point:
        message = "\nTurned out, they give you one that's already perfectly cut out."
        congratualation(message)

    elif command == "2" and evilness_point > goodness_point:
        print("\nThey fight you for your Honey-Comb and it gets destroyed in the process.\nYou are shot and sight.\nYou are dead.")        

    elif command == "2" and evilness_point <= goodness_point:
        message = "\nNothing happens to you.\nKeep going."
        lighter(message)
   
    elif command == "3":
        print("\nYou chose to loop back")
        end_game1("")

    else:
        print("\nThat choice does not exist, please try again")
        young_child_steal("")


def lighter(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nYou then see someone using a lighter to cut their shape out.\nWhat do you do?")
    print("\nYou have three choices.")
    print("-"*20)
    print("1 - Steal it")
    print("2 - Ask if you could use it")
    print("3 - Mind your own business")
    print("4 - Loop back")
       
    command = input("Enter your choice: ")

    if command == "1":
        print("\nYou use it to cut out your shape, but someone tells on you.\nYou defied the rules and was eliminated.\nYou are shot on sight; you are dead.")
        
    elif command == "2" and evilness_point > goodness_point:
        print("\nThey didn't give it to you and you keep going on your own with your shape.\nEventually, you accidently break your Honey-Comb as you lack the skills to cut it out.\nYou are shot of sight; you are dead.")
              
    elif command == "2" and evilness_point <= goodness_point:
        print("\nThey don't let you use it.\nYou then fight for it and get injured.\nEventually, you manage to cut your shape out successfully.")
        health_point -= 1
        health_pointf()
        congratualation("")

    elif command == "3":
        message = "\nNothing happens and you keep going.\nEventually, you succeeded in cutting your shape out!"
        congratualation(message)
        
    elif command == "4":
        print("\nYou chose to loop back")
        young_child_switch("")        

    else:
        print("\nThat choice does not exist, please try again")
        lighter("")

def small_fight(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nSoon a small fight breaks out for a perfectly cut honey comb.\nDo you join the fight?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - No")
    print("2 - Yes")
    print("3 - Loop back")
    

    
    command = input("Enter your choice: ")

    if command == "1":
        print("\nYou continue with your own honeycomb, which was already fragile.\nIt suddenly breaks.\nYou are shot on sight; you are dead.")
        
    elif command == "2" and evilness_point >= goodness_point:
        message = "\nYou were able to dominate the fight considering the amount of evil experiences you had.\nYou got the perfectly cut Honey-Comb."
        congratualation(message)

    elif command == "2" and evilness_point < goodness_point:
        print("\nYou join the fight but wasn't able to take the perfectly cut honey comb.\nYou got injured in the process.\nBut eventually, you were able to cut your Honey-Comb shape.\n-1 health point")
        health_point -= 1
        health_pointf()
        congratualation("")

    elif command == "3":
        print("\nYou chose to loop back")
        goodness_point -= 1
        health_point += 1
        young_child_switch("")   

    else:
        print("\nThat choice does not exist, please try again")
        small_fight("")

def others_struggle(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nYou start cutting the shape out.\nMany others are struggling to finish their shapes.\nWhat do you do?")
    print("\nYou have two choices.")
    print("-"*20)
    print("1 - You make fun of them.")
    print("2 - You mind your own business")
    print("3 - loop back")

    
    command = input("Enter your choice: ")

    if command == "1":
        print("\nYou've angered them.\nThey decided to fight and break your Honey-Comb in the process.\nYou're shot on sight; you are dead.")
              
    elif command == "2" and evilness_point > goodness_point:
        print("\nThey suddenly lost their mind and proceeded to attack everyone in the area.\nYou were caught in the mess and was injured.\nEventually, you successfully cutted out your shape.\n-1 health point")
        health_point -= 1
        health_pointf()
        congratualation("")
        
    elif command == "2" and evilness_point <= goodness_point:
        message = "\nThey didn't bother you.\nEventually, you successfully cut our your shape."
        congratualation(message)
        
    elif command == "3":
        print("\nYou chose to loop back")
        health_point += 1
        evilness_point -= 1
        young_child_steal("")        

    else:
        print("\nThat choice does not exist, please try again")
        others_struggle("")

def gangster(message):
    global health_point, evilness_point, goodness_point

    print(message)

    print("*"*20)
    show_points()
    print("\nYou see a group of ganster-like contestents going around and taking other contestents' Honey-Combs who are close to being finished.\nWhat do you do?")
    print("\nYou have three choices.")
    print("-"*20)
    print("1 - You tell them to stop")
    print("2 - You try to join them")
    print("3 - You mind your own business")
    print("4 - loop back")

    command = input("Enter your choice: ")

    if command == "1":
        print("\nThe gangsters get mad and destroy your Honey-Comb in the process.\nYou are shot on sight; you are dead.")
        
    elif command == "2" and evilness_point >= goodness_point:
        print("\nYou do appear intimidating enough with your previous evil deeds.\nThey let you in and you end up getting a perfectly cut-up shape from some innocent lady.\nA fight broke out in the process though.\n-1 health point.")
        health_point -= 1
        health_pointf()
        congratualation("")
        
    elif command == "2" and evilness_point < goodness_point:
        print("\nThey reject you as you do not appear intimidating enough.\nYou eventually fail to cut your shape out.\nYou are shot on site; you are dead.")

    elif command == "3" and evilness_point > goodness_point:
        print("\nYou are close to finishing your Honey-Comb one of the 'gangsters' come and steal your shape, giving you a broken one in return.\nYou are eliminated since 'your Honey-Comb' is broken.\nYou are shot on sight; you are dead.")

    elif command == "3" and evilness_point <= goodness_point:
        message = "\nYou keep going and end up finishing your Honey-Comb shape."
        congratualation(message)

    elif command == "4":
        print("\nYou chose to loop back")
        young_child_steal("")        

    else:
        print("\nThat choice does not exist, please try again")
        gangster("")

def congratualation(message):
    print(message)
    print("*"*20)
    print("Congratualation, you successfully cut out the shape. You can now claim your 45.6 billion won and escape from this place.")


def health_pointf():
    global health_point

    if health_point <= 0:
        print("Your health point reached zero.\nYou died while participating the game.\nYou are dead.")
        sys.exit()

def show_points():
    global health_point, evilness_point, goodness_point
    print(f'Current health point = {health_point}')
    print(f'Current evilness point = {evilness_point}')
    print(f'Current goodness point = {goodness_point}')
        


    
   
#MAIN
global health_point
global evilness_point
global niceness_point
global random_command
global gi_health_point
global gi_evilness_point
global gi_niceness_point
global ms_health_point
global ms_evilness_point
global ms_goodness_point
global som1_health_point
global som1_evilness_point
global som1_goodness_point
global som2_health_point
global som2_evilness_point
global som2_goodness_point


character()
