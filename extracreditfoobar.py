f1 = open('foobar.txt', 'r')
input = f1.read()
print(input)
input = input.replace(',','\n')
print(input)
f2 = open('foobar.txt',"w+")
f2.write(input)
f1.close()
f2.close()