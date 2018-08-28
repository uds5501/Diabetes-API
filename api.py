from flask import Flask, render_template, jsonify, request, url_for
from DataPreps import PreProcess
# V1 notes 
# -------------------------------------------------
# No user personified experience.
# Purely made for Script Testing.

app = Flask(__name__)

@app.route('/test', methods = ['GET', 'POST'])
def checkResult():
    error = None
    if request.method == 'POST':
        content = dict(request.form)
        
        input_dict = {}

        for i in content.keys():
            input_dict[i] = float(content[i][0])
            
        
        #print("\n\n\n", content)
        print("\nProcessed Content is : ", input_dict)
        result = PreProcess(input_dict)
        print("\nResult is : ", result)
        return jsonify(result)

    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug = True)
