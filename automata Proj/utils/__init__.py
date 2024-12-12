# Import functions to expose them at the package level
from .file_io import save_results, list_files_in_folder
from .metrics import measure_execution_time, count_matches

# Optionally, use __all__ to specify which functions should be exposed when importing *
__all__ = ["save_results", "list_files_in_folder", "measure_execution_time", "count_matches"]
