from move import Move
from stat import Stat

class Character(object):
    """
    Simulates a single fighter character
    Every character can have some set of nicknames to pull from
    Every character has certain base stats
    Every character can have their own pool of special moves

    """
    def __init__(self, name="New Character", nicknames=[], base_stats=[], special_moves=[]):
        super(Character, self).__init__()
        self.name = name
        self.nicknames = nicknames
        self.base_stats = base_stats
        self.special_moves = special_moves