from flask import Flask

app = Flask(__name__)

print("Hello from app")


@app.get("/")
def get_home():
    return "home"


if __name__ == "__main__":
    app.run(debug=True)
