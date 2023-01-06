import datetime
import os


"""
Every Python module is a separate namespace. The Module Global
pattern specifically refers to normal object instances that
are given names at the global level of a module.
"""

"""The Constant pattern

These are “constants” only in the sense that the objects themselves
are immutable. The names can still be reassigned.

A constant can also capture the result of a conditional to avoid
re-evaluating it each time the value is needed — as long, of course,
as the condition won’t be changing while the program is running."""

January = 1                   # calendar.py
WARNING = 30                  # logging.py
MAX_INTERPOLATION_DEPTH = 10  # configparser.py
SSL_HANDSHAKE_TIMEOUT = 60.0  # asyncio.constants.py
TICK = "'"                    # email.utils.py
CRLF = "\r\n"                 # smtplib.py

# In addition to integers, floats, and strings, constants also
# include immutable containers like tuples and frozen sets.

all_errors = (Error, OSError, EOFError)  # ftplib.py
bytes_types = (bytes, bytearray)         # pickle.py
DIGITS = frozenset("0123456789")         # sre_parse.py

# More specialized immutable data types also serve as constants.

_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)  # datetime

"""
Sometimes constants are introduced for efficiency, to avoid
recomputing a value every time code is called.
"""

# zipfile.py
ZIP_FILECOUNT_LIMIT = (1 << 16) - 1

""" Dunder constants

A special case of constants defined at a module’s global
level are “dunder” constants whose names start and end with
double underscores.

Several Module Global dunder constants are set by the language
itself. For the official list, look for the “Modules”
subheading in the Python Reference’s section on the standard
type hierarchy.

https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
"""

here = os.path.dirname(__file__)
