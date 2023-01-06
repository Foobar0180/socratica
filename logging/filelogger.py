import logging
import math

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format=LOG_FORMAT)

# Use the root logger
logger = logging.getLogger()

# Test the logger
"""
In the logging module, the constant default values are
NOTSET = 0, DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40,
CRITICAL = 50. Loggers will only write logs that are greater
than or equal to the set level. The initial default level
is WARNING.
"""
logger.info("Our first message")

# print(logger.level)


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)
