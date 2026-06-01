from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
	from .world import SolitaireWorld

def set_all_rules(world: SolitaireWorld) -> None:
	set_all_entrance_rules(world)
	set_all_location_rules(world)
	set_completion_condition(world)

def set_all_entrance_rules(world: SolitaireWorld) -> None:
	pass

def set_all_location_rules(world: SolitaireWorld) -> None:
	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values = ["0", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	for suit in range(4):
		for value in range(1, 14):
			location_name = f"{values[value]} of {suits[suit]} on foundation"
			item_names = [f"{values[val]} of {suits[suit]}" for val in range(1, value + 1)]
			
			world.set_rule(world.get_location(location_name), HasAll(*item_names))

def set_completion_condition(world: SolitaireWorld) -> None:
	world.set_completion_rule(HasAll("Hearts complete", "Diamonds complete", "Clubs complete", "Spades complete"))
