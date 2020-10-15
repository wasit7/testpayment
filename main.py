from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    print(str(request))
    return str(request.json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')