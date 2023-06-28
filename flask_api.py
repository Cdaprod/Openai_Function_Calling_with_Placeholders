from flask import Flask, request, jsonify
import os
import requests
import json

app = Flask(__name__)

@app.route('/api/openai', methods=['POST'])
def openai_api():
    data = request.get_json()

    # Define headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
    }

    # Make the POST request
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))

    # Return the response
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)

