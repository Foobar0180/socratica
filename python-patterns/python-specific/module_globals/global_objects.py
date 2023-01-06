import os


"""
A module instantiates an object at import time and assigns
it a name in the module’s global scope. But the object does
not simply serve as data; it is not merely an integer, string,
or data structure. Instead, the object is made available
for the sake of the methods it offers — for the actions it
can perform.
"""

"""The Global Object pattern"""

# The simplest Global Objects are immutable.

escapesre = re.compile(r'[\\"]')       # email/utils.py
magic_check = re.compile('([*?[])')    # glob.py
commentclose = re.compile(r'--\s*>')   # html/parser.py
HAS_UTF8 = re.compile(b'[\x80-\xff]')  # json/encoder.py

# Compiling a regular expression as a module global is a good
# example of the more general Global Object pattern.

"""
But what about Global Objects that are mutable? They are easiest
to justify when they wrap system resources that are by their
nature also global to an operating system process. One example
in the Standard Library itself is the environ object that
gives your Python program the “environment” — the text keys
and values supplying your timezone, terminal type, so forth —
that was passed to your Python program from its parent process.
"""

os.environ['TERM'] = 'xterm'

# >>> os.environ['TERM']
# 'xterm'

# The problems with coupling distant parts of your codebase,
# and even unrelated parts of different libraries, through a
# unique global object are well known.
