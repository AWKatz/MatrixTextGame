# This is a rework of day 3 of 100 in the Python Bootcamp with some additions
import time
import sys

def trinity_typing(words):
    words += "\n"
    for char in words:
        time.sleep(0.21)
        sys.stdout.write(char)
    time.sleep(1)



trinity_typing("Wake up, Neo...")
trinity_typing("The Matrix has you.")
trinity_typing("Follow the white rabbit.")
trinity_typing("Knock, knock, Neo.\n")

print("You're finally awake...its time for you to make a choice Neo.\n")

path = input('This is your last chance, after this there is no turning back. If you take the "blue" pill; The story ends.\n'
             'You wake up in your bed and believe whatever you want to believe. You take the "red" pill; You stay in Wonderland.\n'
             'And I show you how deep the rabbit hole goes.\n').lower()

if path == "red":
    path = input('You take the red pill and start the path of The One, just as the Oracle had hoped.\n'
                 'Do you start your "training" with Morpheus or "skip" it?\n').lower()

    if path == "training":
        path = input('The training program was successfully uploaded, you now know kung foo.\n'
                     'It\'s is time for you to meet the Oracle.\n'
                     'On your way to the meeting, you are intercepted by Agents.\n'
                     'Do you call Tank for an "exit", stand your ground and "fight" or open "fire".\n').lower()
        if path == "exit":
            print("You're beginning to believe...You live to fight another day. YOU WIN!")
        elif path == "fight":
            print("You try to fight the Agent, but you're not strong enough to survive yet...Game Over")
        elif path == "fire":
            print("You fire an entire mag and hit nothing but air...Game Over")
        else:
            print("You took too long to make a decision and in doing so, Cypher unplugged you\n"
                  "your body dies in the Matrix and your mind makes it real...Game Over")
            trinity_typing("Don\'t blame me Trinity...I\'m just the messenger...\n")
    else:
        print("You skip your training, failing to learn the skills to survive the machines...Game Over.")
else:
    print("You took the blue pill. You wake up in your bed,\n"
          "your computer terminal blank on your desk.\n"
          "You can't help but feel like you're just a sheep in a machine...Game Over")
    trinity_typing("Perhaps I was wrong about you...\n")
