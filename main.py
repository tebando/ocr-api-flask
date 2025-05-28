# main.py

from app import app  # app.pyにFlaskアプリがあるとする

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
