import re
with open('Alphanumericdata.txt') as f:
    passage = f.read()
words = re.findall(r"\bT\w*?T\b", passage)
print(words)