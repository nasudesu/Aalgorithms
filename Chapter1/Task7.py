def custom_encoder(string):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    indexes = []
    for char in string:
        indexes.append(reference_string.find(char.lower()))
    return indexes


print(custom_encoder('My house is beautiful'))