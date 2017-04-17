from sys import argv

script, filename=argv
txt=open(filename)
print ("Here's the content of your file"),filename
print txt.read()
txt.close()
read_txt=raw_input("Now again type filename :")
new_txt=open(read_txt)
print("Content of file are:")
print new_txt.read()
new_txt.close() 
