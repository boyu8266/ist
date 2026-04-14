# Python Investment Strategy Tracker

<div style="display: flex; justify-content: center;">
  <img src="images/demo.gif" alt="alt_text" height="480px">
</div>

- [Python Investment Strategy Tracker](#python-investment-strategy-tracker)
  - [Basic Information](#basic-information)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Docker Usage](#docker-usage)

## Basic Information
| Key            | Value       |
|----------------|-------------|
| Data Source    | FinMind API |
| Design Pattern | pipeline    |
| Test           | pytest      |

## Installation

### From Source via pipx

```bash
cd ist
pipx install .
```

This installs the `ist` CLI command that can be run from anywhere.

### Development Installation

```bash
cd ist
pip install -e .
```

## Configuration

### 1. Create Config Directory

```bash
mkdir -p ~/.config/ist
```

### 2. Setup Config File

Copy the example config to the config directory:

```bash
cp config.example.ini ~/.config/ist/config.ini
# Edit ~/.config/ist/config.ini with your settings
```

Or create `config.ini` in the current directory (for development):

```bash
cp config.example.ini config.ini
```

### Config File Locations (Priority Order)

1. `./config.ini` - Current directory (development)
2. `~/.config/ist/config.ini` - User config directory (installed)

The first existing file will be used.

### Example Configuration

```ini
[Telegram]
token = 1111111111:xxxxxxxxxxxxxxxxxxxxxxxxx
userid = 111111111

[Strategy]
; The order of strategies, numbers, and periods must be the same

numbers = 1101, 1102, 2330
; Implemented in the ist/custom.py file
strategies = Custom, Custom, Custom
; Support Day, Week and Month
periods = Day, Week, Month
```

## Docker Usage

### Build Image
```bash
docker build -t ist:latest .
```

### Run Container with Config File
Mount your `config.ini` file into the container:
```bash
docker run -v $(pwd)/config.ini:/app/config.ini ist:latest
```

Or copy from `config.example.ini`:
```bash
cp config.example.ini config.ini
# Edit config.ini with your settings
docker run -v $(pwd)/config.ini:/app/config.ini ist:latest
```