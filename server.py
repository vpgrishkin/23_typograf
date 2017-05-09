from flask import Flask, render_template, request

from typograf import typografy_text


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/typografy', methods=['POST'])
def typografy():
    typographed_text = typografy_text(request.form['text'])
    if typographed_text == '' or typographed_text is None:
        return 'No text'
    return typographed_text


if __name__ == "__main__":
    app.run(debug=True)
