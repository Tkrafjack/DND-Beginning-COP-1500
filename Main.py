# Tylor Krafjack
# A DND inspired Role Playing Game
# Ty'rex Journey
from random import randint


def main():
    print(
        "Welcome to Artemis, the greatest village within the country of Ty'rex! Well, maybe not the greatest but a decent village none the less!")

    # Player Name Input
    player_name = input(
        "It's not often that we meet travelers out here. I dont mean to be rude, but what was your name again?")
    player_hp = 30
    companion_name = 'Vax'
    companion_hp = 40
    companion_healing = 3
    print("Ahh ", player_name, " nice to meet you my name is ", companion_name, ".", sep="")

    # weapon Options
    iron_sword = 6
    iron_mace = 5
    iron_spear = 7
    fist = 2
    companion_first_weapon = iron_sword

    # Choosing Weapon
    first_player_weapon_choice = int(input(
        "I'm not sure how you made it this long traveling through the dark forest without a weapon. I have a spare iron sword, mace, and spear. (type a number. 1 = sword, 2 = mace, and 3 = spear)"))

    # https://www.w3schools.com/python/python_conditions.asp
    # If statement to make first_player_weapon an ironSword, ironMace, or ironSpear
    if (first_player_weapon_choice == 1):
        first_player_weapon = iron_sword
        # first_player_weapon_dmg_type = 'slashing'
        print(
            "Wonderful choice! That sword is a versatile weapon that hits for a strong 6 slashing damage. Take a shield as well.")

    elif (first_player_weapon_choice == 2):
        first_player_weapon = iron_mace
        # first_player_weapon_dmg_type = 'bludgeoning'
        print(
            "Wonderful choice! That mace is a blunt weapon that hits for a hard 5 bludgeoning damage. Take a shield as well.")

    elif (first_player_weapon_choice == 3):
        first_player_weapon = iron_spear
        # first_player_weapon_dmg_type = 'piercing'
        print(
            "Wonderful choice! That spear is a strong weapon that hits for a strong 7 piercing damage. Take a shield as well.")

    else:
        first_player_weapon = iron_mace
        print("That's not a choice... here why dont you take this mace")

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Start of Skeleton Combat
    print("Now that you have a weapon you should try it out", end='. ')
    print(
        "We have a grave yard in the forest behind the inn that is frequented by skeletons, ghosts, and ghouls. Lets go to check it out.",
        end=' ')
    print(
        "After a 15 minute walk the graveyard is coming into view. Cracking twigs and rustling bushes alert both and Vax of an extremely close skeleton that went previously unnoticed.")
    print("(Players only have 30 Health Points so play carefully)")

    skeleton_hp = 15
    skeleton_dmg = 3
    attack_on_skeleton = int(input(
        "(In combat there will be options for the player to choose. 1 = weapon attack, 2 = unarmed attack, 3 = shield(Block all incoming damage))(Vax can grapple which will make the player do double damage))"))

    # If statement to check if the player is: weapon attacking, unarmed attacking, or shielding(not in loop so Vax can grapple skeleton this turn)
    if (attack_on_skeleton == 1):
        print("Successful Attack and Vax Successful Grappled")
        # If statement to check what weapon the player has
        # The weapon damage is being divided by 2

        if (first_player_weapon == iron_spear):
            skeleton_hp = skeleton_hp - first_player_weapon / 2
            print("The remaining HP for the skeleton is ", skeleton_hp,
                  ". \nSpears normally do 7 damage but are piercing damage which is half damage against skeletons and some other undead.",
                  sep="")
            player_hp = player_hp - skeleton_dmg
            print("The player is at ", player_hp, ".", sep="")
        # If program never makes it to the else... so swords are hitting like a mace

        elif (first_player_weapon == iron_mace):
            # Multiplication *
            skeleton_hp = skeleton_hp - first_player_weapon * 2
            print("The remaining HP for the skeleton is ", skeleton_hp,
                  " health. Maces normally do 6 damage but are bludgeoning damage which is doubled damage against skeletons and some other undead.",
                  sep="")
            player_hp = player_hp - skeleton_dmg
            print("The player is at ", player_hp, ".", sep="")

        elif (first_player_weapon == iron_sword):
            skeleton_hp = skeleton_hp - first_player_weapon
            print("The remaining HP for the skeleton is ", skeleton_hp,
                  ". Slashing damage is neutral against skeletons so the damage done is 6.", sep="")
            player_hp = player_hp - skeleton_dmg
            print("The player is at ", player_hp, ".", sep="")

    elif (attack_on_skeleton == 2):
        print("Successful Attack and Vax Successful Grappled")
        skeleton_hp = skeleton_hp - fist
        print(skeleton_hp)
        player_hp = player_hp - skeleton_dmg
        print("The player is at ", player_hp, ".", sep="")

    elif (attack_on_skeleton == 3):
        print("Successful Block and Vax Successful Grappled")
        skeleton_hp /= 1
        print("The skeleton is still at ", skeleton_hp, " health.", sep="")
        print("The player health remains at ", player_hp, ".", sep="")

    else:
        print("Type 1-3 next time to do something")
        skeleton_hp *= 1
        print("The skeleton is still at ", skeleton_hp, " health.", sep="")
        player_hp -= skeleton_dmg
        print("The player is at ", player_hp, ".", sep="")

    # While loop until defeat of the skeleton or you
    # https://www.w3schools.com/python/python_while_loops.asp
    # https://www.youtube.com/watch?v=ytXfaew7bCA&t=705s

    # The loop is looping previous elif statement
    skeleton_hp = int(skeleton_hp)
    while (skeleton_hp > 0):

        if (player_hp <= 0):
            break
        else:
            pass

            attack_on_skeleton = int(input(
                "The skeleton is now grappled which will result in double damage. What do you choose to do?(Same 1-3 a s above)"))

            if (attack_on_skeleton == 1):
                print("Successful Attack and double damage due to the skeleton being grappled by Vax")

                # Nested Elif to determine what weapon the player is using
                if (first_player_weapon == iron_spear):
                    skeleton_hurt = first_player_weapon
                    player_hp = player_hp - skeleton_dmg
                    print("The player is at ", player_hp, ".", sep="")
                # The weapon damage is being multiplied by 2 squared. The ** is an exponent

                elif (first_player_weapon == iron_mace):
                    skeleton_hurt = first_player_weapon * 2 ** 2
                    player_hp = player_hp - skeleton_dmg
                    print("The player is at ", player_hp, ".", sep="")

                else:
                    skeleton_hurt = iron_sword * 2
                    player_hp = player_hp - skeleton_dmg
                    print("The player is at ", player_hp, ".", sep="")

            elif (attack_on_skeleton == 2):
                print("Successful Attack and double damage due to the skeleton being grappled by Vax")
                skeleton_hurt = fist * 2
                player_hp = player_hp - skeleton_dmg
                print("The player is at ", player_hp, ".", sep="")

            elif (attack_on_skeleton == 3):
                print("Successful Block and Vax has the skeleton grappled")
                skeleton_hurt = 0
                print("The player is at ", player_hp, ".", sep="")

            else:
                print("Type 1-3 next time to do something")
                skeleton_hurt = 0
                player_hp = player_hp - skeleton_dmg
                print("The player is at ", player_hp, ".", sep="")

            skeleton_hp = int(skeleton_hp - skeleton_hurt)
            player_hp = player_hp
            print("The skeleton is at ", skeleton_hp, ".", sep="")

    # Define players death check
    def player_died():
        if (player_hp <= 0):
            replay = input(
                "The player has died fighting the good fight. Would you like to restart as a new champion?(Type: yes or no)")

            # If the player has died they can restart
            if (replay == 'yes'):
                main()

            else:
                quit()

        else:
            pass

    # Checking to see if the player has died
    player_died()

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print(
        "Hell yeah! Nice fighting there! I'd love to celebrate but we made a huge commotion. We should probably get out of here before... there's a ghoul heading right towards us.")
    print("Take the lead on this fight. You seem to know what you're doing.")

    ghoul_hp = 20
    ghoul_dmg = 4
    ghoul_name = 'ghoul'
    enemy_status = 'normal'

    enemy_fight_no_second(ghoul_hp, player_hp, first_player_weapon, ghoul_dmg, companion_hp, ghoul_name,
                          companion_healing, iron_spear, iron_mace, enemy_status, companion_first_weapon, fist)


