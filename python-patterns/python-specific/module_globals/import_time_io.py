"""
The worst Global Objects are those that perform file or
network I/O at import time. They not only impose the
cost of that I/O on every library, script, and test that
need the module, but expose them to failure if a file or
network is not available.

For all of these reasons, it’s best for your global objects
to wait until they’re first called before opening files and
creating sockets — because it’s at the moment of that first
call that the library knows the main program is now up and
running, and knows that its services are in fact definitely
needed in this particular run of the program.
"""
