from quart import Quart, render_template, redirect


app = Quart(__name__)


@app.route("/", methods=["GET", "POST"])
async def index():
    return await render_template("index.html")


@app.errorhandler(404)
async def page_not_found(e):
    return redirect("/")
