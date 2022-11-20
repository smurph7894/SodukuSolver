from flask_app import app

class Solver:

    def __init__(self, data):
        self.horizontalLine = data['horizontalLine'],
        self.verticalLine = data['verticalLine']