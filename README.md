# RepairQRG

A small Python library and command line tool that provides a sample **Repair Quick
Reference Guide**. The guide contains curated repair procedures for household
appliances, consumer electronics, and residential HVAC systems.

## Features

- Categorised repair procedures with summaries, time estimates, and difficulty
  levels.
- Detailed step-by-step instructions with tips and supplemental notes.
- Command line interface to browse categories, search for procedures, and print
  detailed instructions.

## Installation

The project has no third-party dependencies and can be run directly with
Python 3.11 or newer. Clone the repository and install it in editable mode:

```bash
pip install --editable .
```

## Usage

List the available categories:

```bash
python -m repairqrg.cli categories
```

Show details for a specific category:

```bash
python -m repairqrg.cli category appliances
```

Search for procedures containing a keyword:

```bash
python -m repairqrg.cli search "charging"
```

Display the full procedure for the best matching result:

```bash
python -m repairqrg.cli procedure "Refrigerator"
```

Each command prints formatted output to the terminal, making it easy to share
and adapt the information for field technicians.
