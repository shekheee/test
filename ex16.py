from sys import argv

python_file, Old_file,New_file =argv

Old_file_open=open(Old_file,'r+')

New_file_open=open(New_file,'r')

w=Old_file_open.read()
print "Print 1st file content"
print w

New_file_open.write(w)

z=New_file_open.read()
print "2nd file content"
print z

Old_file_open.truncate()
y=Old_file_open.read()
print "!st file content",w
Old_file_open.close()

New_file_open.close()
