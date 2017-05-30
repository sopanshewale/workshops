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

## A Few Rules: Commonly Used RegEx symbols
---

| symbol | Meaning | Example Pattern | Example Matches|
|---|---|---|---|
|*| Matches Preceding Char, Subexpression, or bracked char 0 or more times | a*b* | aaaaaa, aaabbbb, bbbb|
|+| Matches Preceding Char, Subexpression, or bracked char 1 or more times | a+b+ | aaaaab, aaabbbb, abbbb|
|[] | Matches any char within bracket |[A-Z]*| APPLE, CAPITAL, |
|()| A groupd subexpression | (a*b)* | aaabaab, abaaab|
|{m, n}| Matches the preceding character, subexpression, or bracketed chars between m and n times| a{2,3}b{2,3} | |
|[^] | Matches any single character that is not in the brackets  | [^A-Z]* | aaple |
||| Matches any char, or subexpression, separated by | | b(a|i|e)d| bad, bid, bed|
|.| Matches any single charector| b.d| bed, bzd, b$d|
|^|Beging of line| ^a|apple, an, |
|\|An Escape Char| ||
|$|Used for end of line char| [A-Z]*[a-z]*$| ABCabc, zzzyz, Bob|



## Matching Codes

|Code|Meaning|
|---|---|
|\d|a digit|
|\D|a non-digit|
|\s|whitespace (tab, space, newline, etc.)|
|\S|non-whitespace|
|\w|alphanumeric|
|\W|non-alphanumeric|


## Mostly used functions from re module,

* compile(pattern, flags=0) – it compiles a regular expression pattern into a regular expression object, which can be used for matching using the match and search methods.
* match(pattern, string, flags=0) – if zero or more characters from the beginning of the string match, it returns a Match object, otherwise, it returns None.
* search(pattern, string, flags=0)  – similar to match(), but it scans all the string, not only it’s beginning.
* sub(pattern, repl, string, count=0, flags=0) -  Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.  repl can be either a string or a callable; if a string, backslash escapes in it are processed.  If it is a callable, it's passed the match object and must return a replacement string to be used.
* findall(pattern, string, flags=0)- Return a list of all non-overlapping matches in the string.
* finditer(pattern, string, flags=0)- Return an iterator over all non-overlapping matches in the string.  For each match, the iterator returns a match object.
        

## Examples: 

1. simple_match.py

```
import re

pattern = 'Hello'
text = 'Hello Data Science Folks, How are you?'

match = re.search(pattern, text)
print (type(match))

s = match.start()
e = match.end()

print('Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

```

2. simple_compiled.py 

```
import re

pattern = 'Hello'
re_pattern = re.compile(pattern)
text = 'Hello Data Science Folks, How are you?'

print (type(pattern))

match = re.search(re_pattern, text)
print (type(match))

s = match.start()
e = match.end()

print('Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

```

