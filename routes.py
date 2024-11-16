#rotas

from main import app

@app.route("/")   ## define a homepage
def homepage():
    return "Meu primeiro site com flask! :)"


@app.route("/blog")
def homepage():
    return "outra pagina"