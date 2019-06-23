# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Marisa")


# The game starts here.

label start:
    play music "bgmusic.ogg" loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show marisa5:
        xalign 0.1
        yalign 1.0

    # These display lines of dialogue.

    e "Reimu and I have been friends for so long."
    hide marisa5
    show marisa
    e "She's so cute but I can't tell her that!"
    "As she began to contemplate these thoughts, she noticed a bright purple star growing larger in the distance."
    jump chapter2
    # This ends the game.

    return
