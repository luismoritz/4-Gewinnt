````markdown
# 4-Gewinnt (Connect 4)

A Python implementation of Connect 4 with:
- Local console gameplay (two players on one machine)
- Optional remote gameplay via a Flask REST API server and client
- Optional Sense HAT display/input support (for Raspberry Pi)

---

## Requirements

- **Python 3.8+**
- Python packages:
  - `flask`
  - `flasgger`
  - `requests`
  - `sense-hat` *(optional, only if using the Sense HAT display/input)*

Install the packages with:

```bash
python -m pip install flask flasgger requests
# Optional for Sense HAT hardware:
python -m pip install sense-hat
````

***

## Project Layout (Key Files)

* `coordinator.py` — entry point for running a local or remote game.
* `game_logic.py` — local game logic implementation.
* `game_logic_server.py` — Flask API server for remote play.
* `game_logic_client.py` — client for communicating with the server.
* `player_console.py` — console-based player (keyboard controls).
* `display_console.py`, `input_console.py` — console I/O.
* `display_sense.py`, `input_sense.py` — Sense HAT I/O (optional).

***

## Run Locally (Two Players on One Machine)

```bash
python coordinator.py
```

When prompted:

* Choose **Local (L)**.
* Two players take turns using the keyboard.

***

## Run Remote (Server + Client)

### 1) Start the game server

```bash
python game_logic_server.py
```

The server listens on port `5000` by default.

### 2) Connect from a client

In another terminal (or another machine), run:

```bash
python coordinator.py
```

When prompted:

* Choose **Remote (R)**.
* Enter the server hostname or IP (e.g., `127.0.0.1` or `192.168.1.10`).
* Choose whether to play as Red or Yellow.

***

## Controls (Console)

Use arrow keys to move the drop position:

* **Left / Right**: move selection
* **Down** or **Enter**: drop token

***

## API Endpoints (Server)

The Flask server exposes:

* `GET /api/board` — current board state
* `GET /api/state` — current game state
* `POST /api/drop` — drop a token

Swagger docs are available when the server is running.

***

## Notes

* Sense HAT functionality is optional and only available on compatible hardware.
* The server runs in debug mode by default; you may want to disable debug for production use.

```
