# Recursion 

Recursion is a method of solving a problem by reducing it to a simpler problem of the same type.
Let us look at the example of converting decimal integer to binaray number.

Any whole number has the form 2k + b, where k is some smaller whole number and b is either 0 or 1.
In whole numbers binary expantion, b is the final bit of the binary expansion. It’s easy to see whether this final bit is 0 or 1; 
We just look to observe whether the input number is even or odd. The rest of the number is 2k, whose 
binary expansion is the same as that of k, but shifted left one place


For example, consider the number 37 = 2·18+1; here k is 18 and b is 1, so the binary expansion 
of 37 (100101) is the same as that of 18 (10010), but with an extra 1 on the end.

TODO - diagram, compute expantion of 37

This procedure will work for any number. To compute the binary expansion of a number *n* we proceed as follows:
* 1. If n is 1, its binary expansion is 1, and we may ignore the rest of the procedure. Similarly, if n is 0, the expansion is simply 0. Otherwise:
2. Compute k and b so that n=2k+b and b=0 or 1.To do this, simply divide n by 2; k is the quotient, and b is the remainder, 0 if n was even, and 1 if n was odd.
3. Compute the binary expansion of k, using this same method. Call the result E.
4. The binary expansion for n is Eb.


Step 1 - can be be achieved with following 

```
def binary(n):
   if n == 0 or n == 1
        return n 

```
For Step 2 - 

``` 
    k = int (n/2)
    b = n % 2 

```

For the Step - 3, we need to find the binary expansion of *k* 

```
    E  = binary(k)
```

So the final step is just string concatanation 

```
    return E + b 

```

So the final code looks as below

```
#!/usr/bin/python3
import sys

def binary(n):
   if n == 0 or n == 1:
        return str(n)
   k = int (n/2)
   b = n % 2 
   return str(binary(k)) + str(b)

number = int(sys.argv[1])
bin_exp = binary(number)
print (bin_exp)

```

The essential technique here was to reduce the problem to a simpler case. We were supposed to find the binary expansion 
of a number n; we discovered that this binary expansion was the concatenation of the binary expansion of a smaller number 
k and a single bit b. Then to solve the simpler case of the same problem, we used the function binary() in its own 
definition. When we invoke binary() with some number as an argument, it needs to compute binary() for a different, smaller 
argument, which in turn computes binary() for an even smaller argument. Eventually, the argument becomes 1, and binary() 
computes the trivial binary representation of 1 directly.

This final step, called the base case of the recursion, is important. If we don’t consider it, our function might never 
terminate. If, in the definition of binary(), we had omitted the lines:

```
   if n == 0 or n == 1:
        return str(n)

```

then binary() would have computed forever, and would never have produced
an answer for any argument.

---


