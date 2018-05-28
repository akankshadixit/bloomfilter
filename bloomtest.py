from bloom import BloomFilter
from random import shuffle

error = 0.1
entries = 10

bloom_obj = BloomFilter(error, entries)

print("Size of vector array is:{}".format(bloom_obj.bits))
print("Optimal number of Hash Functions:{}\n".format(bloom_obj.hash))
    

# words to be added
word_present = ['abound','abounds','abundance','abundant','accessable',
                'bloom','blossom','bolster','bonny','bonus','bonuses']
 
# word not added
word_absent = ['bluff','cheater','hate','war','humanity',
               'racism','hurt','nuke','gloomy','facebook']
 
for item in word_present:
    bloom_obj.add(item)
 
shuffle(word_present)
shuffle(word_absent)
 
test_words = word_present[:10] + word_absent
shuffle(test_words)
for word in test_words:
    if bloom_obj.check(word):
        if word in word_absent:
            print("'{}' is a false positive!".format(word))
        else:
            print("'{}' is probably present!".format(word))
    else:
        print("'{}' is definitely not present!".format(word))


