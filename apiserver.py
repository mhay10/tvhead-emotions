from flask import Flask, request
from threading import Thread
from constants import *


class APIServer:
    def __init__(self, callback, port=WEBSERVER_PORT):
        # Create Flask instance
        self.app = Flask(__name__)
        self.port = port

        # Setup API routes
        self.setup_routes()

        # Store expression change callback
        self.callback = callback

    def verify_expression(self, request):
        # Verify expression from request
        data = request.get_json(force=True, silent=True)
        if not data:
            return False, "Invalid request: No JSON data found", 400

        # Verify expression field
        expression = data.get("expression")
        if not expression:
            return False, "Invalid request: 'expression' field is required", 400
        elif expression not in [*EXPRESSION_KEYMAP.values(), DEFAULT_EXPRESSION]:
            return False, f"Invalid expression: '{expression}' not recognized", 400

        return True, expression, 200

    def setup_routes(self):
        # Register homepage route
        @self.app.route("/")
        def homepage():
            # Serve API usage HTML file
            with open(WEBSERVER_API_USAGE_HTML, "r") as file:
                return file.read(), 200

        # Setup expression change route
        @self.app.route("/set-expression", methods=["POST"])
        def set_expression():
            # Verify expression from request
            valid, expression, status_code = self.verify_expression(request)
            if not valid:
                return expression, status_code

            # Update expression via callback
            self.callback(expression)
            return f"Expression set to '{expression}'", 200

        # Setup default expression route
        @self.app.route("/reset-expression", methods=["POST"])
        def reset_expression():
            # Reset expression to default via callback
            self.callback(DEFAULT_EXPRESSION)
            return f"Expression reset to '{DEFAULT_EXPRESSION}'", 200

    def start(self):
        # Start server in background thread
        thread = Thread(
            target=self.app.run,
            kwargs={"host": WEBSERVER_HOST, "port": WEBSERVER_PORT},
            daemon=True,
        )
        thread.start()
