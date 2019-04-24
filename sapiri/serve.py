from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<path:path>')
def path(path):
   return render_template('simple.html')

def main():
   app.run(debug=True)