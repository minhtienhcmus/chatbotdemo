from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,send_from_directory,make_response
import os
import sys
import json
from datetime import datetime
import time
from PIL import Image
import argparse
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    # translator = Translator()
    # #demo detect language
    # langs = translator.detect(['한국어', '日本語', 'English', 'le français',"viet nam"])
    # for lang in langs:
    #     print(lang.lang, lang.confidence)
    return render_template("index.html")

@app.route('/translate',methods=['POST'])
def translate():
    print("abc")
    print(request.method)
    text = request.data.decode('utf-8')
    print(text)
    translator = Translator()
    langs = translator.detect(['한국어', '日本語', 'English', 'le français',"viet nam"])
    for lang in langs:
        print(lang.lang, lang.confidence)
    print("translating ...")
    translations = translator.translate([text], dest='vi')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)

    output=translation.text

    return json.dumps({"text":output})
 
    
if __name__ == '__main__':
	app.run(port="8889",debug=True)