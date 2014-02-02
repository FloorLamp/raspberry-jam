from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temps.csv')
def temps():
    with open('temps.csv') as f:
        BUFSIZ = 1024
        f.seek(0, 2)
        bytes = f.tell()
        size = 10800
        block = -1
        data = []
        while size > 0 and bytes > 0:
            if bytes - BUFSIZ > 0:
                # Seek back one whole BUFSIZ
                f.seek(block * BUFSIZ, 2)
                # read BUFFER
                data.insert(0, f.read(BUFSIZ))
            else:
                # file too small, start from begining
                f.seek(0, 0)
                # only read what was not read
                data.insert(0, f.read(bytes))
            linesFound = data[0].count('\n')
            size -= linesFound
            bytes -= BUFSIZ
            block -= 1
    return '\n'.join(''.join(data).splitlines()[-10800:])

if __name__ == '__main__':
    app.run(host='0.0.0.0')