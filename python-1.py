from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data
with open('index.json') as json_file:
    data = json.load(json_file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/developers')
def developers():
    # Get the search query parameters
    search_name = request.args.get('name', '')
    search_designation = request.args.get('designation', '')

    filtered_developers = []

    # Filter developers by name and designation
    for developer in data:
        if search_name.lower() in developer['name'].lower() and \
                search_designation.lower() in developer['designation'].lower():
            filtered_developers.append(developer)

    return jsonify(filtered_developers)


if __name__ == '__main__':
    app.run(debug=True)
