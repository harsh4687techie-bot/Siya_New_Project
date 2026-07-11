import os

from app import create_app

config_name = os.getenv("FLASK_CONFIG")
if not config_name and os.getenv("VERCEL"):
    config_name = "production"

app = create_app(config_name)

if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False), host="0.0.0.0", port=5000)
