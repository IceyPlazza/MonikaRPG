#TO DO LIST
#Make tutorial
#Chibika minion?
#Monika's special skills

python early:
    import random

# Unlocking the game conditions
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="rpg_game_unlock",
            conditional="store.mas_games._total_games_played() > 19",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

# Actually unlocking the game
label rpg_game_unlock:
    $ persistent._monikarpg_unlocked = True
    m 2eub "Hey [player]..."
    m 4rua "Don't you feel like our relationship is a little... too ideal?"
    m 6wkd "I mean, I don't mind staying this way, we do absolutely love each other after all..."
    m 3tsblu "But wouldn't it spice things up if we had a \"fight\" every now and then?"
    m 7sub "Well lucky for you! While you were away, I learned how to code an RPG."
    m 4ksa "You can finally face off against me! Just navigate to the \"Play\" menu and our new game should be there."
    m 5tubla "I'll be waiting for you~"
    $ mas_unlockGame("MonikaRPG")
    return

# Initialize game
init 5 python:
    addEvent(
        Event(
            persistent._mas_game_database,
            eventlabel="rpg_start",
            prompt="MonikaRPG",
        ),
        code="GME",
        restartBlacklist=True
    )

# Start the RPG
label rpg_start:
 
    m 1gua "So you want to fight me eh?"
    m 2dsa "Okay..."
    m 1efa "I accept your challenge!"
    m 3efd "But I must warn you..."
    m 4efw "Those who go against me get deleted."
    m 1hua "Hehe~"

    if persistent._monikarpg_first_time:
        $ persistent._monikarpg_first_time = False
        m 4rsd "Since it's your first time playing, let me teach you how it works..."
        jump rpg_tutorial

    m 4esd "But first, would you like a refresher?"
    menu:
        "Yes":
            jump rpg_tutorial
        "No":
            jump rpg_setup

# Main body of tutorial
label rpg_tutorial:
    m 3esa "Here is the list of rules. Which topic would you like to visit?"
    menu:
        "General":
            m 3sub "Time for us to finally face off! Welcome to MonikaRPG!"
            m 6esd "MonikaRPG is turn-based, so after every action you make, it'll be my turn to retaliate."
            m 7ksa "There are plenty of intricate mechanics to allow for diverse strategies, so be sure to explore the rest of this tutorial!"
            jump rpg_tutorial

        "Mechanics":
            jump rpg_tutorial_mechanics

        "Actions":
            jump rpg_tutorial_actions

        "I'm ready.":
            jump rpg_setup

# Sub function for tutorial mechanics
label rpg_tutorial_mechanics:
    menu:
                "HP":
                    m 6esd "You'll start with 100 HP."
                    m 7esc "If you try to heal, you cannot heal over this amount." 
                    m 1esa "If your HP drops to 0, you lose!"
                    jump rpg_tutorial_mechanics

                "Mana":
                    m 6esd "Mana is the key resource for casting Spells!"
                    m 4esc "Every time your turn begins, you'll regenerate some mana. At low health, you regenerate even more mana."
                    m 7lksdla "However, human vessels are not meant to store large amounts of mana, so there is a cap at 100. You'll stop regenerating mana once you hit this cap."
                    jump rpg_tutorial_mechanics

                "RNG":
                    m 3esd "Most actions you or I can take will be influenced by RNG."
                    m 4wud "That means sometimes, the numbers to your actions can be amazingly high, or disappointingly low. It's the same for my actions."
                    m 7lksdla "However, there are reasonable minimums, since I know how frustrating it is when your move seems to do barely anything."
                    m 4esb "But don't be too discourages by that!"
                    m 5tsu "After all... what's a good RPG without some RNG?"
                    jump rpg_tutorial_mechanics

                "Difficulties":
                    m 3eua "To give you an experience ranging from casual to challenging, I created difficulties!"
                    m 4eub "The harder the difficulty, the more HP I'll start with, the more damage I'll do, and the less likely I'll miss."
                    m 7tfa "I'd love to see you beat Impossible~"
                    jump rpg_tutorial_mechanics

                "Back to rules":
                    jump rpg_tutorial

