"""
# TITLE: Try-Except Concept

# Created by: Kena D
# Created on: 2025-02-18
# Last editted on: 2025-02-18

"""

#========================================================

#!/usr/bin/env python3

#!/usr/bin/env python3

def character_frequency(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Now process the file
  characters = {}
  for line in f:
    for char in line:
      characters[char] = characters.get(char, 0) + 1
  f.close() 
  return characters