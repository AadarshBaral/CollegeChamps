from flask_sqlalchemy import _DebugQueryTuple
from collegechamps import app
import os
port = int(os.getenv('PORT'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
