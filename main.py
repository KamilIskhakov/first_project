from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/catalog')
def about():
    return render_template("about.html")

@app.route('/catalog/banana')
def banana():
    return render_template("banana.html")

@app.route('/catalog/pineapple')
def pineapple():
    return render_template("pineapple.html")

@app.route('/catalog/orange')
def orange():
    return render_template("orange.html")

@app.route('/catalog/banana/buy')
def banana_buy():
    return render_template("banana_buy.html")

@app.route('/catalog/orange/buy')
def orange_buy():
    return render_template("banana_buy.html")

@app.route('/catalog/pineapple/buy')
def pineapple_buy():
    return render_template("banana_buy.html")





@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page :"+ name + "-" + str(id)

if __name__ == "__main__":
    app.run()