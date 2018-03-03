# R1-peer-review-DubeyJacob
This is a peer review project on the branching plot novel

within this program, the objective is to create an interactive, choose-your-own-story, type of novel. The player will
be given a prompt and then a series of options. Depending on the options, new prompts will appear and (if applicable) new
options. There are good endings and bad endings depending on the decisions of the player.

The program starts with a dictionary titled 'world', within world there are other dictionaries that are the various locations
as well as options within the program; Several of the locations are endings so they only have the description with no
results or options.

Next is the actual code that makes it all work. The first line is a function that is defined. show_location is the defined
function and (current_location) is the parameter. Within this parameter, I also defined the variables within the function:
description, options, and results. Next it will print the description, and the following lines will list the options as
well as printing a quit option. Then it will ask and accept a user input and depending on the input it will return the
new_location, which is the result of the option. This will send the player to the next scene. The next line tells the code
where to begin within a loop, what to do until the end. I am unable to figure out how to get it to come to a conclusion.
However at each bad conclusion, there would be the option to either restart the game, or to quit.