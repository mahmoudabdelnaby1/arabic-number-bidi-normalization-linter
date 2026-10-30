import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from bidi_linter import normalize_bidi_text

class TestBiDi(unittest.TestCase):
    def test_norm(self):
        t = "خصم ٢٠% على العطور"
        res = normalize_bidi_text(t)
        self.assertIn("20", res)

if __name__ == "__main__":
    unittest.main()
