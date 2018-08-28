from flask import Flask, render_template, jsonify, request, url_for

# V1 notes 
# -------------------------------------------------
# No user personified experience.
# Purely made for Script Testing.

app = Flask(__name__)

@app.route('/test', methods = ['GET', 'POST'])
def checkResult():
    error = None
    if request.method == 'POST':
        print("\n\n\n", request.form)
        
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug = True)
