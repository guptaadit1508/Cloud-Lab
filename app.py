from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the root route
@app.route("/")
def home():
    return "Hello, World! This is a basic Flask app."

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True, port=5000)
