#string handling and manupulation
#\n is new line and \t is tab
d ='aman\n raman\n shaman\t\thest'
print (d)
#triple quotes are usedd to 
r ="""aman raman, 
shaman ,
ghhjh hkhg gjhf fhgf gjj hest"""
print (r)
#string concatenation
z = "asdsadsad" 
x = "asdfasdfasdf"
print(z+x)
#repetition
print(z*100)
#indexing
print(z[1])
#slicing
print(z[1:4])
#slicing by giving upper and lower limits
f='gurdaspur'
print(f[:7:2])
#for length
print(len(f))
#to reverse the string
print(f[::-1])
#string type conversion
sd='42'
sr= str(1)
ft = sd + sr
print(ft)
#string capitalize
r='aman is a good boy'
print(r.capitalize())
#returns number of time a word has been repeated
aa = "number 1 number 2 number3"
xx = aa.count("number")
print(xx)
#converts to lowercase
c = "HOHOHOHOHOHOHO"
print(c.casefold())
