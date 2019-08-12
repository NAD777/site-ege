from flask import Flask, render_template, redirect
from read import read, delete, add, done

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('add.html')


@app.route('/table')
def table():
    a = read('data')
    return render_template('table.html', content=a)


@app.route('/done/<name_task>')
def done_task(name_task):
    done('data', name_task, 'done')
    return redirect('/table')


@app.route('/add/<name_task>')
def add_task(name_task):
    if add('data', name_task, 'data', 'done'):
        return redirect('/')
    else:
        return render_template('was.html', num=name_task)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
