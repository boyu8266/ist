# Python Investment Strategy Tracker

<div style="display: flex; justify-content: center;">
  <img src="images/demo.gif" alt="alt_text" height="480px">
</div>

- [Python Investment Strategy Tracker](#python-investment-strategy-tracker)
  - [Basic Information](#basic-information)
  - [Docker Usage](#docker-usage)

## Basic Information
| Key            | Value       |
|----------------|-------------|
| Data Source    | FinMind API |
| Design Pattern | pipeline    |
| Test           | pytest      |

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