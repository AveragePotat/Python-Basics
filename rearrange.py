"""
# TITLE: Edge Case example

# Created by: Kena D
# Created on: 2025-02-18
# Last editted on: 2025-02-18

"""

#========================================================

#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
  if result is None:
    return name # changed from empty variable ""
  return "{} {}".format(result[2], result[1])

def test_empty(self):
  testcase = ""
  expected = ""
  self.assertEqual(rearrange_name(testcase), expected)
  
  # Use ./rearrange_test.py in linux to test