from bitstring import BitArray
class PrefixCodeTree:
  # init Trie class
  def __init__(self):
    self.root = self.createNode()

  def createNode(self, symbol = None, codeword = None):
      return {'isLeaf': True, 'left': dict(), 'right': dict(), 'symbol': symbol,"codeword": codeword}
  def insert(self, codeword, symbol):
    current = self.root
    c = ""
    for ch in codeword:
      c += str(ch)
      current["isLeaf"] = False
      if current["left"] != {} and str(current["left"]["codeword"]).startswith(c):  
        current = current["left"]
      elif current["right"] != {} and str(current["right"]["codeword"]).startswith(c): 
        current = current["right"]
      else: 
        s = symbol if c == self.code2str(codeword) else []
        node = self.createNode(s, c)
        if c[-1] == '0':
          current["left"] = node
        elif c[-1] == '1':
          current["right"] = node
        else: print ("error")
        current = node

  def code2str(self, codeword):
      s = ''
      for c in codeword:
        s+= str(c)
      return s
  def decode(self, byte, length):
    codestring = ''
    bitstring = BitArray(byte).bin
    i = 0
    n = self.root
    while i <= length:
        b = bitstring[i]
        if n["isLeaf"] == True:
            codestring += str(n["symbol"])
            n = self.root
        elif n["isLeaf"] == False:
            i = i+1
            if b == '0':
                n = n["left"]
            elif b == '1':
                n = n["right"]
            else:
                print ("errr")
        else :
            print("error")
    return codestring


  def printTree(self):
      print (str(self.root))
