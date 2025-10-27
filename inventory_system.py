# inventory_system.py
"""Simple inventory system — cleaned for static analysis lab."""
import json
from datetime import datetime
from typing import Dict, List, Optional

# Global variable
stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int, logs: Optional[List[str]] = None) -> None:
    """Add items to inventory with validation and optional logging."""
    if logs is None:
        logs = []

    if not isinstance(item, str):
        raise ValueError("item must be a string")
    if not isinstance(qty, int):
        raise ValueError("qty must be an integer")
    if qty <= 0:
        raise ValueError("qty must be a positive integer")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    """Remove items from inventory safely."""
    if not isinstance(item, str):
        raise ValueError("item must be a string")
    if not isinstance(qty, int):
        raise ValueError("qty must be an integer")
    if qty <= 0:
        raise ValueError("qty must be a positive integer")

    if item not in stock_data:
        # explicitly handle missing item
        print(f"Warning: item '{item}' not found.")
        return

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]


def get_qty(item: str) -> int:
    """Return quantity of item (0 if not present)."""
    if not isinstance(item, str):
        raise ValueError("item must be a string")
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load inventory from JSON file if possible."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("inventory file does not contain a JSON object")
        # normalize values to ints and strings to keys
        new_data: Dict[str, int] = {}
        for k, v in data.items():
            if not isinstance(k, str) or not isinstance(v, int):
                continue
            new_data[k] = v
        stock_data = new_data
    except FileNotFoundError:
        stock_data = {}
    except (json.JSONDecodeError, ValueError):
        # corrupted JSON — start with empty inventory
        stock_data = {}


def save_data(file: str = "inventory.json") -> None:
    """Save inventory to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2, ensure_ascii=False)


def print_data() -> None:
    """Print inventory report."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of items whose qty is below threshold."""
    if not isinstance(threshold, int) or threshold < 0:
        raise ValueError("threshold must be a non-negative integer")
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Demo run — small sanity operations."""
    try:
        add_item("apple", 10)
        add_item("banana", 2)
        # invalid examples commented out; we validate inputs now
        remove_item("apple", 3)
        remove_item("orange", 1)
        print(f"Apple stock: {get_qty('apple')}")
        print("Low items:", check_low_items())
        save_data()
        load_data()
        print_data()
    except ValueError as exc:
        print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
