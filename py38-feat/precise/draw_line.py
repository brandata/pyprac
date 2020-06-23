# draw_line.py

# Mypy wont detect an error even if you pass in 'up'
from typing import Literal
def draw_line(direction: Literal["horizontal", "vertical"]) -> None:
    if direction == "horizontal":
        ...  # Draw horizontal line

    elif direction == "vertical":
        ...  # Draw vertical line

    else:
        raise ValueError(f"invalid direction {direction}")

draw_line("up")