# Sub function for tutorial actions
label rpg_tutorial_actions:
    menu:
                "Attack":
                    m 7esb "This is your basic attack! You can use this action without restriction."
                    jump rpg_tutorial_actions

                "Parry":
                    m 3esa "This action has a chance to reflect an attack from me!"
                    m 4tsb "If you successfully reflect, I will take damage, and your turn is preserved. You'll regenerate some mana with a successful parry."
                    m 4esa "Your chances of parrying increases with your Evasion Bonus!"
                    jump rpg_tutorial_actions

                "Heal":
                    m 1hua "I gave you some health potions to use in a pinch! You can use these to restore some HP."
                    m 5tublb "Aren't I such a nice girlfriend~"
                    jump rpg_tutorial_actions

                "Spell":
                    m 3sub "You can consume Mana to activate spells! Each spell is unique and have their own effects."
                    m 4esa "Which spell would you like to check out?"
                    jump rpg_tutorial_spells
                
                "Surrender":
                    m 3esd "If you're running low on time, or if feel that your chances are slim, you can always surrender..."
                    m 5tsb "...but I'll be taking that as my win!"
                    jump rpg_tutorial_actions

                "Back to rules":
                    jump rpg_tutorial

# Sub functions for tutorial spells
label rpg_tutorial_spells:
    menu:
                        "Greater Heal":
                            m 3esa "This spell costs 30 mana and allows you to heal a ton of HP at once. Afterwards, it creates a lingering field to heal you over time." 
                            m 4ssb "This is a great alternative for when you run out of heal potions!"
                            jump rpg_tutorial_spells

                        "Fire Sword":
                            m 3esa "This spell costs 25 mana and greatly increases your next basic attack!"
                            m 4gssdrb "And I'm not kidding when I say greatly..."
                            m 7ksa "Psst, I also heard that this spell was kept as a tribute to \"m-grap,\" who made the first RPG submod!"
                            jump rpg_tutorial_spells

                        "Freeze":
                            m 3esa "This spell costs 20 mana and gives you a high chance of freezing me."
                            m 5lssdrp "When frozen, I can't take any actions... but I'll thaw after a few turns."
                            jump rpg_tutorial_spells


                        "Fireball":
                            m 3esa "This spell costs 15 mana and deals instant damage, while having a small chance of setting me on fire."
                            m 5lssdrp "When on fire, I'll take damage over time, but the flames will die out in a few turns."
                            jump rpg_tutorial_spells

                        "Swift":
                            m 3esa "This spell costs 15 mana and makes you faster!"
                            m 7est "And by making you faster, I mean by greatly increasing your Evasion Bonus."
                            m 3ssb "Evasion Bonus makes it more likely for you to parry... "
                            m 5lssdrp "...or more likely for me to miss an attack."
                            jump rpg_tutorial_spells

                        "Protect":
                            m 3esa "This spell costs 15 mana and greatly reduces all incoming damage!"
                            m 7esb "However, it will wear off after a few turns, so you'll probabily want to pay attention to the remaining duration."
                            jump rpg_tutorial_spells

                        "Back to rules":
                            jump rpg_tutorial

