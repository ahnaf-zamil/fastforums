import nox


@nox.session(reuse_venv=True)
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("pytest")


@nox.session(reuse_venv=True)
def formatting(session):
    session.install("black")
    session.run("black", "./")


@nox.session(reuse_venv=True)
def linting(session):
    session.install("flake8")
    session.run(
        "flake8",
        "--statistics",
        "--show-source",
        "--benchmark",
        "--tee",
        "./app",
        "./tests",
    )
