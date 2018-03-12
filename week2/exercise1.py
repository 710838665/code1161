"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will define somethings.
some_words = ['what', 'does', 'this', 'line', 'do', '?']# it initialised a list with those worlds.

for word in some_words:
    print(some_words)# it initialised a list with those worlds.
    # I think this will print "what dose this line do ?'
for x in some_words:
    print(x)# x is not in those words,so it will not be printed.


print(some_words)# it initialised a list with those worlds.

if len(some_words) > 3: # I think it will define something.# it assumed a consequence.
    print('some_words contains more than 3 words') # it will print something.
print('a_number >= 3')
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
