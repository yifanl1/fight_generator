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
        affects={},
        success_rate=1,
        descriptions=["$a attacks $b"],
        fail_descriptions=["$a attacks $b but misses"],
        prerequisites=[]
    ):
        super(Move, self).__init__()
        self.name = name
        self.power = power
        self.affected_stats = affected_stats
        self.success_rate = success_rate
        self.descriptions = descriptions
        self.fail_descriptions = fail_descriptions
        self.prerequisites = prerequisites

    def stat_breakdown(self):
        return {
            stat_name: move.power * stat.modifer * util.random(low=0.8, high=1.2)
            for (stat_name, stat) in move.affected_stats.items()}


    def format(self, *, performer="", victim=""):
        descriptions = self.descriptions if self.does_succeed() else self.fail_descriptions
        return util.choice(descriptions).replace("$a", performer).replace("$b", victim)


    def does_succeed(self):
        return True


    # @classmethod
    # def validate_prerequisite(prerequisite):
    #     """
    #     checks if prerequisite is of a valid format

    #     a prerequisite must be one of:
    #      [my OR their] _stat >= X
    #      [my OR their] _stat1 >= [my OR their] _stat2
    #      [my OR their] _stat = X
    #      [my OR their] _stat1 = [my OR their] _stat2
    #      [my OR their] _stat <= X
    #      [my OR their] _stat1 <= [my OR their] _stat2
    #      [my OR their] recent move = <_move_name, ...>
    #      [my OR their] last move = <_move_name, ...>
    #      X uses total
    #     """
    #     return True


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
        affects={},
        success_rate=1,
        descriptions=["$a attacks $b"],
        fail_descriptions=["$a attacks $b but misses"],
        counter_to=[]
    ):
        prerequisites = ["last move was {}".format(move.name) for move in counter_to]
        super(CounterAttack, self).__init__(
            name=name,
            power=power,
            affects=affects,
            success_rate=success_rate,
            descriptions=descriptions,
            fail_descriptions=fail_descriptions,
            prerequisites=prerequisites)


class SelfMove(Move):
    """
    Represents a move that only affects the performing character
    """
    def __init__(
        self,
        *,
        name="New Move",
        power=0,
        affected_stats={},
        success_rate=1,
        descriptions=["$a blocks"],
        fail_descriptions=["$a raises a gaurd but is too weak!"],
        prerequisites=[]
    ):
        super(SelfMove, self).__init__(
            name=name,
            power=power,
            affects=affects,
            success_rate=success_rate,
            descriptions=descriptions,
            fail_descriptions=fail_descriptions,
            prerequisites=prerequisites)


    def format(self, *, performer=""):
        description = util.choice(self.descriptions)
        return description.replace("$a", performer)