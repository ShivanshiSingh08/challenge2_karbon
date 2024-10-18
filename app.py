from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from model import analyze_financial_data

app = Flask(__name__)

# Route for page 1 (upload page)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Getting the uploaded file
        file = request.files['file']
        
        # Loading JSON data
        data = json.load(file)
        
        # Analyzing data using model.py
        results = analyze_financial_data(data)
        
        # Passing results to the results page
        return redirect(url_for('results', result=json.dumps(results)))

    return render_template('upload.html')

# Route for page 2 (results page)
@app.route('/results')
def results():
    # Getting the analysis results from query parameter
    results = json.loads(request.args.get('result'))
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
