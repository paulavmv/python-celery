from app.src.app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host=os.environ.get('WSGI_HOST ', 'localhost:5000'), port=port)
