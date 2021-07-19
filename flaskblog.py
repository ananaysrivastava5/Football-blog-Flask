from flask import Flask, render_template, url_for
app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)    