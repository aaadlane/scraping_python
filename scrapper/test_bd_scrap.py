import unittest
from bd_scrap import *

mybd = Table_articles()
table = "articles"
database = "my_db_scrap"



class MyTestCase(unittest.TestCase):
    def testCreateTable(self):
        self.assertTrue(isinstance(mybd, Table_articles))

if __name__ == '__main__':
    unittest.main()