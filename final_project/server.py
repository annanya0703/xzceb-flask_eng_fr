from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/french_to_english")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    return translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)