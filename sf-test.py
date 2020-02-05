import unittest
from superfresh import SuperFresh

class SuperTest(unittest.TestCase):
  def setUp(self):
    self.sf = SuperFresh(True)
  def test_NonUpperTest(self):
    self.assertEqual('Upper',self.sf.myStr('Upper',False))
  def test_UpperTest(self):
      self.assertEqual('UPPER',self.sf.myStr('Upper',True))
  def test_PreservedTest(self):
      self.assertEqual('lower',self.sf.myStr('lower',False))
      self.assertEqual('UPPER',self.sf.myStr('UPPER',True))
  def test_PrintTest(self):
      self.assertEqual('my String',self.sf.myStr('my String'))
      self.assertEqual('self.String is: \'my String\'',self.sf.myPrint('my String'))
    

unittest.main()