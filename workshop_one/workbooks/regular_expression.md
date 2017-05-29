# Regular Expression
---

* Regular expressions are patterns described with a formal syntax. The patterns are tried to match with text. 
* The patters are executed with a string as input to produce a matching subset or modified version of the original

The term “regular expressions” is frequently shortened to “regex” or “regexp” in conversation. 

Let us look at some regular expression examples: Define some rules

* Write a letter "a" at least once
* Append to this the letter "k" exactly three times
* Append to this the letter "c" any even number of times
* Optionally, write the letter "d" at the end

Examples of such strings are:
* aaaakkkccccd
* aakkkcc

May such strings can satifies above rules.  Look at the script below: 

```
import re

text = 'aaaabbbbbccccccd'
pattern = 'a+kkk(cc)+d?'
match = re.match(pattern, text)

if match:
   print ("I am satisfying the Rules")
else:
   print ("Nope - The rules are not satisfied")

```

The pattern: 

```
pattern = 'a+bbbbb(cc)+d?'

```
help detect whether text satisfy above defined rules or not. 

The execution of the above script is as below:

```
$ python3 simple_rules.py 
I am satisfying the Rules

```


