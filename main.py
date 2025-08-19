"""
Simple game state management utilities.

Exposes:
- `player_state`: initial example state (this name is required by tests)
- `print_status(state) -> str`: returns a formatted status string
- `add_item(state, item) -> None`: adds a unique item to inventory (max 5)
- `take_damage(state, amount) -> None`: reduces health, not below 0
"""

from typing import Dict, List


# Required variable name; test harness may replace this dict at runtime
player_state: Dict[str, object] = {
	"name": "Rupert",
	"health": 10,
	"max_health": 15,
	"inventory": [],  # type: List[str]
	"location": "Start",
}


def print_status(state: Dict[str, object]) -> str:
	"""Return a formatted description of the player's current state.

	Includes:
	- Player name
	- Health (adds "Player has fallen!" if health <= 0)
	- Inventory status ("Inventory: is empty." or comma-separated items with a period)
	- Current location
	"""
	player_name: str = str(state.get("name", ""))
	current_health: int = int(state.get("health", 0))
	maximum_health: int = int(state.get("max_health", 0))
	inventory_items: List[str] = list(state.get("inventory", []))
	current_location: str = str(state.get("location", ""))

	output_lines: List[str] = []
	output_lines.append(f"Name: {player_name}")
	output_lines.append(f"Health: {current_health}/{maximum_health}")
	if current_health <= 0:
		output_lines.append("Player has fallen!")

	if len(inventory_items) == 0:
		output_lines.append("Inventory: is empty.")
	else:
		joined_items: str = ", ".join(str(item) for item in inventory_items)
		output_lines.append(f"Inventory: {joined_items}.")

	output_lines.append(f"Location: {current_location}")
	return "\n".join(output_lines)


def add_item(state: Dict[str, object], item: str) -> None:
	"""Add a unique item to the player's inventory, respecting capacity 5.

	If the item already exists or the inventory is full, the state is unchanged.
	"""
	inventory: List[str] = state.get("inventory")  # type: ignore[assignment]
	if inventory is None:
		# Ensure inventory is a list if absent; tests may inject different states
		inventory = []
		state["inventory"] = inventory

	# Prevent duplicates and enforce max capacity of 5
	if item in inventory:
		return
	if len(inventory) >= 5:
		return

	inventory.append(item)


def take_damage(state: Dict[str, object], amount: int) -> None:
	"""Reduce player's health by `amount`, not allowing it to drop below 0."""
	current_health: int = int(state.get("health", 0))
	new_health: int = max(0, current_health - int(amount))
	state["health"] = new_health


if __name__ == "__main__":
	# Simple demo; not required for tests
	print(print_status(player_state))
