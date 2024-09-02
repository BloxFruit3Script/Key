from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/')
def mboost():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"result": "No URL provided."})
    
    try:
        response = requests.get(url)
        html_content = response.text
    except requests.RequestException as e:
        return jsonify({"result": f"{str(e)}"})
    
    targeturl_regex = r'"targeturl":\s*"(.*?)"'
    
    match = re.search(targeturl_regex, html_content, re.MULTILINE)
    
    if match and len(match.groups()) > 0:
        result = match.group(1)
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Please try again later"})

if __name__ == '__main__':
    app.run(debug=True)