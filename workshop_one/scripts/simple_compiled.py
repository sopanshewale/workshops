#!/usr/bin/python3
import re

pattern = 'Hello'
re_pattern = re.compile(pattern)
text = 'Hello Python Programmers, How are you?'

print (type(pattern))

print('Seeking "{}"'.format(re_pattern.pattern))
match = re.search(re_pattern, text)
print (type(match))

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))