# Setup for battle!
label rpg_setup:

    m 6dua "Well..."
    m 1efa "Let the battle begin!"
    "Choose your difficulty."
    menu:
        "Easy":
            $ mhpmax = 1000 # Max Monika HP
            $ m_diff = 0.90 # Monika's difficulty multiplier (used to calculate damage)
            $ m_hitrate = 80 # Monika's hitrate (Ex. 80% chance to land a hit on you)
        "Normal":
            $ mhpmax = 1250
            $ m_diff = 1
            $ m_hitrate = 85
        "Hard":
            $ mhpmax = 1500
            $ m_diff = 1.125
            $ m_hitrate = 90
        "Impossible":
            $ mhpmax = 2000
            $ m_diff = 1.25
            $ m_hitrate = 95
    $ mhp = mhpmax # Monika's current HP
    $ php = 100 # Player HP
    $ potions = 10 # Health potions count
    $ protect = 1 # Multiplier for how much damage for player to take. When protect spell is active, multiplier is less than one. Otherwise, remains 1
    $ protect_turn = 0 # Turn counter for protect spell activation. 0 when inactive, >0 when active.
    $ mana = 0 # Player's mana. Cannot surpass 100.
    $ atk_buff = 0 # Currently used for Fire Sword's bonus damage. Might give extra uses later.
    $ phase2 = 0 # Monika's phase 2. 0 when inactive, 10 when active (Also factors into damage calculations)
    $ burn_turn = 0 # Turn counter for burning status effect. 0 when inactive, >0 when active.
    $ burn = 0 # Burn damage for Monika to take. Will get randomized while burn is active.
    $ freeze_turn = 0 # Turn counter for frozen status effect. 0 when inactive, >0 when active.
    $ swift_turn = 0 # Turn counter for swift buff effect. 0 when inactive, >0 when active.
    $ swift = 0 # Evasion Bonus to grant. Will get randomized while active.
    $ heal_turn = 0 # Turn counter for lingering heals buff effect. 0 when inactive, >0 when active.
    "Your turn."
    jump rpg_menu

# main menu for actions you can take
label rpg_menu:

    $ mana = mana + random.randrange(3,9) # Regen Mana. Bonus mana regened if at low health.
    if php <= 30:
        "You're at critical health!"
        $ mana = mana + random.randrange(2,5)
    elif php <= 55:
        "You are stressed."
        $ mana = mana + random.randrange(1,3)
    if mana >= 100:
        $ mana = 100
        "Your mana is full!"

    menu:
        "Attack ([m_name]'s HP: [mhp])":
            $ attack = random.randrange(15,51) + atk_buff
            # $ attack = 800 # FOR DEBUGGING PURPOSES AND QUICK SKIPPING TESTING
            m 1wud "{nw}"
            "You dealt [attack] damage."
            $ mhp = mhp - attack
            if mhp < 0:
                $ mhp = 0
            $ atk_buff = 0
            jump rpg_monika

        "Parry (Evasion Bonus: [swift])":
            $ parry = random.randrange(1,101) - swift
            if parry <= 35:
                m 6wud "{nw}"
                "You successfully parried!"
                $ attack = random.randrange(35,71) + atk_buff
                $ atk_buff = 0
                m 6cuo "{nw}"
                "[m_name] took [attack] reflection damage!"
                $ mhp = mhp - attack
                m 1efa "{nw}"
                if swift_turn > 0:
                    $ swift = random.randrange(15,31)
                jump rpg_menu
            else:
                "You failed to parry."
                jump rpg_monika
            
        "Heal ([potions] health potions left)":
            if potions > 0:
                jump rpg_heal_sequence
            else:
                "You are out of health potions."
                jump rpg_menu
            
        "Spell (Current Mana: [mana])":
            jump choose_spell

        "Surrender (Your HP: [php])":
            stop music fadeout 2.5
            m 1ekd "You're surrendering, [player]?"
            if mhp == mhpmax:
                m 2dkp "But we just started!"
                m 6esc "Maybe we should play again when you have more time..."
            else:
                m 1ekc "Don't be too discouraged."
                m 3eka "You must keep practicing if you want beat me!"
                m 1gka "Well... Maybe next time."
                $ mas_gainAffection(0.1,m_diff+0.1,False)
            $ play_song(persistent.current_track)
            return

