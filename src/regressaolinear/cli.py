"""Console script for regressaolinear."""
import regressaolinear

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for regressaolinear."""
    console.print("Replace this message by putting your code into "
               "regressaolinear.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
