# IPv4 Address lookup, longest prefix
# KTH, EP1100
import ipaddress
import random

class TrieNode: 
    # Trie node class 
    def __init__(self, port=None): 
        self.children = [None]*2
        self.port = port
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
    # table is a pre-defined list with tuples containing ip address and ports
    # + no error check, aggregate will just crash instead
    def __init__(self, table=None): 
        self.root = self.getNode("0") 

        # if a node does not exist for address then go to latest port
        # root node has the default route = "0"
        # TODO: implement aggregation
        #if table is not None:
        #    self.aggregate(table)
  
    def getNode(self,port=None): 
        # Returns new trie node (initialized to NULLs) 
        return TrieNode(port) 
  
    # convert number to index.
    # ONLY use 0 or 1!!
    # private helper function
    def _charToIndex(self,ch): 
        return int(ch)
  
    '''
    # table = [(ip,port),...], ip and port are string values
    # returns new list with aggregated ips: [(aggrip, port),...]
    def aggregate(self, table):
        #1: find addresses with same port
        #2: see how many significant bits are equal
        #3 replace addresses w/ matching most sig bits (and the port ofc)

        portlist = {} # saves indices for ports
        #separate ips by port
        for tup in table
            ip = self.iptobit(tup[0]) # binary number as str
            po = tup[1]
            if not portlist[po]:
                portlist[po] = []
            portlist[po].append(ip)

        mlen = 0 #matching length
        for p,ips in portlist.items():
            b = 0 # bitindex
            match = True

            minlen = 32
            ipRef = ips[0]
            clen = 0
            # TODO: remove first iteration as ipRef is oip
            # TODO: less shitty var names
            for oip in ips:
                clen = 0
                for bidx, bit in enumerate(oip)
                    if ipRef[bidx] != bit:
                        # NOT A MATCH!!
                        if clen < minlen:
                            minlen = clen
                        break
                     clen+=1
                     if clen < minlen:
                        minlen = clen
                        # clen is reset in new iteration
            # we have the number of matched bits:
            #aggrip = ipRef AND subnetmast(minlen) 

            while match and i < len(ips):
                nummat = 0
                for j in range(ips)
                    if ipa[j] != ipb[i]:
                        match = False
                        break
                    nummat+=1
    '''                    

    def insert(self,key,port=None): 
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 

        for level in range(length): 
            index = self._charToIndex(key[level]) 
            # if current character is not present create empty node
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 

            # update port if parameter not None
            if level == (length-1) and port is not None:
                pCrawl.port = port
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True
  
    def search(self, key): 
        # Search key in the trie 
        # Returns port if key present
        # in trie otherwise the latest traversed port
        pCrawl = self.root 
        latestPort = pCrawl.port
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return latestPort
            pCrawl = pCrawl.children[index] 
            if pCrawl.port is not None:
                latestPort = pCrawl.port
        return latestPort #pCrawl != None and pCrawl.isEndOfWord 

    # ipaddr a string, e.g 192.168.1.1
    # to a string of bits, e.g "1010101....."
    def iptobit(self,ipaddr):
        return str(bin(int(ipaddress.IPv4Address(ipaddr))))[2:] 

    def searchIP(self, ipaddr):
        # ip address string, e.g 192.168.1.1
        # convert to string with binary num
        bkey = self.iptobit(ipaddr) 
        return self.search(bkey)
 
# driver function 
def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    # remember that we need: len(key) == len(ports)
    keys = ["0","1","00","01","10"]
    ports = ["A","B",None,"C",None]
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    l = len(keys)
    for i in range(l): 
        t.insert(keys[i],ports[i]) 

    # generate random ip:
    randIpDec = ""   
    i = 0
    for i in range(32):
        num = random.randint(0,1)
        randIpDec += str(num)
        i+=1

  
    # Search for different keys 
    print("in:{} ---- out:{} -- answ=A".format("0",t.search("0"))) 
    print("in:{} ---- out:{} -- answ=B".format("1",t.search("1"))) 
    print("in:{} ---- out:{} -- answ=A".format("00",t.search("00"))) 
    print("in:{} ---- out:{} -- answ=C".format("01",t.search("01"))) 
    print("in:{} ---- out:{} -- answ=B".format("10",t.search("10"))) 
    print("in:{} ---- out:{} -- answ=B".format("11",t.search("11"))) 
    print("----------------------")
    print("in:{} ---- out:{} -- answ=B".format("192.168.1.1 in binary 11*",
        t.searchIP("192.168.1.1"))) 
    # test random ip
    print("random IP in BINARY: {}".format(randIpDec))
    print("in:{} ---- out:{} -- answ=check".format(randIpDec,
        t.search(randIpDec))) 
  
if __name__ == '__main__': 
    main() 
  

