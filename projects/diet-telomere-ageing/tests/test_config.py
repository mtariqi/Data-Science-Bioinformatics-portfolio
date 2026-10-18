from pathlib import Path
import unittest
import yaml

class ConfigTests(unittest.TestCase):
    def test_config_has_required_cycle_and_files(self):
        cfg = yaml.safe_load(Path("config/config.yaml").read_text())
        self.assertEqual(cfg["cycles"], ["1999-2000", "2001-2002"])
        self.assertTrue({"DEMO", "TELO"}.issubset(set(cfg["files"])))

if __name__ == "__main__":
    unittest.main()
