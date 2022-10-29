import sys
import typer

app = typer.Typer()

@app.command()
def gui():
    from smallapp.gui import start
    start()

def main():
    if len(sys.argv) == 1:
        gui()
    else:
        app()

if __name__ == "__main__":
    main()
