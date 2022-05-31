from __main__ import app

from flask import request

@app.route('/test', methods=['GET'])
def test():
    return 'Si'