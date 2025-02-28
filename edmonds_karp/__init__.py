# Import the EdmondsKarp class from the algorithm module within the same package
from .algorithm import EdmondsKarp
# Define the public API for the package, allowing only EdmondsKarp to be imported with 'from edmonds_karp import *'
__all__ = ["EdmondsKarp"]