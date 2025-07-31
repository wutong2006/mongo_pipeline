
"""
Funktionen zum Extrahieren von Daten
"""

import csv
from pathlib import Path
from typing import Generator


# (str | Path) filepath kann als str oder path gegeben werden.
def extract_csv(filepath: str | Path) -> Generator[dict, None, None]:
    """
    Liest eine CSV-Datei ein und gibt einen
    Generator zurück.
    """
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
