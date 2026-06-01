from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class SolitaireWebWorld(WebWorld):
	game = "Solitaire"

	theme = "grassFlowers"

	setup_en = Tutorial(
		"Multiworld Setup Guide",
		"A guide to setting up Solitaire for Multiworld.",
		"English",
		"setup_en.md",
		"setup/en",
		["FractalDiane"],
	)

	tutorials = [setup_en]
