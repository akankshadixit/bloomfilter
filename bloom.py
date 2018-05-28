import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):
   def __init__(self, error, entries):
       self.error = error
       self.entries = entries

      #Optimal number of bits is:
      # bits = (entries * ln(error)) / ln(2)^2
      #Optimal number of hash functions is:
      # hashes = frac * ln(2)

       num = math.log(self.error)
       denom = math.pow(math.log(2), 2)             # ln(2)^2
       frac = -(num/denom)
       self.bits = int(math.ceil(self.entries * frac))
       self.hash = int(math.ceil(frac * math.log(2)))
       self.array = bitarray(self.bits)
       self.array.setall(0)
       

   def add(self, element):
       index = []

       for i in range(self.hash):
          digest = mmh3.hash(element,i) % self.bits
          index.append(digest)
          self.array[digest] = True

   def check(self, element):
       for i in range(self.hash):
          digest = mmh3.hash(element,i) % self.bits
          if(self.array[digest]) == False:
             return False
       return True

          
