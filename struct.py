from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 10, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal (b'\x06\x00\x00\x00\n\x00\x00\x00)\\\x97@')
original_data = unpack('iif', packed_data)
print(original_data)

# another way of completing the above action
print(unpack('iif', b'\x06\x00\x00\x00\n\x00\x00\x00)\\\x97@'))
