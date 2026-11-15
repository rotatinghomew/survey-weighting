import json
import unittest
from pathlib import Path

class ProjectContractTest(unittest.TestCase):
    def test_synthetic_context_is_readable(self):
        sample = json.loads((Path(__file__).parents[1] / "data" / "sample.json").read_text(encoding="utf-8"))
        self.assertEqual(sample["kind"], "survey-weighting-lab")
        self.assertGreaterEqual(len(sample["rows"]), 3)

if __name__ == "__main__":
    unittest.main()
