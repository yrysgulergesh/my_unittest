import unittest
from test import full_name

class NameTestCase(unittest.TestCase):
    """Тесты для full_name.py"""

    def test_first_last_name(self):
        """Имена вида 'Yrysgul Ergesh' работают нормально?"""
        format_name = full_name('Yrysgul', 'Ergesh')
        self.assertEqual(format_name, 'Yrysgul Ergesh')

    def test_first_last_middle(self):
        """Имена вида 'Yrysgul Ergesh Ergeshovna' работают нормально?"""
        format_name = full_name('Yrysgul', 'Ergesh', 'Ergeshovna')
        self.assertEqual(format_name, 'Yrysgul Ergesh Ergeshovna')
    
unittest.main()


# if __name__ == "__name__":
#     unittest.main()