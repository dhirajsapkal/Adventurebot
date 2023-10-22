import os
import sys
from flask import Flask

sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

from server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
