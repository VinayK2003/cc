from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "CC-Lab Experiment-10 . Implementing service model of Platform as a Service"

if __name__ == '__main__':
    app.run()
