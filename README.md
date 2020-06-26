# pascals-triangle-starter

Pascal's triangle is a triangular array of the binomial coefficients.
https://en.wikipedia.org/wiki/Pascal%27s_triangle


Complete the function `pascalsTriangle` which takes an `int` and prints that many rows.

`pascalsTriangle(6)` would print:

```
     1  
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 
```

The entry in the nth row and kth column of Pascal's triangle is denoted `(n, k)`. The topmost row is row 0, denoted as `(0, 0) = 1`. The recursive formula to find an element in any row is:
```
(n, k) = (n - 1, k - 1) + (n - 1, k)
```
For `k >= n`, such as `(2, 3)`, we get 0 since it does not exist in the triangle.

To calculate row 3, column 1:
```
(3, 1) = (2, 0) + (3, 1)
       = 1      + (2, 0) + (3, 0)
       = 1      + 1      + 1
```

