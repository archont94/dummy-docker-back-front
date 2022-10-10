from flask import Flask
app = Flask(__name__)

BACKEND_PORT = 8800
global_cnt = 0

@app.route('/')
def home():
    return "homepage"

@app.route('/get_global_cnt')
def get_global_cnt():
    global global_cnt
    global_cnt = global_cnt + 1
    return str(global_cnt)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=BACKEND_PORT)
