from flask import Flask, request, render_template,jsonify
import subprocess as sp
import sys

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

@app.route("/generate", methods=["GET","POST"])
def generate():
    text = request.form['text']
    model = request.form['model']
    resource = request.form['resource']

    text=str(text)
    
    text=text.replace("&lt;","<")
    text=text.replace("&gt;",">")

    text_file = open("input.txt", "w")

    print (model, file=sys.stderr)
    print (resource, file=sys.stderr)
    if (model == "transformer"):
        text_file.write(text)
        text_file.close()
        if (resource == "full"):
            p = sp.getoutput("./transformer.sh")
        else:
            p = sp.getoutput("./transformer_low.sh")
    else:
        text = "<|startoftext|>" + text + " = "
        text_file.write(text)
        text_file.close()
        if (resource == "full"):
            p = sp.getoutput("./gpt2.sh")
        else:
            p = sp.getoutput("./gpt2_low.sh")

    output_file = open("output.txt","r")
    output = output_file.read()

    return output

if __name__ == '__main__':
    #app.run(port=8888)
    app.run(host='0.0.0.0', port=8888)
