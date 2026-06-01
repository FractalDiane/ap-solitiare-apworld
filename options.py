from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions

class DeathLink(Toggle):
	"""
	Enables DeathLink.
	If you fulfill the DeathLink criteria, you will send a DeathLink to other players with it enabled.
	If another player with DeathLink enabled sends it to you, you will receive a punishment.
	"""

	display_name = "DeathLink"


class DeathLinkCriteria(Choice):
	"""
	The criteria required for sending a DeathLink.
	- Game Reset: Sends a DeathLink whenever you reset the game, such as when you get stuck.
	- Exhaust Deck: Sends a DeathLink whenever you go through the deck a certain number of times.
	"""

	display_name = "DeathLink Criteria"

	option_game_reset = 0
	option_exhaust_deck = 1

	default = option_game_reset


class DeathLinkCriteriaCount(Range):
	"""
	How many times the specified DeathLink criteria must occur to send a DeathLink.
	It is recommended to set this to 1 for Game Reset, and HIGHLY recommended to set it to something higher than 1 for Exhaust Deck.
	"""

	display_name = "DeathLink Criteria Count"

	range_start = 1
	range_end = 10
	default = 1


class DeathLinkPunishment(Choice):
	"""
	What unfortunate thing will happen to you when someone sends you a DeathLink. Only applies if DeathLink is enabled.
	- None: You can send DeathLinks, but nothing will happen when you receive one. You monster.
	- Random Trap: Activates the effects of a random trap.
	- Freeze: Freezes your game for 20 seconds, preventing you from doing anything.
	- Defoundation: One card from the top of each foundation is removed and shuffled back into the draw pile.
	- Blackout: Turns all non-top cards facedown in two random columns.
	- Reset Game: Resets the entire game. VERY evil and not recommended.
	"""

	display_name = "DeathLink Punishment"

	option_none = 0
	option_random_trap = 1
	option_freeze = 2
	option_defoundation = 3
	option_blackout = 4
	option_reset_game = 5

	default = option_blackout

class TrapFillPercentage(Range):
	"""
	Percentage of filler checks that will be replaced with traps.
	"""

	display_name = "Trap Fill Percentage"

	range_start = 0
	range_end = 100
	default = 50

@dataclass
class SolitaireOptions(PerGameCommonOptions):
	death_link: DeathLink
	death_link_criteria: DeathLinkCriteria
	death_link_criteria_count: DeathLinkCriteriaCount
	death_link_punishment: DeathLinkPunishment
	trap_fill_percentage: TrapFillPercentage
