from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
	from .world import SolitaireWorld

def create_and_connect_regions(world: SolitaireWorld) -> None:
	create_all_regions(world)
	connect_regions(world)

def create_all_regions(world: SolitaireWorld) -> None:
	regions = [
		Region("Start", world.player, world.multiworld),
	]

	world.multiworld.regions += regions

def connect_regions(world: SolitaireWorld) -> None:
	pass
