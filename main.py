# This is a sample Python script.
from flask import Flask
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Guys'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

