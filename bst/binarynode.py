from __future__ import annotations
from typing import Any, Callable
from dataclasses import dataclass


@dataclass
class BinaryNode:
    value: Any
    left_child: BinaryNode = None
    right_child: BinaryNode = None
