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


    @classmethod
    def parse(line):
        """Read a line and converts it into a move object

        A line should be structured as such:
        (_name) (_description) _power _accuracy <(_stat, _stat_modifier), ...> <(_prerequisite), ...>

        description includes the keywords "$a", "$b"
        """
        name, rest = util.read_in_bracket(line.strip())
        description, rest = util.read_in_bracket(rest.strip())
        power, accuracy, rest = rest.split(" ", 2)
        stat_breakdown_list = util.read_in_bracket(rest.strip(), start_bracket="<")
        prerequisite_list = util.read_in_bracket(rest.strip(), start_bracket="<")
        return Move()


    @classmethod
    def validate_prerequisite(prerequisite):
        """
        checks if prerequisite is of a valid format

        a prerequisite must be one of:
         [my OR their] _stat >= X
         [my OR their] _stat1 >= [my OR their] _stat2
         [my OR their] _stat = X
         [my OR their] _stat1 = [my OR their] _stat2
         [my OR their] _stat <= X
         [my OR their] _stat1 <= [my OR their] _stat2
         [my OR their] recent move = <_move_name, ...>
         [my OR their] last move = <_move_name, ...>
         X uses total
        """
        return True


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
