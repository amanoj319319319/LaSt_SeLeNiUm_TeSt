'''
# unicode string
string = 'india'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)
'''

'''
str_original = input('Please enter string data:\n')

bytes_encoded = str_original.encode()

str_decoded = bytes_encoded.decode()

print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)
print('str_original equals str_decoded =', str_original == str_decoded)
'''

str_original = input('Please enter string data:\n')

bytes_encoded = str_original.encode()

str_decoded = bytes_encoded.decode()

print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)
print('str_original equals str_decoded =', str_original == str_decoded)