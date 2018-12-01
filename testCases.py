import numpy.testing as npt
from poi import find_Target
import unittest

class TestStringMethods(unittest.TestCase):

   def test_find_POI_Single(self):
      # checks that actual (x,y,r) are all within 15 of the expected (x,y,r)
      # 15 = abs(desired-actual) < 1.5 * 10**(-decimal), decimal = -1 
      npt.assert_almost_equal(find_Target("poiTestImages/target1.jpg"), [383, 153, 17], -1)
      npt.assert_almost_equal(find_Target("poiTestImages/target2.jpg"), [443, 341,  29], -1)
      npt.assert_almost_equal(find_Target("poiTestImages/target3.jpg"), [371,  97,  13], -1)

   def test_find_POI_None(self):
      self.assertEqual(find_Target("poiTestImages/noTarget.jpg"), [])
      self.assertEqual(find_Target("poiTestImages/noTarget2.jpg"), [])
      self.assertEqual(find_Target("poiTestImages/noTarget3.jpg"), [])

   def test_find_POI_Multiple(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
         s.split(2)

if __name__ == "__main__":
   unittest.main()
   #run test cases with ball

   #run no ball

   #run part ball


