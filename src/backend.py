import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS


# Configure Flask app for Cloud Run
app = Flask(__name__, static_folder="../dist", static_url_path="")

# Configure CORS based on environment
if os.getenv("FLASK_ENV") == "production":
    # Production: Allow Cloud Run domains and common domains
    CORS(
        app,
        resources={
            r"/*": {
                "origins": ["*"],  # Allow all origins for Cloud Run
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
    )
else:
    # Development: Only allow localhost
    CORS(
        app,
        resources={
            r"/*": {"origins": ["http://localhost:5173", "http://localhost:3000"]}
        },
        supports_credentials=True,
    )

print("Starting up the Flask backend....")
@app.route("/webscrape", methods=["GET", "POST"])
def webscrape():
    if request.method == "GET":
        return jsonify({"success": False, "error": "This route only accepts POST method requests"})
    else:
        print("Received a request to /webscrape")
        try:
            data = request.json
            url = data.get("url", "")

            print(f"The url that was passed in is {url}")
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"success": False, "error": f"Server error: {str(e)}"}), 500
    
# Global error handler to ensure all errors return JSON
@app.errorhandler(Exception)
def handle_exception(e):
    """Global exception handler to ensure JSON responses."""
    import traceback
    from werkzeug.exceptions import HTTPException

    error_details = traceback.format_exc()
    print(f"Unhandled exception: {error_details}")

    # For HTTP exceptions, return a cleaner response
    if isinstance(e, HTTPException):
        return jsonify(
            {"success": False, "error": f"{e.name}: {e.description}"}
        ), e.code

    # For all other exceptions, return a generic JSON error
    return jsonify({"success": False, "error": f"Internal server error: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_ENV") != "production")
