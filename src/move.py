from stat import Stat
import util


class Move(object):
    """
    Represents a single move that a character can perform during combat
    """
    def __init__(
        self,
        *,
        name="New Move",
        power=0,
        affected_stats={},
        chance_to_succeed=1,
        description="$a attacks $b",
        prerequisites=[]
    ):
        super(Move, self).__init__()
        self.name = name
        self.power = power
        self.affected_stats = affected_stats
        self.chance_to_succeed = chance_to_succeed
        self.description = description
        self.prerequisites = prerequisites

    def stat_breakdown(self):
        return {
            stat_name: move.power * stat.modifer * util.random(low=0.8, high=1.2)
            for (stat_name, stat) in move.affected_stats.items()}


    def format(self, *, performer="", victim=""):
        return self.description.replace("$a", performer).replace("$b", victim)


class CounterAttack(Move):
    """
    Represents a single counterattack a character can perform after a certain move fails
    counter_to is a list of the moves that are countered by this move
    """
    def __init__(
        self,
        *,
        name="New Move",
        power=0,
        affected_stats={},
        chance_to_succeed=1,
        description="(1) attacks (2)",
        counter_to=[]
    ):
        prerequisites = ["LAST MOVE WAS {}".format(move.name) for move in counter_to]
        super(CounterAttack, self).__init__(name, affected_stats, chance_to_succeed, description, prerequisites)