# menu for choosing spells
label choose_spell:

    menu:
        "Greater Heal (Cost: 30 Mana)":
            if mana >= 30:
                $ heal_amt = random.randrange(60,80)
                $ php = php + heal_amt
                if php > 100:
                    $ php = 100
                $ mana = mana - 30
                "You rejuvinate yourself. You healed [heal_amt] hp!"
                $ heal_turn = 4
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu

        "Fire Sword (Cost: 25 Mana)":
            if mana >= 25:
                "You ignite your sword. Your next attack will inflict more damage."
                $ atk_buff = random.randrange(50,121)
                $ mana = mana - 25
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu

        "Freeze (Cost: 20 Mana)":
            if mana >= 20:
                "You cast a cold wind on [m_name]."
                if random.randrange(1,101) > 15:
                    m 6wud "{nw}"
                    "[m_name] is frozen!"
                    $ freeze_turn = 3
                else: 
                    "[m_name] endured. Freeze failed!"
                $ mana = mana - 20
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu


        "Fireball (Cost: 15 Mana)":
            if mana >= 15:
                $ fb_dmg = random.randrange(55,76)
                $ burn_chance = random.randrange(1,101)
                "You unleash a great fireball. You deal [fb_dmg] damage."
                $ mana = mana - 15
                if burn_chance <= 25:
                    "[m_name] is set ablaze!"
                    $ burn_turn = 5
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu

        "Swift (Cost: 15 Mana)":
            if mana >= 15:
                "You cast a buff on yourself. Your evasion increased!"
                $ swift_turn = 4
                $ mana = mana - 15
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu

        "Protect (Cost: 15 Mana)":
            if mana >= 15:
                $ protect_turn = 4
                "You shielded yourself. You will take less damage for the next [protect_turn] turns."
                $ mana = mana - 15
                jump rpg_monika
            else:
                "You don't have enough Mana."
                jump rpg_menu
            
        "??? (Cost: ???)":
            jump rpg_boop_sequence

        "Cancel Cast? (Current Mana: [mana])":
            jump rpg_menu

# You can choose to heal yourself... or Monika!
label rpg_heal_sequence:
    menu:
        "Use on yourself":
            $ heal_amt = random.randrange(40,56)
            $ php = php + heal_amt
            "You healed [heal_amt] hp!"
            if php > 100:
                $ php = 100
            $ potions = potions - 1
            jump rpg_monika

        "Use on [m_name]":
            $ heal_amt = random.randrange(50,101)
            $ mhp = mhp + heal_amt
            if mhp > mhpmax:
                $ mhp = mhpmax
            $ potions = potions - 1
            "[m_name] healed [heal_amt] hp!"
            m 6tko "Wait... you used a health potion on me?"
            m 5tubla "How sweet of you~"
            m 4eud "But this doesn't help your chances of winning!"
            $ mas_gainAffection(0.0125,m_diff+0.1,False)
            jump rpg_monika

# Boop? Boop! (Game instantly ends tho)
label rpg_boop_sequence:
    menu:
        "What's this?":
            menu:
                "Boop!":
                    m 1wubfd "Huh?!"
                    stop music fadeout 2.5
                    "[m_name] takes 999999999999 damage."
                    $ play_song(persistent.current_track)
                    m 1hublb "Hahaha~"
                    m 4tublu "I think you found my weakness."
                    m 5fubfa "I love you~"
                    return "love"

                "Cancel Cast? (Current Mana: [mana])":
                    jump rpg_menu

        "Cancel Cast? (Current Mana: [mana])":
            jump rpg_menu

