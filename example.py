from flask import Flask, request, render_template
##import os

##project_root = os.path.dirname(__file__)
##template_path = os.path.join(project_root, 'app/templates')
app = Flask(__name__)
##app = Flask(__name__, template_folder=template_path)


@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/shopping')
def shopping():
    food = ["cheese", "tuna", "beef"]
    return render_template("shopping.html", food=food)


@app.route('/method')
def method():
    return "Method used %s" % request.method


@app.route('/bacon', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        return "YOU are using POST"
    else:
        return "You are probably using GET"


@app.route('/tuna')
def tuna():
    return "<h1>Tuna is good</h1>"


@app.route('/profile/<name>')
def czemu(name):
    try:
        return render_template("profile.html", name = name)
    except Exception as e:
        return "Exception: %s" % str(e)


@app.route('/katalog/<kat>')
def katalog(kat):
    return "<h2>Hey there %s</h2>" % kat


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id



if __name__ == "__main__":

##    app.run(debug=True)
    app.run()
