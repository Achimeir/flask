from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rootpage():
    user_name = 'user X'
    user_weight = 0
    user_height = 0
    bmi=0

    if request.method == 'POST' and 'username' in request.form:
        user_name = request.form.get('username')
        user_weight = int(request.form.get('wheight'))
        user_height = int(request.form.get('height'))
        bmi=round(user_weight/((user_height/100)**2),2)
        
    return render_template('index.html', user_name=user_name,bmi=str(bmi))


app.run()
