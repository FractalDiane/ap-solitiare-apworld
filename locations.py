from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
	from .world import SolitaireWorld

LOCATION_NAME_TO_ID = {}

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["0", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

item_id = 1
for suit in range(4):
	for value in range(1, 13):
		name = f"{values[value]} of {suits[suit]} on foundation"
		LOCATION_NAME_TO_ID[name] = item_id
		item_id += 1

class SolitaireLocation(Location):
	game = "Solitaire"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
	return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SolitaireWorld) -> None:
	create_regular_locations(world)
	create_events(world)

def create_regular_locations(world: SolitaireWorld) -> None:
	start = world.get_region("Start")

	start_locations = LOCATION_NAME_TO_ID

	start.add_locations(start_locations, SolitaireLocation)

def create_events(world: SolitaireWorld) -> None:
	start = world.get_region("Start")

	start.add_event(
        "King of Hearts on foundation", "Hearts complete", location_type=SolitaireLocation, item_type=items.SolitaireItem
    )
	start.add_event(
        "King of Diamonds on foundation", "Diamonds complete", location_type=SolitaireLocation, item_type=items.SolitaireItem
    )
	start.add_event(
        "King of Clubs on foundation", "Clubs complete", location_type=SolitaireLocation, item_type=items.SolitaireItem
    )
	start.add_event(
        "King of Spades on foundation", "Spades complete", location_type=SolitaireLocation, item_type=items.SolitaireItem
    )
