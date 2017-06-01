# Regular Expression
---

check this out : https://www.xkcd.com/208/


* Regular expressions are patterns described with a formal syntax. The patterns are tried to match with text. 
* The patterns are executed with a string as input to produce a matching subset or modified version of the original text

The term *“regular expressions”* is frequently shortened to *“regex”* or *“regexp”* in conversation. 

Regular expressions are typically used in applications that involve a lot of text processing and data


Let us look at some regular expression examples: Define some rules

* Write a letter "a" at least once
* Append to this the letter "k" exactly three times
* Append to this the letter "c" any even number of times
* Optionally, write the letter "d" at the end

Examples of such strings are:
* aaaakkkccccd
* aakkkcc

Many such strings can satifies the above rules.  Look at the script below: 

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
is the regular expression. This help detect whether text satisfy above defined rules or not. 

The execution of the above script is as below:

```
$ python3 simple_rules.py 
I am satisfying the Rules

```

## A Few Rules: Commonly Used RegEx symbols
---
Regular expressions support powerful patterns than simple literal text strings. 
Patterns can repeat, can be expressed in compact forms. Following  meta-characters can help you build regular expression pattern
syntax implemented by re module.

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

Following codes can help you create compact patterns - they represent certain set of charectors. 

|Code|Meaning|
|---|---|
|\d|a digit|
|\D|a non-digit|
|\s|whitespace (tab, space, newline, etc.)|
|\S|non-whitespace|
|\w|alphanumeric|
|\W|non-alphanumeric|

## Anchoring 

The relative location of pattern in the text is also most important part when you deal with data. 
Following anchoring instructions can help with this requirement. 

|Code|Meaning|
|---|---|
|^|start of string, or line|
|$|end of string, or line|
|\A|start of string|
|\Z|end of string|
|\b|empty string at the beginning or end of a word|
|\B|empty string not at the beginning or end of a word|


## Most commonly used functions from re module,

*re* module has lots of methods to help us with our *regex* needs. Following are a few very commonly used methods. 

* compile(pattern, flags=0) – it compiles a regular expression pattern into a regular expression object, which can be used for matching using the match and search methods. Its always better to compile patterns - they help improve the speed of code. 
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
text = 'Hello Python Programmers, How are you?'

match = re.search(pattern, text)
print (type(match))

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\n from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

```



2. simple_compiled.py 

```
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

```

3. regex_find_all.py

```
#!/usr/bin/python3

import re
regex = "\[P\] (.+?) \[/P\]+?"
line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday. [P] Donald Trump [/P] was not Pre
sident at that moment."
person = re.findall(regex, line)
print(person)


```

4.  regex_find_iter.py

```

#!/usr/bin/python3

import re
regex = r"\[P\] (.+?) \[/P\]+?"
line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday. [P] Donald Trump [/P] was not Pre
sident at that moment."

for match in re.finditer(regex, line):
        print (type(match))
        print ("match start: ", match.start())
        print ("match end (exclusive): ", match.end())
        print ("matched text: ", match.group())


```


## A few Patterns:  Repetition

* 'ab*' :  'a followed by zero or more b'
* 'ab+' :  'a followed by one or more b'
* 'ab?' : 'a followed by zero or one b'
* 'ab{3}':  'a followed by three b'
* 'ab{2,3}' :  'a followed by two to three b'

## Character Sets

A character set is a group of characters, any one of which can match at that point in the pattern. For example, [ab] would match either a or b.

* '[ab]' :  'either a or b'
* 'a[ab]+' :  'a followed by 1 or more a or b'
* '[a-z]+' :  'sequences of lowercase letters'
* '[A-Z]+' :  'sequences of uppercase letters'
* '[a-zA-Z]+' :  'sequences of letters of either case'
* '[A-Z][a-z]+' :  'one uppercase followed by lowercase'


A character set can also be used to exclude specific characters. The carat (^) means to look for characters that are not in the set following the carat.

* '[^-. ]+':  'sequences without -, ., or space' 

## Matches with Groups

We need to address certain parts of texts while extracting information from it. 
The group method on *match* object from *re* module is most important part while dealing with *regex*. 
We can define a group as a piece of the regular expression search string, and then individually address the corresponding content that was matched by this piece.


## Search Options 

### Case Insensitive Match 
### Multiple Line Match 
### Verbose Expression Syntax


## References 
* http://pythex.org/ 
