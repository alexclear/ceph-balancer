"""
Defines various Enum types used throughout the application.
"""

from enum import Enum


class PGState(Enum):
    """
    what pg state set to use
    """
    UP = 1  # use the future planned pg assignments
    ACTING = 2  # use the current data-serving pg assignments


class OSDSizeMethod(Enum):
    """
    how to determine the OSD size
    """
    CRUSH = 1  # use the crush size
    DEVICE = 2  # use the device size
    WEIGHTED = 3  # weighted device size


class OSDUsedMethod(Enum):
    """
    how to determine the OSD usage size during simulation.
    we don't know what the OSD will actually do for movement and cleanup,
    so we have options to choose from how to estimate the new usage.
    """
    # adjusting the reported osd usage report by adding fractions of currently-in-move pg sizes.
    # more accurate but doesn't account pending data deletion.
    DELTA = 1
    # estimate the usage by summing up all pg shardsizes,
    # doesn't account PG metadata.
    SHARDSUM = 2


class OSDFromChoiceMethod(Enum):
    """
    how to choose a osd to move data from
    """
    FULLEST = 1  # use the fullest osd
    LIMITING = 2  # use devices limiting the pool available space
    ALTERNATE = 3 # alternate between limiting and fullest devices


class PGChoiceMethod(Enum):
    """
    how to select a pg for movement
    """
    # take the largest pg from the best source osd
    LARGEST = 1

    # take the median pg size from the best source osd
    MEDIAN = 2

    # determine the best pg size automatically by looking at the ideal space needed on the emptiest osd.
    AUTO = 3


class PoolFreeMethod(Enum):
    """
    how available pool space is predicted
    """
    # use device utilization and osd weight distribution
    WEIGHT = 0
    # determine the limiting osd device and exact placement group availability
    LIMITING = 1 