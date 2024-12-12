from interface.cli import run_cli
from interface.gui import run_gui
from interface.web import app  # If using Flask for the web interface

if __name__ == "__main__":
    choice = input("Choose interface (1: CLI, 2: GUI, 3: Web): ")
    if choice == "1":
        
        run_cli()
    elif choice == "2":
        run_gui()
    elif choice == "3":
        app.run(debug=True)
    else:
        print("Invalid choice!")
