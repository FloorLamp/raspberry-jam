from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temps.csv')
def temps():
    with open('temps.csv') as log_file:
        temps = log_file.read()
    return temps

if __name__ == '__main__':
    app.run(host='0.0.0.0')