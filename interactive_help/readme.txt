> python 
>>> dir() ## short for directory
>>> dir(__builtins__) ## pass in the name of a module - lists entire contents 
>>> help(pow) ## call help and pass the name of the function e.g. pow

>>> help('modules') ## to see a list of all available modules

## To see the contents of a module, you first need to import it

>>> import math
>>> dir() ## math module now appears

>>> help(math.radians) ## you must specify the path to the function. If you call
help(radians), you will get back a Trackback error - this is because the radians
function lives inside the math module

