# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marisa", color ="#F1C40F")
define r = Character("Reimu", color ="#7F0815")


# The game starts here.

label start:
    play music "bgmusic.ogg" loop

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
    show reimu mad
    r "Ahhhh what should I do?"
    hide reimu mad
    show yellowstone:
        yalign 0.7
        xalign 0.5
    "As she continues walking she notices there’s something that shines on the ground"
    show reimu shock at left
    "She gets closer to it and realizes that there’s is a shining rock, as if it was a magic rock"
    hide reimu shock
    show reimu happy at left
    r "Oh… This is so precious! Marisa likes to collect things so I’m sure she will like this!"
    scene shrinetunnel
    show rumia dark
    "As Reimu dissapeared long into the night, a dark figure descended and let out a disturbing echoing laughter."

    scene library
    show marisa5 at right
    "Marisa was back in the library reading some new books she borrowed from Patchouli. On the table were some strange magical reagants and a bracelet."
    m " Ah… I’m so tired, but at least I’m finished with this incantation. Now it’s time to re-..."
    show reimu happy at left
    r " Marisaaa! What are you doing?"
    hide marisa5
    show marisa6 at right
    m "Kyaaaa! What the…!!! "
    m " Reimu? What you’re doing here?!"
    r "I asked you a question, fufu~"
    hide marisa6
    show marisa at right
    m "It’s n-none of your business... "
    hide reimu happy
    show reimu smile at left
    r "Oh, come on! Is there something you’re hiding to your best friend?"
    hide marisa
    show marisa grin at right
    m "Hahaha, is not like I’m working on something for y-..."
    hide reimu smile
    show reimu shock at left
    r "What…?"
    hide marisa grin
    show marisa sweat at right
    m "N.... Nothing!"
    hide reimu shock
    show reimu smile at left
    r "Uh…? Marisa? What’s that thing you’re hiding in your hands?"
    m " EH?!!"
    "She puts her hands behind her back to hide the bracelet she has."
    m "I have nothing!"
    r "Are you sure…?"
    scene library
    "Reimu starts to walk towards Marisa. Marisa walks without looking back and does not notice that there is a protruding edge on the floor that makes them fall on top of each other."
    "Marisa and Reimu's cheeks turn bright red as they both get up."
    show marisa sweat at right
    m "Look... Reimu... ummm...."
    "She let out a deep sigh, closed her eyes, took a deep breath and continued."
    m "We.. have been friends for such a long time... I..."
    "Marisa hesitated a moment, wondering if now was the time was right. Deciding to summon her inner strength she looked into Reimu's eyes"
    m "I... think I may be falling for you.."
    "Marisa reached her hands out to Reimu, handing her a bracelt with a 6 pointed star, in the middle of which was a circular yin yang."
    show reimu shock at left
    r "R.... really.. ?"
    "Marisa nodded her head, looking away, her cheeks now as red as a tomato."
    hide reimu shock
    show reimu happy at left
    "Reimu took the bracelet, placing it on her wrist then tackling Marisa down to the ground, straddlng her lap."
    hide marisa sweat
    show marisa happy at right
    r "I thought I was the only one! I have been feeling the same way. Thank you so much for this."
    show yellowstone:
        yalign 0.7
        xalign 0.2

    "Reimu admired the bracelet on her wrist. She then reached into her pocket and took out a glowing yellow stone."
    "The stone radiated bright in the room, light pulsating back and forth from it."
    hide marisa happy
    show marisa grin at right
    m "Oh.ho... What's this?"
    hide yellowstone
    show yellowstone:
        yalign 0.7
        xalign 0.7
    "Marisa reached out her hands to take the stone. As she did, a black cloud started oozing out from within."
    show tbc:
        xalign 0.8
        yalign 0.7
    "Stay tuned for the next episode."

    #jump chapter2

    # This ends the game.

    return
