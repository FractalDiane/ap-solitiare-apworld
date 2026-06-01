from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
	from .world import SolitaireWorld

import random

ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["0", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

item_id = 1
for suit in range(4):
	for value in range(1, 14):
		name = f"{values[value]} of {suits[suit]}"
		DEFAULT_ITEM_CLASSIFICATIONS[name] = ItemClassification.progression
		ITEM_NAME_TO_ID[name] = item_id
		item_id += 1

traps = [
	"Rainbow Trap",
	"Mirror Trap",
]

for trap in traps:
	DEFAULT_ITEM_CLASSIFICATIONS[trap] = ItemClassification.trap
	ITEM_NAME_TO_ID[trap] = item_id
	item_id += 1

ITEM_NAME_TO_ID["Joker"] = item_id
DEFAULT_ITEM_CLASSIFICATIONS["Joker"] = ItemClassification.filler

class SolitaireItem(Item):
	game = "Solitaire"

################################################################################

def get_random_filler_item_name(world: SolitaireWorld) -> str:
	if world.random.randint(0, 99) < world.options.trap_fill_percentage:
		return world.random.choice(traps)
	else:
		return "Joker"

def create_item_with_correct_classification(world: SolitaireWorld, name: str) -> SolitaireItem:
	classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
	return SolitaireItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SolitaireWorld) -> None:
	item_pool: list[Item] = [world.create_item(item) for item in ITEM_NAME_TO_ID]

	aces = [it for it in item_pool if "Ace" in it.name]

	number_of_items = len(item_pool)
	number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
	needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

	item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

	world.multiworld.itempool += item_pool

	world.push_precollected(world.random.choice(aces))
