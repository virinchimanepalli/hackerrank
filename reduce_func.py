import re

P = "101201"
k = r"____[1-9]\d{5}$_____"
m = r"(\d)(?=\d\1)"
print (re.match(k, P)) 
# and len(re.findall(m, P)) < 2)

print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))

# In this just replcae blanks with re.math value, i.e -'^[1-9][\d]{5}$' and re.findall value with '(\d)(?=\d\1)' in the hackerrank IDE