from flask import Flask ,render_template ,request

import model

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    abcd = model.top20()
    return render_template("index.html",mk=abcd.to_html())
if __name__ == '__main__':
    app.run(debug=True)
