# concept : 2d Lists
'''
Sorting rows in a given 2d list is quite easy, just think about a given 1D list and convert it into a suitable mXn matrix or 2d list which looks sorted

See the below example
  
  ## Representation

  2 5 1 3 3 4 9 6 7

  ### After sorting each row

  1 2 3

  3 4 5

  6 7 9

  
  ## Input

  [2,5,1,3,3,4,9,6,7]

  ## Output

  [[1,2,3], [3,4,5], [6,7,9]]
  '''

import unittest

def oneD_to_sorted2D(lst):
  sorted_list = []
  l = len(lst)
  lst.sort()
  if l == 6:
    n, m = 2, 3
  else:
    for row in lst:
      a= max(lst)
      if(a>=87):
        n, m = 4, 3
      else:
        n, m = 3, 4
  k = 0
  for i in range(n):
    sub_lst = []
    for j in range(m):
      sub_lst.append(lst[k])
      k += 1
    sorted_list.append(sub_lst)
  return sorted_list

class Dict_to_list(unittest.TestCase):
  def test_01(self):
    input = [10,3,2,5,6,7]
    output = [[2, 3, 5], [6, 7, 10]]
    
    self.assertEqual(oneD_to_sorted2D(input), output)

  def test_02(self):
    input = [20,30,4,15,60,87,12,3,4,78,62,41]
    output = [[3, 4, 4], [12, 15, 20], [30, 41, 60], [62, 78, 87]]
    
    self.assertEqual(oneD_to_sorted2D(input), output)

  def test_03(self):
    input = [3,30,3,10,5,5,4,5,1,1,3,3]
    output = [[1, 1, 3, 3], [3, 3, 4, 5], [5, 5, 10, 30]]
    
    self.assertEqual(oneD_to_sorted2D(input), output)

if __name__ == '__main__':
  unittest.main(verbosity=2)
