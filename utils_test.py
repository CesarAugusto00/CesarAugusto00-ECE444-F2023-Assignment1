import unittest 
from utilsClass import utils

class testUtils(unittest.TestCase):
  def test_reverse(self):
    y = utils
    self.assertEqual(y.reversed(1234), 4321)
    self.assertEqual(y.reversed(789.14), 41.987)
    self.assertEqual(y.reversed("Hello"), "elloH")

def test_formatter(self):
  z = utils
  a, b = z.formatter(4)
  self.assertEqual(a, "0b100" )
  self.assertEqual(b, "0o4")

  #Considering the asci representation of each character and then taking that ascii and convert it in binary of 1byte
  a, b = z.formatter("hello")
  self.assertEqual(a, "0b100100001100101011011000110110001101111" )
  #Same in case of octal but making it a octal containing 3 parts
  self.assertEqual(b, "0o150145154154157")

  a, b = z.formatter(7.5)
  self.assertEqual(a, "0b111" )
  self.assertEqual(b, "0o10.4")

if __name__ == '__main__':
  unittest.main()
