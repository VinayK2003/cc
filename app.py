from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Route for the homepage.
    Displays the purpose of the experiment with HTML styling.
    """
    return """
    <html>
        <head>
            <title>CC-Lab Experiment 10</title>
        </head>
        <body style="background-color:#f9f9f9; text-align:center; padding-top:100px;">
            <h1 style="color:#4CAF50; font-size: 36px;">
                ✨ CC-Lab Experiment 10 ✨
            </h1>
            <p style="font-size: 24px; color:#333;">
                Implementing the Platform as a Service (PaaS) model
            </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
