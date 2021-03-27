from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return {
            'userID': 3,
            'title': 'The App',
            'state': "in progress"
        }
        
if __name__ == '__main__':
    app.run()
