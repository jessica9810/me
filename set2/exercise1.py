"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]
#I think this will print what, does, this, line, do, ?
for word in some_words:
    print(word) #it printed each word in the some_words list on a separate line
#I think this will print what, does, this, line, do, ?
for x in some_words:
    print(x) #it printed each element in the some_words list on a separate line
#I think this will print what, does, this, line, do, ?
print(some_words) #it printed the entire some_words list
#If the length of some_words is greater than 3, print the message
if len(some_words) > 3:
    print("some_words contains more than 3 words") #it printed message which the length of some_words is greater than 3

#i think it will print platform uname
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #it printed the information about the current system


usefulFunction()
