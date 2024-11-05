import sys
import os
import pytest

# Insert 'src' at the start of the system path
sys.path.insert(0, os.path.abspath("src"))

# Run pytest
pytest.main()
