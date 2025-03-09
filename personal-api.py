from flask import Flask

app =Flask(_name_)

@app.route("/")
def name():
    return "iyappan "


@app.route("/registerNumber")
def register_number():
    return "22IT013"

@app.route("/department")
def department():
    return "IT(Information Technology)"

if _name_ == "_main_":
    app.run(debug=True)
