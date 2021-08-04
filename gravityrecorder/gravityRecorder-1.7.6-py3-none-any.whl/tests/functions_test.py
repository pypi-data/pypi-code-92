import unittest
from gravityRecorder import functions
from gravityRecorder.tests import test_objects


class FunctionsTest(unittest.TestCase):
    def test_get_next_id(self):
        response = functions.get_next_id(test_objects.test_sqlshell)
        print("NEXT ID:", response)

    def test_current_id(self):
        response = functions.get_current_id(test_objects.test_sqlshell, 1274)
        print("UNFINISHED ID:", response)

    def test_get_tc_id(self):
        response = functions.get_local_trash_cat_id(test_objects.test_sqlshell,
                                                    1)
        self.assertEqual(response, 1)

if __name__ == '__main__':
    unittest.main()
