from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html", title="Колонизация Марса")


@app.route('/training/<prof>')
def training(prof):
    return render_template("training.html", prof=prof)


@app.route('/list_prof/<prof_type>')
def list_prof(prof_type):
    return render_template("profs.html", type=prof_type)





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')