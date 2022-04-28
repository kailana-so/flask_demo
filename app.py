from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

#The if __name__ == "__main__": part is important, so it doesn't clash with the app.run in wsgi.py later.

if __name__ == "__main__":
    app.run(debug=True)
