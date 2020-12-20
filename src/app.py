from flask import Flask, render_template, request

app = Flask(__name__, static_folder="../static",
            template_folder="../templates",)


@app.route('/bmi', methods=['GET', 'POST'])
def bmi_page():
    user_name = 'user X'
    user_weight = 0
    user_height = 0
    bmi = 0

    if request.method == 'POST' and 'username' in request.form:
        user_name = request.form.get('username')
        user_weight = request.form.get('weight', default=0, type=float)
        user_height = request.form.get('height', default=0, type=float)
        if user_height and user_height:
            bmi = round(user_weight/((user_height/100)**2), 2)

    return render_template('bmi_calc.html', user_name=user_name, bmi=str(bmi))


@app.route('/', methods=['GET', 'POST'])
def rootpage():
    return render_template('index.html')


app.run(host='resite02.herokuapp.com',port=8080)
