from stat import Stat
import util


class Move(object):
    """
    Represents a single move that a character can perform during combat
    """

    name = "New Move"
    outcomes = []
    prerequisites = []


    def stat_breakdown(self):
        pass


    def format(self, *, performer="", victim=""):
        pass


    @classmethod
    def from_data(cls, data):
        move = Move()
        move.name = data['name']
        if 'outcomes' in data:
            move.outcomes = [Outcome.from_data(outcome_data) for outcome_data in data['outcomes']]
        else:
            # TODO: raise an error, all moves need at least one outcome
            pass

        if 'prerequisites' in data:
            move.prerequisites = data['prerequisites']
        return move


    def as_data(self):
        data = {
            "name": self.name,
            "prerequisites": self.prerequisites,
            "outcomes": [Outcome.as_data(outcome) for outcome in self.outcomes]
        }
        return data


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


class Outcome(object):
    name = "New Outcome"
    power = 0
    damage = []
    descriptions = []
    rate = 1


    @classmethod
    def from_data(cls, data):
        outcome = Outcome()
        outcome.name = data['name']

        if 'power' in data:
            outcome.power = data['power']

        if 'damage' in data:
             outcome.damage = data['damage']

        if 'descriptions' in data:
            outcome.descriptions = data['descriptions']
        else:
            outcome.descriptions = ["|a performs a {}!}".format(data['name'])]

        if 'rate' in data:
            outcome.rate = data['rate']
        return outcome


    def as_data(self):
        data = {
            'name' = self.name,
            'power' = self.power,
            'rate' = self.rate,
            'damage' = self.damage
        }
        return data