import re
txt="Rashad Bingo"
x=re.search("^Rashad",txt)
if x:
    print("Found")
else:
    print("Not found")
print("-----------1------------")

import re
txt="Rashad Bingo"
x=re.search("Bingo$",txt)
if x:
    print("Found")
else:
    print("Not found")
print("----------2------------")

import re
txt="Rashad Middle Bingo"
x=re.search("^Rashad.*Bingo",txt)
if x:
    print("Found")
else:
    print("Not found")
print("------------3-------------")

import re
txt="Rashad Middle Bingo"
x=re.search("Rasha",txt)
if x:
    print("Found")
else:
    print("Not found")
print("------------4-------------")
import re
txt="Rashad Bingo"
x=re.search("[a-z]",txt)
if x:
    print("Found")
else:
    print("Not found")
print("------------5-------------")
import re
txt="Rashad Bingo"
x=re.search("^Rash?.d",txt)
if x:
    print("Found")
else:
    print("Not found")
print("----------6----------")
import re
txt="Naja"
x=re.search("N.+a",txt)
if x:
    print("Found")
else:
    print("Not found")