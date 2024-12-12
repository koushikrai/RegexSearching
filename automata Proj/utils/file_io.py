import os

def save_results(results, save_path):
    """Save the search results to a specified file."""
    with open(save_path, "w") as f:
        for result in results:
            f.write(f"File: {result['file']}, Line: {result['line_number']}, Content: {result['line']}\n")
    print(f"Results saved to {save_path}")

def list_files_in_folder(folder_path, file_extension=".txt"):
    """List all files with a specific extension in a folder."""
    return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(file_extension)]
