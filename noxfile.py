import nox
import datetime

nox.options.sessions = ["css", "generate", "serve"]


@nox.session
def css(session):
    session.run(
        "npx",
        "tailwindcss",
        "-i",
        "./input.css",
        "-o",
        "./assets/output.css",
        external=True,
    )


@nox.session
def generate(session):
    session.install("staticjinja")
    session.log("Building pages")
    session.run("python", "build.py")
    session.log("Copying static files")
    session.run("cp", "-r", "assets", "output/", external=True)


@nox.session
def serve(session):
    session.run("python", "-m", "http.server", "--directory", "output")


@nox.session
def publish(session):
    session.install("ghp-import")
    session.run(
        "ghp-import",
        "-b",
        "gh-pages",
        "-m",
        f"Publish site on {datetime.date.today().isoformat()}",
        "output",
    )
