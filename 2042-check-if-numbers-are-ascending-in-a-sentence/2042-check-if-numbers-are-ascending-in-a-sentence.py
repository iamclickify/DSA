class Solution:
  def areNumbersAscending(self, s: str) -> bool:
    prev_num = 0  # All numbers in s are strictly positive (>= 1)

    for character in s.split():
      if character.isdigit():
        curr_num = int(character)
        if curr_num <= prev_num:
          return False
        prev_num = curr_num

    return True
