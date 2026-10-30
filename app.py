from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import list_courses, get_course

app = Flask(__name__)

@app.get('/hello/<name>')
def hello(name):
    return jsonify(message=f'Hello, {name}!')

@app.get('/api/square/<int:number>')
def square(number):
    return jsonify(number=number, square=number * number)

@app.get('/courses')
def courses():
    return render_template('courses.html', courses=list_courses())

@app.get('/api/courses')
def courses_api():
    return jsonify(list_courses())

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    name = ''
    selected = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        selected = request.form.get('course', '')
        if not name:
            error = 'Student name is required.'
        elif len(name) > 40:
            error = 'Student name must be 40 characters or fewer.'
        elif not get_course(selected):
            error = 'Choose a valid course.'
        elif get_course(selected)['seats'] < 1:
            error = 'This course has no available seats.'
        else:
            return redirect(url_for('success', name=name, course=selected), code=303)
    return render_template('register.html', courses=list_courses(), error=error,
                           name=name, selected=selected), (400 if error else 200)

@app.get('/success')
def success():
    return render_template('success.html', name=request.args.get('name', ''),
                           course=request.args.get('course', ''))

@app.get('/')
def home():
    return redirect(url_for('courses'))


@app.get('/health')
def health():
    return jsonify(status='ok')
