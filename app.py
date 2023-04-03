from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        python_code = request.form['python_code']
        with open('user_code.py', 'w') as f:
            f.write(python_code)
        return 'File written successfully!'
    return render_template('index.html')