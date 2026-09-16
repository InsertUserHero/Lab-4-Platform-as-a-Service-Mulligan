```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <html>
            <head>
                <title>MSOE Microservices</title>
            </head>
            <body>
                <h1>Hello MSOE!</h1>
                <p>Welcome to my Flask Microservice.</p>

                <h2>Available Pages</h2>
                <ul>
                    <li><a href="/about">About</a></li>
                    <li><a href="/student">Student</a></li>
                    <li><a href="/status">Status</a></li>
                </ul>
            </body>
        </html>
    '''


@app.route('/about')
def about():
    return '''
        <h1>About This App</h1>
        <p>This is a simple Flask microservice.</p>
        <p>It was created using Python and Flask.</p>
        <a href="/">Back Home</a>
    '''


@app.route('/student')
def student():
    return '''
        <h1>MSOE Student</h1>
        <p>Welcome to the MSOE Microservices application!</p>
        <p>This application demonstrates Flask routing.</p>
        <a href="/">Back Home</a>
    '''


@app.route('/status')
def status():
    return '''
        <h1>Application Status</h1>
        <p>Application: MSOE Microservices</p>
        <p>Status: Running</p>
        <p>Framework: Flask</p>
        <a href="/">Back Home</a>
    '''


if __name__ == "__main__":
    app.run(debug=True)

