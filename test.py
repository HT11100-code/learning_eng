import re

text = "abc@xxx.coms"

p = re.compile(r'([a-z]+)@([a-z]+)\.com')
print(re.match(r'([a-z]+)@([a-z]+)\.com', text))