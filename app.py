from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key='mysecretkey'

@app.route("/")
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    visit_count= session['counter']
    return render_template('index.html', visit_count=visit_count)

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/increment")
def increment():
    session["counter"] +=2
    return redirect("/")

@app.route("/reset")
def reset():
    session["counter"]=0
    return redirect("/")

@app.route("/costum_increment", methods=["POST"])
def costum_increment():
    increment_value=request.form.get("increment_value", type=int)
    if increment_value:
        session["counter"] += increment_value-1
        return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)