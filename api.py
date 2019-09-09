from flask import Flask, request, render_template,jsonify
import subprocess as sp
import re
import nltk
from autocorrect import spell
from gensim.summarization import summarize as g_sumn

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/model_demo', methods=["GET"])
def model_demo():
    return render_template('model_demo.html')


@app.route('/installation', methods=["GET"])
def installation():
    return render_template('installation.html')

@app.route("/summarize", methods=["GET","POST"])
def summarize():
    text = request.form['text']
    sent = nltk.sent_tokenize(text)
    if len(sent) < 2:
        summary1 =  "please pass more than 3 sentences to summarize the text"
    else:
        summary = g_sumn(text)
        summ = nltk.sent_tokenize(summary)
        summary1 = (" ".join(summ[:2]))
    result = {
        "result": summary1
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route("/generate", methods=["GET","POST"])
def generate():
    text = request.form['text']

    text=str(text)
    
    text=text.replace("&lt;","<")
    text=text.replace("&gt;",">")

    text_file = open("temp.txt", "w")
    text_file.write(text)
    text_file.close()

    text += "hello world!"
    p = sp.getoutput("./test.sh")
    text += str(p)
    return text

if __name__ == '__main__':
    app.run(port=8888)
    #app.run(host='0.0.0.0', port=8888)