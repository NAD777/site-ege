from flask import Flask, render_template, redirect
import read

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('add.html')


@app.route('/table')
def table():
    a = read.read('data')
    return render_template('table.html', content=a)


@app.route('/done/<name_task>')
def done_task(name_task):
    read.done('data', name_task, 'done')
    return redirect('/table')


@app.route('/add/<name_task>')
def add_task(name_task):
    if read.add('data', name_task, 'data', 'done'):
        return redirect('/table')
    else:
        return render_template('was.html', num=name_task)


@app.route('/del/<name_task>')
def del_task(name_task):
    read.delete('data', name_task)
    return redirect('/table')


@app.route('/done')
def done():
    content = read.read('done')
    return render_template('done.html', content=content, col=len(content))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27018)
