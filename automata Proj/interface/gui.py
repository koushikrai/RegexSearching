import tkinter as tk
from tkinter import filedialog, scrolledtext
from regex_engine.search import search_documents

def save_results(results):
    """Save results to a file."""
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if save_path:
        with open(save_path, "w") as f:
            for result in results:
                f.write(f"File: {result['file']}, Line: {result['line_number']}, Content: {result['line']}\n")
        print(f"Results saved to {save_path}")

def run_gui():
    def search_action():
        # Get the regex and folder path from the user input
        regex = regex_input.get()
        folder = folder_path.get()
        case_insensitive = case_insensitive_var.get()
        
        # If case insensitive search is selected, add the (?i) flag to the regex
        if case_insensitive:
            regex = f"(?i){regex}"

        # Perform the search using the regex and folder path
        results = search_documents(regex, folder)

        # Clear the output window before displaying new results
        output.delete(1.0, tk.END)

        # Display the individual results in the output
        for res in results:
            output.insert(tk.END, f"File: {res['file']}, Line: {res['line_number']}, Content: {res['line']}\n")

        # Display the total number of matches
        total_matches = len(results)
        output.insert(tk.END, f"\nTotal Matches Found: {total_matches}\n")

        # Update the Save button to allow saving the results
        save_button.config(command=lambda: save_results(results))

    # Initialize the main window
    root = tk.Tk()
    root.title("Regex Search Engine")

    # Create and pack the widgets for user input
    tk.Label(root, text="Regex:").pack()
    regex_input = tk.Entry(root, width=50)
    regex_input.pack()

    tk.Label(root, text="Folder Path:").pack()
    folder_path = tk.Entry(root, width=50)
    folder_path.pack()

    case_insensitive_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Case Insensitive", variable=case_insensitive_var).pack()

    search_button = tk.Button(root, text="Search", command=search_action)
    search_button.pack()

    save_button = tk.Button(root, text="Save Results")
    save_button.pack()

    output = scrolledtext.ScrolledText(root, width=60, height=20)
    output.pack()

    root.mainloop()
