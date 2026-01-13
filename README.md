# TVHead Emotions

A Pygame application that displays customizable facial expressions on a TV head character.

## Requirements

-   [Python 3.x](https://www.python.org/downloads/)
-   [Pillow](https://pypi.org/project/Pillow/)
-   [pygame-ce](https://pypi.org/project/pygame-ce/)
-   [Flask](https://pypi.org/project/Flask/)

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

-   **Windows**: `venv\Scripts\activate`
-   **macOS/Linux**: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the application

```bash
python main.py [--windowed]
```

The application will launch in fullscreen unless `--windowed` is used. Use the following keys to change expressions:

-   `1` - Happy
-   `2` - Sad
-   `3` - Angry
-   `4` - Surprised
-   `5` - Tired
-   `6` - Skeptical
-   `7` - Love
-   `8` - Confused
-   `ESC` - Quit

Expressions display while the key is held down and return to neutral when released.  
There is a 200ms delay between expression changes to prevent glitchy visuals.

### Using the API

The application includes an API server that can also change the displayed expression.
The API server listens on all interfaces at port `5000` by default.

To change the expression via the API, send a POST request to `/set-expression` with a JSON body:

```bash
curl -X POST http://<host>:5000/set-expression \
     -d '{"expression": "happy"}'
```

You can also reset the expression by sending a POST request to `/reset-expression`:

```bash
curl -X POST http://<host>:5000/reset-expression
```

A simple HTML page documenting the API usage is available at the root endpoint (`/`).
