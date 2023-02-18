import unittest
import typewise_alert as ta
import typewise_constants as tc


class TypewiseTest(unittest.TestCase):

  def test_check_and_alert(self):
    for coolingType in tc.COOLING_TYPE:
        for alertTarget in tc.ALERT_TARGET:
          self.assertTrue(
            ta.check_and_alert(
              alertTarget,
              {'coolingType': coolingType},
              80
            ) == 'TOO_HIGH'
          )
          self.assertTrue(
            ta.check_and_alert(
              alertTarget,
              {'coolingType': coolingType},
              -1
            ) == 'TOO_LOW'
          )
          self.assertTrue(
            ta.check_and_alert(
              alertTarget,
              {'coolingType': coolingType},
              20
            ) == 'NORMAL'
          )


if __name__ == '__main__':
  unittest.main()
