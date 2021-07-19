from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3e10ea9a7101ae69e3e9314756688bee'


posts = [
    {
        'author': 'Ananay Srivastava',
        'title': 'Messi is the GOAT. Period.',
        'content': 'Messi proved that he is the undisputed GOAT by winning the COPA America.',
        'date_posted': 'July 12, 2021'
    }, 
    {
        'author': 'Aman Srivastava',
        'title': 'CR7 wins the Golden Boot.',
        'content': "Cristiano Ronaldo proving his haters wrong for (well we've lost count now)th time "
                   "by winning the Golden Boot at the Euros 2021.",
        'date_posted': 'July 14, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)    