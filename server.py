from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temps.csv')
def temps():
    return send_from_directory('', 'temps.csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0')