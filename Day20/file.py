with open('names.txt', 'r') as reader:
    # print(reader.read(5))
    # print(reader.readline(5))
    
    # read the file as a list
    # print(reader.readlines())

    # iterate over each line
    # line = reader.readline()
    # while line != '':
    #     print(line, end='')
    #     line = reader.readline
   breeds = reader.readlines()

with open('breeds_reversed.txt', 'w') as writer:
    for breed in reversed(breeds):
        writer.write(breed)
