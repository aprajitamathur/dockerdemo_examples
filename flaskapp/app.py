from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/', methods=["POST"])
def some_function():
    text = request.form.get('name')
    return "Hello {}!".format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)