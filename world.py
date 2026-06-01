from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as solitaire_options

class SolitaireWorld(World):
	"""
	The classic Klondike Solitaire, now with archipelago!
	"""

	game = "Solitaire"

	web = web_world.SolitaireWebWorld()

	options_dataclass = solitaire_options.SolitaireOptions
	options: solitaire_options.SolitaireOptions # type: ignore

	location_name_to_id = locations.LOCATION_NAME_TO_ID
	item_name_to_id = items.ITEM_NAME_TO_ID

	origin_region_name = "Start"

	def create_regions(self) -> None:
		regions.create_and_connect_regions(self)
		locations.create_all_locations(self)

		from Utils import visualize_regions
		visualize_regions(self.multiworld.get_region("Start", self.player), "solitaire_regions.puml", show_entrance_names=True, detail_other_regions=True)

	def set_rules(self) -> None:
		rules.set_all_rules(self)

	def create_items(self) -> None:
		items.create_all_items(self)

	def create_item(self, name: str) -> items.SolitaireItem:
		return items.create_item_with_correct_classification(self, name)
	
	def get_filler_item_name(self) -> str:
		return items.get_random_filler_item_name(self)
	
	def fill_slot_data(self) -> Mapping[str, Any]:
		return self.options.as_dict(
			"death_link",
			"death_link_criteria",
			"death_link_criteria_count",
			"death_link_punishment",
			"trap_fill_percentage",
		)

	def generate_output(self, output_directory: str) -> None:
		from Utils import visualize_regions
		visualize_regions(self.multiworld.get_region("Start", self.player), "solitaire_regions.puml", show_entrance_names=True, detail_other_regions=True)
		return super().generate_output(output_directory)
