import json
import logging
from datetime import datetime

from flask import Flask, request
from flask_api import status

app = Flask(__name__)
logging.basicConfig(filename='cybserver.log', level=logging.DEBUG)


@app.route('/', methods=['POST'])
def receive_process_info():
    logging.info('Receiving process data from client...')
    processes = request.get_json(force=True)
    logging.info('Processes data follows at {}: {}'.format(datetime.now(), processes))
    return 'Success', status.HTTP_200_OK


if __name__ == '__main__':
    app.run()
