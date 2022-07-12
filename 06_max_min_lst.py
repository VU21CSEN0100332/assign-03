# Concept : Dictionaries
# Find Max and Min Value in a dictionary

'''
You will be given a dictionary with a key-value pair

for each key "k" there will be a list [v1,v2,v3,v4] as value

your first task is to find the max and min of each list of each key

example

d1 = {"a":[20,30,10,1], "b":[10,100,1000,3], "c":[30,50,2,5]}

the max and min for "a" is 30 and 1
the max and min for "b" is 1000 and 3
the max and min for "c" is 50 and 2

You have to finally return the list of keys which is having the max and min value 

So for the above dictionary the list will be ["b", "a"] as [max,min] -> "b" having 1000 and "a" having 1

'''

import unittest

def find_max_min_dict(d1):
  mxmn_lst=[]
  dmax = dict()
  dmin = dict()
  for i in d1:
    dmax[i] = max(d1[i])
  for i in d1:
    dmin[i] = min(d1[i])
  maxi = dmax['a']
  mini = dmin['a']
  for i in dmax:
    if dmax[i] > maxi:
      maxi = dmax[i]
  for i in dmin:
    if dmin[i] < mini:
      mini = dmin[i]
  for i in d1:
    if maxi in d1[i]:
      mxmn_lst.append(i)
      break
  for i in d1:
    if mini in d1[i]:
      mxmn_lst.append(i)
      break
  return mxmn_lst

#DO NOT TOUCH THE BELOW CODE
class Max_(unittest.TestCase):
  def test_01(self):
    d1 = {"a":[20,30,60,1], "b":[1000,10,2,4], "c":[40,2000,3,5] }
    
    output = ["c","a"]
    
    self.assertEqual(find_max_min_dict(d1), output)

  def test_02(self):
    d1 = {"a":[2,300,6,100], "b":[10,90,89,4], "c":[40,2,3,5] }
    
    output = ["a","a"]
    
    self.assertEqual(find_max_min_dict(d1), output)

if __name__ == '__main__':
  unittest.main(verbosity=2)
