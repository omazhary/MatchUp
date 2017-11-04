from flask import Flask, render_template, request, json
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate():
    _participants = request.form['participants']
    if _participants:
        return json.dumps({'html':'<span>Field good!</span>'})
    else:
        return json.dumps({'html':'<span>Field bad!</span>'})

if __name__ == "__main__":
    app.run()
