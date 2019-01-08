from .move import Move
from .stat import Stat
from . import util


class Character(object):
    """
    Simulates a single fighter character
    Every character can have some set of nicknames to pull from
    Every character has certain base stats
    Every character can have their own pool of special moves

    """

    nicknames=["New Character"],
    base_stats=[],
    _stats = []
    signature_moves=[]


    def name(self):
        return util.choice(self.nicknames)


    def perform_move_on_self(*, move=None):
        stat_breakdown = move.stat_breakdown()
        self.change_stats(stat_breakdown)


    def perform_move(*, move=None, victim=None):
        stat_breakdown = move.stat_breakdown()
        victim.change_stats(stat_breakdown)
        return move.format(performer=self.name(), victim=victim.name())


    def change_stats(stat_breakdown):
        for (stat, damage) in stat_breakdown.items():
            self._stats[stat].modify(damage)


    @property
    def stats(self)
        if not self._stats:
            self._stats = self.base_stats
        return self._stats



    @classmethod
    def from_data(cls, data):
        character = Character()
        character.nicknames = data['nicknames']
        character.base_stats = [Stat.from_data(stat_data)
            for stat_data in data['stats']]
        character.signature_moves = [Move.from_data(move_data)
            for move_data in data['signature_moves']]
        return character


    def as_data(self):
        data = {
            "nicknames": self.nicknames,
            "base_stats": [Stat.as_data(stat) for stat in self.base_stats],
            "signature_moves": [Move.as_data(move) for move in self.signature_moves]
        }
        return data