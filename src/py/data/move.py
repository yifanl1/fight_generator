from stat import Stat

class Move(object):
    """
    Represents a single move that a character can perform during combat
    """
    def __init__(self,
                 name="New Move",
                 affects_stats={},
                 chance_to_succeed=1,
                 description="(1) attacks (2)",
                 prerequisites=[]):
        super(Move, self).__init__()
        self.name = name
        self.affects_stats = affects_stats
        self.chance_to_succeed = chance_to_succeed
        self.description = description
        self.prerequisites = prerequisites


class CounterAttack(Move):
    """
    Represents a single counterattack a character can perform after a certain move fails
    counter_to is a list of the moves that are countered by this move
    """
    def __init__(self,
                 name="New Move",
                 affects_stats={},
                 chance_to_succeed=1,
                 description="(1) attacks (2)",
                 counter_to=[]):
        prerequisites = ["LAST MOVE WAS {}".format(move.name) for move in counter_to]
        super(CounterAttack, self).__init__(name, affects_stats, chance_to_succeed, description, prerequisites)
