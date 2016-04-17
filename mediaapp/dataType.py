import abc
from enum import Enum, unique

@unique
class aplicationType(Enum):
    twitter = 1
    flickr = 2
