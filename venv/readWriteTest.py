import pickle

"""Basic program for writing and reading data to a text file, then to a binary file.
Overrides anything already in the file, and obviously creates the file, if it doesn't exist
"""

# Test data to write to text file and binary file
dioSongs = ["Invisible", "Stargazer", "Straight through the heart", "Holy Diver", "Caught in the Middle"]
evenNumbers = set(range(0, 50, 2))
oddNumbers = set(range(1, 50, 2))

# Writes the sample data to a text file and reads it back afterwards
with open(r'testFile.txt', 'w+', encoding="utf8") as myFile:
    for songs in dioSongs:
        myFile.write(songs + '\n')

    print('Even numbers: {}'.format(evenNumbers), file=myFile)
    print('Odd numbers: {}'.format(oddNumbers), file=myFile)

    myFile.seek(0)
    fileData = myFile.read()
    print(fileData)

# Writes the sample data to a binary file
with open("binaryData.pickle", "wb") as myBinaryFile:
    pickle.dump(dioSongs, myBinaryFile)
    pickle.dump(evenNumbers, myBinaryFile)
    pickle.dump(oddNumbers, myBinaryFile)

# Reads the sample data from a binary file (using pickle module)
with open("binaryData.pickle", "rb") as myBinaryFile:
    songs = pickle.load(myBinaryFile)
    eveNums = pickle.load(myBinaryFile)
    oddNums = pickle.load(myBinaryFile)

print(songs)
print(eveNums)
print(oddNums)

