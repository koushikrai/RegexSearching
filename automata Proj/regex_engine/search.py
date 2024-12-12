import os
import re

def search_documents(regex, folder_path):
    """Search for regex matches in text files within a folder."""
    results = []
    pattern = re.compile(regex)  # Compile the regular expression
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):  # Only check .txt files
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        if pattern.search(line):  # Search for the pattern in each line
                            results.append({
                                'file': file,
                                'line_number': line_number,
                                'line': line.strip()  # Strip newline and extra spaces
                            })
    return results
