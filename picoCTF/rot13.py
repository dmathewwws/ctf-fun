from __future__ import print_function

def rotify(input):
  for char in input:
    if char.isalpha():
      if char.isupper():
        rot = ord(char) + 13
        if rot > ord('Z'):
          rot = rot - 26
      else:
        rot = ord(char) + 13
        if rot > ord('z'):
          rot = rot - 26
      print(chr(rot), end=""),
    else:
      print(char, end=""),

rotify("NOPQRSTUVWXYZ")