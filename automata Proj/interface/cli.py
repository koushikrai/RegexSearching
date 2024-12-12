from regex_engine.search import search_documents
from utils.file_io import save_results
from utils.metrics import measure_execution_time, count_matches

def run_cli():
    regex = input("Enter a regular expression: ")
    folder_path = input("Enter the folder path containing documents: ")
    case_insensitive = input("Case-insensitive search? (yes/no): ").lower() == "yes"
    # Measure execution time
    execution_time, results = measure_execution_time(search_documents, regex, folder_path)

    print("\nSearch Results:")
    for result in results:
        print(f"File: {result['file']}, Line: {result['line_number']}, Content: {result['line']}")

    # Count matches and display metrics
    total_matches = count_matches(results)
    print(f"\nTotal Matches Found: {total_matches}")
    print(f"Execution Time: {execution_time:.2f} seconds")

    # Save results
    save = input("Do you want to save the results to a file? (yes/no): ").lower()
    if save == "yes":
        save_results(results, "results.txt")