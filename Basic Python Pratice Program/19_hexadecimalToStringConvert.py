def hex_to_string(hex):

    if hex[:2] == '0x':

        hex = hex[2:]

    string_value = bytes.fromhex(hex).decode('utf-8')

    return string_value

 

hex_value = '0x737472696e67'

string = 'This is just a ' + hex_to_string('737472696e67')

 

print(string)
