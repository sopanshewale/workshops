# formatting integers
#'Binary representation of 12 is 1100'
print("Binary representation of {0} is {0:b}".format(12))

 # formatting floats
#'Exponent representation: 1.566345e+03'
print("Exponent representation: {0:e}".format(1566.345))

# round off
#'One third is: 0.333'
print( "One third is: {0:.3f}".format(1/3))

# string alignment
#'|butter    |  bread   |       ham|'
print( "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
