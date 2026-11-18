# Seismology Monte Carlo Engine

This project provides a robust Monte Carlo engine specifically designed to analyze earthquake waveform data, allowing users to run simulations and generate reliable confidence intervals. Built from the ground up in pure Python, this tool prioritizes ease of use and flexibility. With comprehensive testing and documentation in place, researchers can quickly integrate this engine into their workflows.

## What makes it unique

Combines earthquake waveform data with a Monte Carlo experiment runner with confidence intervals — a niche where few ready-made tools exist.

## Features

- **`seismology_randomizer/main.py`** — Main entry point for the project
- **`seismology_randomizer/engine.py`** — Monte Carlo experiment runner with confidence intervals
- **`seismology_randomizer/data_loader.py`** — Loads and preprocesses earthquake waveform data
- **`seismology_randomizer/results_processor.py`** — Processes results from Monte Carlo experiments, including generating plots and statistics
- **`seismology_randomizer/tests_test_engine.py`** — Unit tests for the engine module
- **`seismology_randomizer/docs_conf.py`** — Configuration file for Sphinx documentation generation

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/seismology-randomizer.git
cd seismology-randomizer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
seismology-randomizer/
├── seismology_randomizer/
│   ├── main.py
│   ├── engine.py
│   ├── data_loader.py
│   ├── results_processor.py
│   ├── tests_test_engine.py
│   ├── docs_conf.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **seismology** · Archetype: **randomizer** ·
Built autonomously by JARVIS on 2026-11-17. MIT licensed.
