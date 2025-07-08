import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
import main


def test_main_version():
    assert main._version == "0.0.1"
