from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,send_from_directory,make_response
import json
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/translate',methods=['GET', 'POST'])
def translate():
    text=request.data.decode('utf-8')
    translator = Translator()
    print("translating ...")
    translations = translator.translate([text], dest='vi')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
    string_me=text
    string_bot=translation.text
    print("done")
    return json.dumps({"me":string_me,"bot":string_bot})
 
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)