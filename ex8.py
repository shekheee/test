formatter="%r %r %r %r"

print formatter %(1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (True,True,False,True)

print formatter % ("I can't do it","I can do it", "Here I am the only one","Fuck'em all")
