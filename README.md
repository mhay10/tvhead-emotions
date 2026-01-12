# TVHead Emotions

A simple fullscreen Pygame application that displays customizable facial expressions on a TV head character.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [Pillow](https://pypi.org/project/Pillow/)
- [pygame-ce](https://pypi.org/project/pygame-ce/)

## Installation

### 1. Clone or download this repository

```bash
git clone <repository-url>
cd tvhead-emotions
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the application

```bash
python main.py
```

The application will launch in fullscreen. Use the following keys to change expressions:

- `1` - Happy
- `2` - Sad
- `3` - Angry
- `4` - Surprised
- `5` - Tired
- `6` - Skeptical
- `7` - Love
- `8` - Confused
- `ESC` - Quit Program

Expressions display while the key is held down and return to neutral when released.  

There is a 200ms delay between expression changes to prevent glitchy visuals.
