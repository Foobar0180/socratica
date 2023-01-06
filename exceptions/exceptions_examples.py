"""
Exceptions allow you to write code which may not work, and
then handle the successful and failed cases separately. The
four clauses in Python Exception handling are try, except,
else, and finally. When an exception occur, it causes the
current process to stop and passes it to the calling process
until it is handled. If not handled, our program will stop.
"""

# Syntax errors

# for i in range(5)
#     print('Hello world')


# Zero division error

# 1/0


# IO File not found error

# with open('x_files.txt') as xf:
#     the_truth = xf.read()

# print(the_truth)


# Type errors

# 1 + 2 + "three"

import logging
import time

# Create a logger
logging.basicConfig(
    filename="exceptions_tutorial.log",
    level=logging.DEBUG)

logger = logging.getLogger()


def read_file_timed(path):
    """
    Returns the contents of the file at 'path' and
    calculate the time required.
    """
    start_time = time.time()

    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(
            file=path,
            time=dt
        ))

data = read_file_timed("does_not_exist.mov")
