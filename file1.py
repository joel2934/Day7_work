'''
file = open('student.txt','r')
data = file.read()
print(data)
file.close()

'''


file = open('student.txt','a+')
file.write("A new line of text added to the file.")
file.seek(0)
data = file.read()
print(data)
file.close()


'''
file=open('student.txt','r')
data=file.read()
print(data)
file.close()

'''
