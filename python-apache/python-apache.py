

from dotenv import load_dotenv

# -------------------------------------------------
# Load environment variables
# -------------------------------------------------
CONFIG_PATH = "config/.env"

def load_env():
    load_dotenv(dotenv_path=CONFIG_PATH)

load_env()

# -------------------------------------------------
# Run Flask App
# -------------------------------------------------
from flaskApp import app

if __name__ == '__main__':
    app.run(debug=True)
