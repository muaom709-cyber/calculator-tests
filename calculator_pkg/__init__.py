"""Пакет калькулятора для базовых арифметических операций."""

from .input_data import get_user_input
from .operations import calculate
from .output_data import print_result

__all__ = ["calculate", "get_user_input", "print_result"]
