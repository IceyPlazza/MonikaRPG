# Note: I tried using the usual
# "some text"
# $ _history_list.pop()
# menu:
#     "more text"
#     choice1:
#     choiceN:
# but the textbox still sometimes fade out, so I've been using 'extend ""' as a getaround that works.

# Main body of tutorial
label rpg_tutorial:

    m 3esa "Here is the list of rules. Which topic would you like to visit?"
    menu:
        extend ""
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

    m 3esa "Which mechanic would you like to learn more about?"
    menu:
        extend ""
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
    m 3esa "Which action would you like to learn more about?"
    menu:
        extend ""
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
            jump rpg_tutorial_spells
                
        "Surrender":
            m 3esd "If you're running low on time, or if feel that your chances are slim, you can always surrender..."
            m 5tsb "...but I'll be taking that as my win!"
            jump rpg_tutorial_actions

        "Back to rules":
            jump rpg_tutorial

# Sub functions for tutorial spells
label rpg_tutorial_spells:
    m 4esa "Which spell would you like to check out?"
    menu:
        extend ""
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

        "Poison Mist":
            m 3esa "This spell costs 15 mana and applies poison, dealing damage over time."
            m 4nub "But beware, there is a small chance that my immune system is strong enough to resist!"
            jump rpg_tutorial_spells

        "Swift":
            m 3esa "This spell costs 15 mana and makes you faster!"
            m 7est "And by making you faster, I mean by greatly increasing your Evasion Bonus."
            m 3ssb "Evasion Bonus makes it more likely for you to parry... "
            m 5lssdrp "...or more likely for me to miss an attack."
            m 7eub "While Swift is active, your Evasion Bonus will decrease with each successful parry. However, at the start of a new turn, your Evasion Bonus will be refreshed."
            jump rpg_tutorial_spells

        "Protect":
            m 3esa "This spell costs 15 mana and greatly reduces all incoming damage!"
            m 7esb "However, it will wear off after a few turns, so you'll probably want to pay attention to the remaining duration."
            jump rpg_tutorial_spells

        "Back to rules":
            jump rpg_tutorial