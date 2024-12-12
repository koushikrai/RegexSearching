# Importing key functions to expose them at the package level
from .search import search_documents
from .analysis import measure_efficiency

# Optional: Metadata for the package
__all__ = ["search_documents", "measure_efficiency"]
