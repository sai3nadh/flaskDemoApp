from flask import Flask , render_template, url_for

app= Flask(__name__)

@app.route('/')
def index():
    #return "Hello World!!!" Set-ExecutionPolicy Bypass -Scope Process       
    return render_template('index.html')

@app.route('/home.html')
def home():
    #return "Hello World!!!" Set-ExecutionPolicy Bypass -Scope Process       
    return render_template('home.html')


if __name__ == "__main":
    app.run(debug=True)