from move import Move
from stat import Stat
import util


class Character(object):
    """
    Simulates a single fighter character
    Every character can have some set of nicknames to pull from
    Every character has certain base stats
    Every character can have their own pool of special moves

    """
    def __init__(
        self,
        *,
        name="New Character",
        nicknames=[],
        base_stats=[],
        special_moves=[]):

        super(Character, self).__init__()
        self.name = name
        self.aliases = nicknames.append(self.name)
        self.stats = base_stats
        self.base_stats = base_stats
        self.special_moves = special_moves


    def name(self):
        return util.choice(self.aliases)


    def perform_move_on_self(*, move=None):
        stat_breakdown = move.stat_breakdown()
        self.change_stats(stat_breakdown)


    def perform_move(*, move=None, victim=None):
        stat_breakdown = move.stat_breakdown()
        victim.change_stats(stat_breakdown)
        return move.format(performer=self.name(), victim=victim.name())


    def change_stats(stat_breakdown):
        for (stat, damage) in stat_breakdown.items():
            self.stats[stat] -= damage