#############################################################################################################################################################################

# neutral fight because the enemy has no weaknesses or strengths
def enemy_fight_no_second(enemy_hp, player_hp, first_player_weapon, enemy_dmg, companion_hp, enemy_name,
                          companion_healing, iron_spear, iron_mace, enemy_status, companion_first_weapon, unarmed):
    global enemy_hurt, enemy_hurt_companion
    while (enemy_hp > 0):

        # -----------------------------------------------------------------------------------------------------------------------------
        if (player_hp <= 0):
            break
        else:
            # pass
            # -----------------------------------------------------------------------------------------------------------------------------

            # Checking to see if Vax has reached 0 hp
            if companion_hp <= 0:
                print(
                    "Vax has passed out and can no longer assist in battle. Finish the fight quick so you can heal him")
                # who_attacks = 1

            else:
                who_attacks = int(input(
                    "From now you'll command both Vax and yourself in battle to allow more flexibility in combat(Type: 1 to move yourself first or 2 to move Vax first)"))

                # -----------------------------------------------------------------------------------------------------------------------------

                # While loop to make the player choose 1 or 2 for who_attacks
                while (who_attacks > 2 or who_attacks < 1):
                    who_attacks = int(input(
                        "From now you'll command both Vax and yourself in battle to allow more flexibility in combat(Type: 1 to move yourself first or 2 to move Vax first)"))

                # If player moves first
                if who_attacks == 1:
                    attack_on_enemy = int(input(
                        "You're moving first. 1 = weapon attack, 2 = unarmed attack, 3 = shield(Block all incoming damage)"))

                    # While loop to make the player choose 1-3 for attack_on_enemy
                    while (attack_on_enemy > 3 or attack_on_enemy < 1):
                        attack_on_enemy = int(input(
                            "You're moving first. 1 = weapon attack, 2 = unarmed attack, 3 = shield(Block all incoming damage)"))

                    if (attack_on_enemy == 1):
                        print("Successful Attack")

                        # Nested Elif to determine what weapon the player is using
                        if (first_player_weapon == iron_spear):

                            # Nested elif to see if enemy is grappled
                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                        elif (first_player_weapon == iron_mace):

                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                        else:

                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                    elif (attack_on_enemy == 2):
                        print("Successful Unarmed Attack")

                        if (enemy_status == 'grappled'):
                            print("The ", enemy_name,
                                  " is currently grappled, but will be released now that you've attacked", sep='')
                            enemy_hurt = unarmed * 2
                            enemy_status = 'normal'

                        else:
                            enemy_hurt = unarmed

                    elif (attack_on_enemy == 3):
                        print("Successful Block")
                        enemy_hurt = 0

                    # -----------------------------------------------------------------------------------------------------------------------------
                    # Companion's attack after player attack
                    attack_on_enemy_companion = int(input(
                        "Vax moves next. 1 = weapon attack(Vax has a sword), 2 = healing, 3 = shield(Block all incoming damage), 4 = grapple(lasts only one turn"))

                    # While loop to make the player choose 1-4 for attack_on_enemy_companion
                    while (attack_on_enemy_companion > 4 or attack_on_enemy_companion < 1):
                        attack_on_enemy_companion = int(input(
                            "Vax moves next. 1 = weapon attack(Vax has a sword), 2 = healing, 3 = shield(Block all incoming damage), 4 = grapple(lasts only one turn"))

                    if (attack_on_enemy_companion == 1):
                        print("Successful Attack")
                        enemy_hurt_companion = companion_first_weapon

                    elif (attack_on_enemy_companion == 2):
                        healing_choice = int(
                            input("who are you healing?(Type 1 to heal you and 2 to have Vax heal himself)"))

                        # While loop to make the player choose 1 or 2 for healing_choice
                        while (healing_choice > 2 or healing_choice < 1):
                            healing_choice = int(
                                input("who are you healing?(Type 1 to heal you and 2 to have Vax heal himself)"))

                        # Nested If to see who gets healed
                        if (healing_choice == 1):
                            print("Successfully Healed yourself")
                            player_hp = player_hp + companion_healing
                            print("You are healed ", player_hp, " HP.", sep="")
                            enemy_hurt_companion = 0

                        elif (healing_choice == 2):
                            print("Successfully Healed Vax")
                            companion_hp = companion_hp + companion_healing
                            print("Vax is healed ", companion_healing, " HP.", sep="")
                            enemy_hurt_companion = 0

                    elif (attack_on_enemy_companion == 3):
                        print("Successful Block")
                        enemy_hurt_companion = 0

                    elif (attack_on_enemy_companion == 4):
                        print("Successful Grapple")
                        enemy_status = 'grappled'
                        enemy_hurt_companion = 0

                # -----------------------------------------------------------------------------------------------------------------------------

                # If Vax moves first
                if who_attacks == 2:
                    attack_on_enemy_companion = int(input(
                        "Vax moves first. 1 = weapon attack(Vax has a sword), 2 = healing, 3 = shield(Block all incoming damage), 4 = grapple(lasts only one turn"))

                    # While loop to make the player choose 1-4 for attack_on_enemy_companion
                    while (attack_on_enemy_companion > 4 or attack_on_enemy_companion < 1):
                        attack_on_enemy_companion = int(input(
                            "Vax moves first. 1 = weapon attack(Vax has a sword), 2 = healing, 3 = shield(Block all incoming damage), 4 = grapple(lasts only one turn"))

                    if (attack_on_enemy_companion == 1):
                        print("Successful Attack")
                        enemy_hurt_companion = companion_first_weapon

                    elif (attack_on_enemy_companion == 2):
                        healing_choice = int(
                            input("who are you healing?(Type 1 to heal you and 2 to have Vax heal himself)"))

                        # While loop to make the player choose 1 or 2 for healing_choice
                        while (healing_choice > 2 or healing_choice < 1):
                            healing_choice = int(
                                input("who are you healing?(Type 1 to heal you and 2 to have Vax heal himself)"))

                        # Nested If to see who gets healed
                        if (healing_choice == 1):
                            print("Successfully Healed yourself")
                            player_hp = player_hp + companion_healing
                            print("You are healed ", player_hp, " HP.", sep="")
                            enemy_hurt_companion = 0

                        elif (healing_choice == 2):
                            print("Successfully Healed Vax")
                            companion_hp = companion_hp + companion_healing
                            print("Vax is healed ", companion_healing, " HP.", sep="")
                            enemy_hurt_companion = 0

                    elif (attack_on_enemy_companion == 3):
                        print("Successful Block")
                        enemy_hurt_companion = 0

                    elif (attack_on_enemy_companion == 4):
                        print("Successful Grapple")
                        enemy_status = 'grappled'
                        enemy_hurt_companion = 0

                    # -----------------------------------------------------------------------------------------------------------------------------
                    # player's attack after Vax's attack
                    attack_on_enemy = int(input(
                        "You're moving second. 1 = weapon attack, 2 = unarmed attack, 3 = shield(Block all incoming damage)"))

                    # While loop to make the player choose 1-3 for attack_on_enemy
                    while (attack_on_enemy > 3 or attack_on_enemy < 1):
                        attack_on_enemy = int(input(
                            "You're moving second. 1 = weapon attack, 2 = unarmed attack, 3 = shield(Block all incoming damage)"))

                    if (attack_on_enemy == 1):
                        print("Successful Attack")

                        # Nested Elif to determine what weapon the player is using
                        if (first_player_weapon == iron_spear):

                            # Nested elif to see if enemy is grappled
                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                        elif (first_player_weapon == iron_mace):

                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                        else:

                            if (enemy_status == 'grappled'):
                                print("The ", enemy_name,
                                      " is currently grappled, but will be released now that you've attacked", sep='')
                                enemy_hurt = first_player_weapon * 2
                                enemy_status = 'normal'

                            else:
                                enemy_hurt = first_player_weapon

                    elif (attack_on_enemy == 2):
                        print("Successful Unarmed Attack")

                        if (enemy_status == 'grappled'):
                            print("The ", enemy_name,
                                  " is currently grappled, but will be released now that you've attacked", sep='')
                            enemy_hurt = unarmed * 2
                            enemy_status = 'normal'

                        else:
                            enemy_hurt = unarmed

                    elif (attack_on_enemy == 3):
                        print("Successful Block")
                        enemy_hurt = 0

            # https: // www.w3schools.com / python / numpy / numpy_random.asp
            # Randomizing the enemy_attack value

            enemy_attack(player_hp, enemy_dmg, enemy_name, companion_hp)

        if (player_hp and companion_hp == 30):
            print("We've got this!")

        if (player_hp or companion_hp <= 15):
            print("We're not looking too good")

        enemy_hp = int(enemy_hp - (enemy_hurt + enemy_hurt_companion))

        if (enemy_hp >= 10):
            print("The ghoul doesnt look too hurt")

        print("The ", enemy_name, " is at ", enemy_hp, ".", sep='')

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print(
        "Well I can see now that you have plenty of combat experience. I've never seen someone kill two undead with such ease!")
    print(
        "This ghoul must have been an seasoned adventurer judging by the weapons on his belt. He has a spell book and a magic dagger. I'll take one and you can take the other.")

    # lightning_spell = 10
    # magic_dagger = 9

    # choosing dagger or lightning spell
    second_player_weapon_choice: str = input("Which do you want? The dagger or the spell book? (type: book or dagger)")

    # While loop to make the player choose book or dagger for second_player_weapon_choice (how to make a while loop for strings?)
    while (second_player_weapon_choice != 'book'):
        input(
            "Which do you want? The dagger or the spell book? (type: 1 for the book or 2 for the dagger)")

    # If statement to decide if the player has a spell or dagger now
    if (second_player_weapon_choice == 'book'):
        # second_player_weapon = lightning_spell
        # second_player_weapon_dmg_type == 'lighting'
        print(
            "The book has a blue cover with a lighting bolt streaking across it. Opening the book floods you with the knowledge of how to use a basic lightning spell. (10 lighting damage)")
    elif (second_player_weapon_choice == 'dagger'):
        # second_player_weapon = magic_dagger
        # second_player_weapon_dmg_type == 'poison'
        print(
            "The dagger has a green threaded handle and a quarter sized circle in the center of the blade. Touching it granted the knowledge of how to use this magic weapon. (9 poison damage)")
        print(
            "Cutting any living creature with it will instantly hurt the creature with terrible poison damage. This weapon will have no effect on undead")
    else:
        # second_player_weapon = lightning_spell
        # second_player_weapon_dmg_type == 'lighting'
        print(
            "(You get the spell then) The book has a blue cover with a lighting bolt streaking across it. Opening the book floods you with the knowledge of how to use a basic lightning spell. (10 lighting damage)")

    for player_hp in range(0, 6):
        print("We probably should heal a bit before the next fight.")

    player_hp += companion_healing

    # ghost_hp = 15
    # ghost_dmg = 5
    # ghost_name = 'ghost'
    # enemy_grapple_status = 'normal'

    # enemy_fight_magic_only(enemy_hp, player_hp, first_player_weapon, ghost_dmg, companion_hp, ghost_name, companion_healing, iron_spear, iron_mace, enemy_status, companion_first_weapon, unarmed, second_player_weapon)
    print("Congrats! You've made it to the end for now. The journey will  continue more in the future.")


# def resistance_vulnerability_immunity_check()

def enemy_attack(player_hp, enemy_dmg, enemy_name, companion_hp):
    enemy_attack_choice = randint(1, 2)

    # Deciding to see who get hits by the enemy
    if enemy_attack_choice == 1:
        player_hp = player_hp - enemy_dmg
        print("The ", enemy_name, " attacked you. You got hit with ", enemy_dmg, " damage.", sep='')
        print("You are at ", player_hp, " and Vax is at ", companion_hp, ".", sep='')

    else:
        companion_hp = companion_hp - enemy_dmg
        print("The ", enemy_name, " attacked Vax. Vax got hit with ", enemy_dmg, " damage.", sep='')
        print("You are at ", player_hp, " and Vax is at ", companion_hp, ".", sep='')

main()
