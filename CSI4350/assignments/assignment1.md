# Assignment 1
Drew Bonde

## 1. ***[10 points]*** What sets are defined by the following pairs of rules? Explain why and also list a few members of each set.

### a. 
```
                 (n, k) ε S
(0, 1) ε S      ------------  
               (n+1, k+7) ε S
```

> The set defined by the above rules contains pairs starting at (0, 1) with the following rules: if (n, k) belong in the set S, then so does (n+1. k+7). Given that (0, 1) ε S, so does (1, 8), (2, 15), (3, 22), (4, 29), (5, 36), and so on.

$S = {(n, 7n+1) | n \epsilon ℕ}$

### b.
```
                 (n, k) ε S
(0, 1) ε S      -------------  
                (n+1, 2k) ε S
```

> The set defined by the above rules contains pairs starting at (0, 1) with the following rules: if (n, k) belong to the set S, then so does (n+1, 2k). Given that (0, 1) ε S, then so does (1, 2), (2, 4), (3, 8), (4, 16), (5, 32), and so on. To put an informal definition on this set, it contains powers of two, where n represents the exponent and k represents the product.

### c.
```
                  (n, i, j) ε S
(0, 0, 1) ε S   -----------------  
                (n+1, j, i+j) ε S
```

> The set defined by the above rules contains 3-tuples with the following rules: if (n, i, j) belong to the set S, then so does (n+1, j, i+j). To informally define this set, it act as the fibonacci sequence. Where n is the current step, i is the previous value, and j is the current value. Given that the fibonacci sequence is a set whose members are equal to the sum of the previous two numbers and that (0, 0, 1) ε S, this holds. For some example members, if (0, 0, 1) ε S, then so does (1, 1, 1), (2, 1, 2), (3, 2, 3), (4, 3, 5), (5, 5, 8), and so on.

### d. 
```
                  (n, i, j) ε S
(0, 1, 0) ε S  -------------------  
               (n+1, i+2, i+j) ε S
```

> The set defined by the above rules contains 3-tuples with the following rules: if (n, i, j) ε S, then so does (n+1, i+2, i+j). 