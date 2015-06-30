import unittest
from structures import Building
from GLOBS import RESOURCES, BUILDING_NAMES

VALID = {"name": BUILDING_NAMES[0],
        "level": 2,
        "cost": {r:100 for r in RESOURCES},
        "increment": 1.3}

class TestBuildingInit(unittest.TestCase):
    """Test the creation of a building"""

    @classmethod
    def setUpClass(self):
        """Check the VALID global variable upon which many other tests rely"""
        b = Building(**VALID)

    def test_valid_init(self):
        """Test some valid init compositions"""
        Bs = []
        costs = {r:100 for r in RESOURCES}
        valid = VALID.copy()
        Bs.append(Building(**valid))
        valid["name"] = BUILDING_NAMES[1]
        Bs.append(Building(**valid))
        valid["level"] = 30
        Bs.append(Building(**valid))
        valid["cost"][RESOURCES[0]] = 300
        Bs.append(Building(**valid))
        valid["increment"] = 1.5
        Bs.append(Building(**valid))

        for b in Bs:
            self.assertIsInstance(b, Building)

    def test_init_name(self):
        """Test the 'name' attribute error checking"""
        valid = VALID.copy()
        for name in BUILDING_NAMES:
            valid["name"] = name
            self.assertIsInstance(Building(**valid), Building)

        bad_type_names = [23, 3.4, (43, 234), ["HQ", "HQ"]]
        not_valid = VALID.copy()
        for bad_name in bad_type_names:
            not_valid["name"] = bad_name
            self.assertRaises(TypeError, Building, **not_valid)

        bad_value_names = ["", "hq", "banana", "fuckmylife", "420blazeit"]
        for bad_name in bad_value_names:
            not_valid["name"] = bad_name
            self.assertRaises(ValueError, Building, **not_valid)

        not_valid["name"] = valid["name"]
        self.assertEqual(not_valid, valid)

if __name__ == "__main__":
    unittest.main()
