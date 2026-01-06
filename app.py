
from flash import Flask

app = Flask(_name_)

@app.routr("/")
def hello():
    return "Hello from CI/CD Pipeline!"

if _name_ == "_main_"
    app.run(host="0.0.0.0", port=5000)
