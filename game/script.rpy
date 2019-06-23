# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marisa", color ="#F1C40F")
define r = Character("Reimu", color ="#7F0815")


# The game starts here.

label start:
    #play music "bgmusic.ogg" loop

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene shrinetunnel

    show reimu tear
    r "Oh goodness… I would really like to give a gift to Marisa…"
    r "Today is our anniversary of being the best friends…"
    hide reimu tear
    show reimu sweat
    r "But as usual I don’t have money to buy her anything…"
    hide reimu sweat
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    scene nightsky

    show marisa5:
        xalign 0.1
        yalign 1.0

    # These display lines of dialogue.

    m "Reimu and I have been friends for so long."
    hide marisa5
    show marisa
    m "She's so cute but I can't tell her that!"
    "As she began to contemplate these thoughts, she noticed a bright purple star growing larger in the distance."
    jump chapter2
    # This ends the game.

    return
