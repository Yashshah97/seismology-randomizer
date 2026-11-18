"""Demo for Seismology Monte Carlo Engine."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import seismology_randomizer

print("Seismology Monte Carlo Engine", "v" + seismology_randomizer.__version__)
print("modules:", [m for m in dir(seismology_randomizer) if not m.startswith('_')])
