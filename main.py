from flask_api import FlaskAPI

app = FlaskAPI(__name__)

kkjj = ":o"

@app.route('/teste')
def teste():
    return {
        "corno": "%s" %kkjj
    }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')