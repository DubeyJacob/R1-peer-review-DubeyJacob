    #!/usr/bin/python3

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'


world = {"start":{"description":"You are at a rest stop in space",
                  "options":["You go into the tavern","You go back on your ship","You explore the planet"],
                  "results":["Tavern","Ship","Explore"]},
         "Tavern":{"description":"You are in the tavern",
                   "options":["You order a drink","You talk to the mysterious character in the corner",
                              "you leave the tavern"],
                   "results":["drink","character","start"]},
         "Ship":{"description":"You are on your ship and you take off, but the space police are after you",
                 "options":["You try to escape","You fight back","You self destruct, no one can know..."],
                 "results":["escape","fight","self_destruct"]},
         "Explore":{"description":"You come across some ancient ruins",
                    "options":["explore the ruins","go back to ship"],
                    "results":["ruins","start"]},
         "drink":{"description":"The bartender asks you a favor.",
                  "options":["You accept the offer","You decline the offer"],
                  "results":["accept","decline"]},
         "character":{"description":"The mysterious character wants to sell you some death sticks",
                      "options":["You refuse","You accept (for some reason)"],
                      "results":["Tavern","Death sticks"]},
         "escape":{"description":"You lose them in an asteroid field, but a gang of space pirates attack",
                   "options":["You attack","You surrender", "You flee"],
                   "results":["attack","surrender","flee"]},
         "fight":{"description":"You blow up the space police ship, but reinforcements are on the way",
                  "options":["You try to hide","You run away"],
                  "results":["hide","escape"]},
         "self_desctruct":{"description":"You explode",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "ruins":{"description":"You enter a find a room full of exotic materials",
                  "options":["You pick up the material","You leave it alone and go back"],
                  "results":["curse","start"]},
         "accept":{"description":"The bartender asks you to marry his daughter",
                   "options":["You accept his offer","You decline","You ask to see a picture first"],
                   "results":["marriage","frying pan","RUDE"]},
         "decline":{"description":"The bartender is angered and shoots you with his lazer cannon",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "Death Sticks":{"description":"You die... What did you think would happen?",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "attack":{"description":"You blow up the ship and escape with your lives and live happily ever after",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "surrender":{"description":"The pirates raid your ship",
                      "options":["You use the escape pods","You join their crew","You fight to the death"],
                      "results":["pods","crew","finale"]},
         "flee":{"description":"You were too hasty and hit an asteroid, your body is still floating in space to this day",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "hide":{"description":"The police find you and you are arrested. You live out the rest of your days in space prison.",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "curse":{"description":"The material turns into a giant monster",
                  "options":["expel the monster","run!"],
                  "results":["victory","yummy"]},
         "marriage":{"description":"You marry his daughter and live a long happy life.",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "frying pan":{"description":"He is angered by this response and hits you with a frying pan, you run away",
                       "results":["start"]},
         "RUDE":{"description":"He shouts at you for such a rude request and shoots you with his lazer cannon",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "pods":{"description":"you enter an escape pod eventually landing on an alien planet where you become king!",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "crew":{"description":"You join the crew, but in an unfortunate accident involving a coffee maker, the ship explodes",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "finale":{"description":"In an epic final battle, you kill the pirates, but your ship explodes",
                   "options":["Do you want to play again?","Would you like to quit?"],
                   "results":["start","quit"]},
         "victory":{"description":"The monster turns back into the material which you sell and become the richest in the world",
                    "options":["Do you want to play again?","Would you like to quit?"],
                    "results":["start","quit"]},
         "yummy":{"description":"You try to run, but the monster eats you and converts you into the exotic substance"},
         }

def show_location(current_location):
    '''Display the description of the current location, shows the options, accepts and returns user input'''
    description = current_location['description']
    options = current_location['options']
    results = current_location['results']
    print(description)
    count = 1
    for o in options:
        print('[' + str(count) + '] ' + o)
        count = count + 1
    print('[q] to quit')
    choice = input('What do you decide?')
    if choice.lower() == 'q':
        return quit()
    new_location = results[int(choice) - 1]
    return new_location

current = "start"

while current != "quit":
        current = show_location(world[current])
