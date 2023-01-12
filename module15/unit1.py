myFile = open('namefile.txt', 'w')
myFile.write('new text')
print('print new text', file=myFile)