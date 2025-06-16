from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привіт, моє Сонце! Я твій Стендрі працюю!"

if __name__ == "__main__":
    app.run()