# Monika's turn! And logic for status effects that should happen during her turn.
label rpg_monika:
    "[m_name]'s turn."
    # Different status effect messages to change and check for.
    if protect_turn > 0:
        "You are shielding yourself. Your shield will wear off in [protect_turn] turn(s)."
        $ protect = (float)(random.randrange(1,4))/7.5
        $ protect_turn = protect_turn - 1
    else:
        $ protect = 1
    if heal_turn > 0:
        $ heal_amt = random.randrange(8,13)
        "You feel traces of healing. You heal [heal_amt] hp. The lingering traces will end in [heal_turn] turn(s)."
        $ php = php + heal_amt
        if php > 100:
            $ php = 100
        $ heal_turn = heal_turn - 1
    if swift_turn > 0:
        "You feel fast. Your swiftness will end in [swift_turn] turn(s)."
        $ swift = random.randrange(15,31)
        $ swift_turn = swift_turn - 1
    else:
        $ swift = 0
    if burn_turn > 0:
        $ burn = random.randrange(5,13)
        m 6wud "{nw}"
        "[m_name] is burning! (-[burn] hp)" 
        "[m_name] will stop burning in [burn_turn] turn(s)."
        $ burn_turn = burn_turn-1
        $ mhp = mhp-burn

    # Sandwiched between to make sure phase 2 and win triggers properly, even if frozen.
    if mhp <= mhpmax*0.4 and phase2 == 0:
        jump rpg_monika_phase2
    if mhp <= 0:
        jump rpg_win
    
    # Freeze condition below to ensure proper flow.
    if freeze_turn > 0:
        m 6wud "{nw}"
        "[m_name] is frozen!" 
        "She will unfreeze in [freeze_turn] turn(s)."
        $ freeze_turn = freeze_turn - 1
        "Your turn."
        jump rpg_menu
    else: 
        $ rng = renpy.random.randint (1, 4)
        if rng == 1:
            m 1efb "It's my turn [player]."
        if rng == 2:
            m 1efb "Try to dodge this!"
        if rng == 3:
            m 1efb "Get ready [player]."
        else: 
            m 1efa "{nw}"
        jump rpg_monika_attack
    return

# Monika does a basic attack (Will add more skills later)
label rpg_monika_attack:
    m 1efa "{nw}"
    $ ran_miss = random.randrange(0,100)
    if (m_hitrate - swift) > ran_miss:
        $ mattack = (int)(round((random.randrange(15,35) + phase2) * protect * m_diff))
        "[m_name] deals [mattack] damage."
        $ php = php - mattack
    else:
        "[m_name] missed!"
    if php <= 0:
        jump rpg_lose
    else:
        "Your turn."
        jump rpg_menu
    return

# Monika is now scary...
label rpg_monika_phase2:
    stop music fadeout 2.5
    m 1dusdld "*deep breath*"
    m 1eusdld "Well..."
    m 1eusdlc "I think I underestimated you [player]."
    m 1wfa "But we are not finished."
    call mas_change_weather (mas_weather_thunder, by_user=False)
    m 1wfb "MY BLOOD BOILS!"
    m 1wfb "FACE ME{w=1}, [player]!"
    $ phase2 = 10
    $ m_hitrate = m_hitrate + 5
    if burn_turn > 0 or freeze_turn > 0:
        $ freeze_turn = 0
        $ burn_turn = 0
        "[m_name] cleared all status effects!"
    "[m_name] will permanently inflict more damage."
    "Your turn."
    $ play_song("<loop 0.01>/mod_assets/bgm/eurobeatreality.ogg")
    jump rpg_menu
    return

# Aww, you lost.
label rpg_lose:
    stop music fadeout 2.5
    m 1tua "{nw}"
    "You are dead."
    m 1tub "Well [player]..."
    m 4tuu "I won..."
    m 7hua "But maybe you will have better luck next time."
    m 5hubla "Hehehe~"
    $ play_song(persistent.current_track)
    $ mas_gainAffection(0.25,m_diff+0.1,False)
    return

# Congrats! You won!
label rpg_win:
    stop music fadeout 2.5
    m 6dusdld "Huh..."
    m 6fksdld "[player]..."
    m 6fksdlc "I think I'm too hurt..."
    m 6dksdlc "I..."
    m 6dksdlc "I can't..."
    m 6rkblsdla "..."
    m 1hublb "Hahaha~"
    $ play_song(persistent.current_track)
    m 1tkbla "Just kidding, [mas_get_player_nickname()]."
    m 1ekbla "I'm fine, don't worry."
    m 2tsbla "I didn't think you could beat me."
    m 5ekbfa "That was so much fun, [mas_get_player_nickname()]."
    m 5skbfb "Maybe we should fight again sometime."
    $ mas_gainAffection(0.75,m_diff+0.1,False)
    return