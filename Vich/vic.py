from flask import Flask, render_template, request

app = Flask(__name__)

formula = 0
a = 0
b = 0
sin = 0


#
#
# @app.route('/')
# def index():
#     return render_template('main')


@app.route('/triangle')
def first():
    global formula
    global a
    global b
    global sin
    if 'a' in request.args:
        a = request.args['a']
    if 'b' in request.args:
        b = request.args['b']
    if 'sin' in request.args:
        sin = request.args['sin']
    formula = int(a) * int(b) * int(sin) * 0.5

    return render_template('xer.html', formula=formula)


app.run(debug=True, port=8080)
