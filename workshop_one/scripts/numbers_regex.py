#!/usr/bin/python
import re

ss = ["apple-12.34 ba33na fanc-14.23e-2yapple+45e5+67.56E+3",
          'hello X42 I\'m a Y-32.35 string Z30',
          'he33llo 42 I\'m a 32 string -30',
          'h3110 23 cat 444.4 rabbit 11 2 dog',
          "hello 12 hi 89"]                                                     
for s in ss:
    print re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", s)                                 
 
#['-12.34', '33', '-14.23e-2', '+45e5', '+67.56E+3']
#['42', '-32.35', '30']
#['33', '42', '32', '-30']
#['3110', '23', '444.4', '11']
#['12', '89']

