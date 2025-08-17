from flask import Flask,render_template, request, send_file,redirect
from edit import create_report

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():

    file_ready = False

    if request.method == 'POST':
        
        prompt = request.form['prompt']

        create_report(prompt)

        file_ready = True

        return send_file('/tmp/generated.docx',as_attachment=True,download_name='generated.docx')

    return render_template('generate.html',file_ready=file_ready)


if '__main__' == __name__:
    app.run()