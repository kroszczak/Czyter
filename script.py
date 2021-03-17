from flask import Flask, render_template, request, url_for, send_from_directory
# from flask_pymongo import PyMongo
import pdftotext
import re
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

@app.route("/")
def index():
   return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
   file = request.files['file']
   rsrcmgr = PDFResourceManager()
   retstr = io.StringIO()
   device = TextConverter(rsrcmgr, retstr, codec = 'utf-8')
   interpreter = PDFPageInterpreter(rsrcmgr, device)
   pagenos = set()
   for page in PDFPage.get_pages(file.stream, pagenos, check_extractable=True):
        interpreter.process_page(page)
   text = retstr.getvalue()

   device.close()
   retstr.close()
   # mongo.db.files.insert({
   #    'name': file.filename,
   #    'content': text,
   #    })
   
   return render_template("index.html",result = text)

if __name__ == "__main__":
    app.run(debug=True)
    
