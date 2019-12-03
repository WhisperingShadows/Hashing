# not gonna comment this much because I'm tired as hell

# multiplication function 
def c_mulg(a, b):
  return eval(hex((a * b) & (2**64 - 1))[:-1])

# hash implemented as a function
def hash64(self):
  if not self:
    return 0 # empty
  value = ord(self[0]) << 7
  for char in self:
    value = c_mulg(1000003, value) ^ ord(char)
  value = value ^ len(self)
  if value == -1:
    value = -2
  if value >= 2**63:
    value -= 2**64
  return value



# another multiplication function 
def c_mul(a, b):
    return eval(hex((a * b) & 2**32 - 1)[:-1])

# hash implemented as a class method
class string:
    def __hash__(self):
        if not self:
            return 0 # empty
        value = ord(self[0]) << 7
        for char in self:
            value = c_mul(1000003, value) ^ ord(char)
        value = value ^ len(self)
        if value == -1:
            value = -2
        return value

# runs above hashing functions and native python hash()
def getHashin(val):
    print(hash64(val))

    print(string.__hash__(val))

    print(hash(val))

getHashin("hewwo")

