from flask import Flask ,render_template ,request

import model

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    if request.method=="POST":
        abcd = model.top20()
        abc = abcd
        render_template("index.html",mk=abc.to_html())
    return "themk"
if __name__ == '__main__':
    app.run(debug=True)
