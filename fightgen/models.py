"""
All models to be used by fightgen
"""

from . import util


class Fight():
    """
    Models a single instance of a fight
    """

    fighters = []
    _fighter_states = []
    ruleset = None


    def choose_fighters(self, fighters):
        pass


    def run(self):
        """
        runs the whole fight until its over
        """
        pass



    def round(self):
        """
        Simulate one round of combat between two characters
        FLow of a round is as follows:
            1. determine who makes the move
            2. determine what move the character decided in step 1 makes
            3. determine if the move succeeds or not
            4a. if the move succeeds, apply any damage and other modifiers to characters
            4b. if the move fails, determine what counter attack,
                   if any, the other character makes, and apply the results to characters
            5. determine if the fight is won
        """
        pass


class Ruleset():
    """
    Models the simulation of the rules of fight
    Every fight will have a common pool of moves that all characters can use,
     in addition to character specific moves
    Every fight will have some set of conditions to determine victory,
     such as running out of stamina, tapping out, etc
    """
    name = "New Fight"
    standard_moves = []
    common_stats = []
    win_conditions = []

    @classmethod
    def from_data(cls, data):
        pass


    def as_data(self):
        pass



class Character(object):
    """
    Simulates a single fighter character
    Every character can have some set of nicknames to pull from
    Every character has certain base stats
    Every character can have their own pool of special moves

    """

    nicknames = ["New Character"]
    base_stats = []
    _stats = []
    signature_moves = []


    @property
    def name(self):
        return util.choice(self.nicknames)


    def change_stats(self, stat_breakdown):
        for (stat, damage) in stat_breakdown.items():
            self._stats[stat].modify(damage)


    @property
    def stats(self):
        if not self._stats:
            self._stats = self.base_stats
        return self._stats


    @classmethod
    def from_data(cls, data):
        character = Character()
        character.nicknames = data['nicknames']
        character.base_stats = [
            Stat.from_data(stat_data) for stat_data in data['stats']
        ]
        character.signature_moves = [
            Move.from_data(move_data) for move_data in data['signature_moves']
        ]
        return character


    def as_data(self):
        data = {
            "nicknames": self.nicknames,
            "base_stats": [Stat.as_data(stat) for stat in self.base_stats],
            "signature_moves": [Move.as_data(move) for move in self.signature_moves]
        }
        return data


class Move():
    """
    Represents a single move that a character can perform during combat
    """

    name = "New Move"
    outcomes = []
    prerequisites = []
    priority = 1


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

        if 'priority' in data:
            move.priority = data['priority']

        if 'prerequisites' in data:
            move.prerequisites = data['prerequisites']
        return move


    def as_data(self):
        data = {
            "name": self.name,
            "prerequisites": self.prerequisites,
            "priority": self.priority,
            "outcomes": [Outcome.as_data(outcome) for outcome in self.outcomes]
        }
        return data


    # @classmethod
    # def validate_prerequisite(prerequisite):
    #     """
    #     checks if prerequisite is of a valid format

    #     a prerequisite must be one of:
    #      [my OR their] _stat [>=, >, =, <, <=] X
    #      [my OR their] _stat1 [>=, >, =, <, <=] [my OR their] _stat2
    #      [my OR their] recent move = <_move_name, ...>
    #      [my OR their] last move = <_move_name, ...>
    #      X uses total
    #     """
    #     return True


class Outcome():
    """
    Represents a single possible outcome for a move
    All moves require at least one outcome, otherwise they will be ignored
    """
    name = "New Outcome"
    damage = []
    descriptions = []
    rate = 1


    @classmethod
    def from_data(cls, data):
        outcome = Outcome()
        outcome.name = data['name']

        if 'damage' in data:
             outcome.damage = data['damage']

        if 'descriptions' in data:
            outcome.descriptions = data['descriptions']
        else:
            outcome.descriptions = ["|a performs a {}!".format(data['name'])]

        if 'rate' in data:
            outcome.rate = data['rate']
        return outcome


    def as_data(self):
        data = {
            'name': self.name,
            'rate': self.rate,
            'damage': self.damage
        }
        return data


class Stat():
    """
    represents a single statistical value for characters
    stats determine what moves will be performed and how effective they will be
    """
    name = "New Stat"
    value = 10
    regen = 0

    @classmethod
    def from_data(cls, data):
        stat = Stat()
        stat.name = data['name']

        if 'value' in data:
            stat.value = data['power']

        if 'regen' in data:
            stat.regen = data['regen']
        return stat


    def as_data(self):
        data = {
            'name': self.name,
            'value': self.value,
            'regen': self.regen
        }
        return data
