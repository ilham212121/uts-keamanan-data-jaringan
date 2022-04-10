from flask import Flask, flash, redirect,render_template, request, url_for
from flask_wtf.csrf import CSRFProtect
from form import RegistrationForm

app=Flask(__name__)
csrf=CSRFProtect()
app.config['SECRET_KEY']="DHOLBENK"
SERVER_NAME = '192.168.43.143:8000'
app.config['SERVER_NAME']=SERVER_NAME
app.config.update(
    DEBUG=True,
    SECRET_KEY="dolbenk",

)
csrf.init_app(app)

@app.route("/")
def index():
    form = RegistrationForm()
    return render_template('home.html', form=form)
@app.route("/post",methods=['POST'])

def post():
    print('-------{0}'.format(request.form))
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('data terkirim dengan aman')
        return redirect(url_for('index'))
    return render_template('home.html', form=form)
if __name__ == '__main__' :
    app.run(host="0.0.0.0",debug=True,port=8000)