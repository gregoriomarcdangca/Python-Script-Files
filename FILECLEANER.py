import re
file = (r"C:\Users\marcg\Documents\squid.conf")
clean = open(file).read()
cleaned = re.sub("#", " ", clean)
open(file,"w").write(cleaned)