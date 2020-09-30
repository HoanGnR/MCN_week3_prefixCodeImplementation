from prefixcodetree import *
codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}
codeTree = PrefixCodeTree() # create a prefix code tree `codeTree`
# Initialize codeTree with codebook
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
#print (n)
#print(str(codeTree.findNode(n,0)))
message = codeTree.decode(b'\xd2\x9f\x20', 21)
print (message)
# Below is explaination:
# data = b'\xd2\x9f\x20' --> 24 bit
# datalen = 21 --> use only 21 bit, 3 remaining bits are not used
#
# Decoded data should be :
#
# 11 0 100 10|1 0 0 11 11 1|00 100 000
# x4 x1 x2 x3 x1 x1 x4 x4 x2 x2
