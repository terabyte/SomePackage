''' test init module for somepackage '''
# implement a basic test under somepackage.tests
#pylint: disable=W0406
import unittest

class TestSomething(unittest.TestCase):
    ''' Example test class '''
    def test_something_else(self):
        ''' first test '''
        self.assertEqual(True, True)

def get_suite():
    "Return a unittest.TestSuite."
    import somepackage.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite

