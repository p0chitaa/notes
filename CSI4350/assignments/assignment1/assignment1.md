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

* $S = {(n, 7n+1)\ |\ n\ \epsilon\ ℕ}$

### b.
```
                 (n, k) ε S
(0, 1) ε S      -------------  
                (n+1, 2k) ε S
```

> The set defined by the above rules contains pairs starting at (0, 1) with the following rules: if (n, k) belong to the set S, then so does (n+1, 2k). Given that (0, 1) ε S, then so does (1, 2), (2, 4), (3, 8), (4, 16), (5, 32), and so on. To put an informal definition on this set, it contains powers of two, where n represents the exponent and k represents the product.

* $S = {(n, 2^n)\ |\ n\ \epsilon\ ℕ}$

### c.
```
                  (n, i, j) ε S
(0, 0, 1) ε S   -----------------  
                (n+1, j, i+j) ε S
```

> The set defined by the above rules contains 3-tuples with the following rules: if (n, i, j) belong to the set S, then so does (n+1, j, i+j). To informally define this set, it acts as the fibonacci sequence. Where n is the current step, i is the previous value, and j is the current value. Given that the fibonacci sequence is a set whose members are equal to the sum of the previous two numbers and that (0, 0, 1) ε S, this holds. For some example members, if (0, 0, 1) ε S, then so does (1, 1, 1), (2, 1, 2), (3, 2, 3), (4, 3, 5), (5, 5, 8), and so on.

$S = {(n, F(n), F(n+1))\ |\ n\ \epsilon\ ℕ}$

### d. 
```
                  (n, i, j) ε S
(0, 1, 0) ε S  -------------------  
               (n+1, i+2, i+j) ε S
```

> The set defined by the above rules contains 3-tuples starting at (0, 1, 0) with the following rules: if (n, i, j) belongs to S, then so does (n+1, i+2, i+j). Given that (0, 1, 0) ε S, then so does (1, 3, 1), (2, 5, 4), (3, 7, 9), (4, 9, 16), (5, 11, 25), and so on.

$S = {(n, 2n+1, n^2)\ |\ n\ \epsilon\ ℕ}$

## 2. ***[10 points]*** In the definition of `remove-first` below, if that last line were replaced by `(remove-first s (cdr los))`, what function would the resulting procedure compute? Give the contract, including the usage statement, for the revised procedure.
```scheme
remove-first : Sym x Listof(Sym) --> Listof(Sym)

#lang racket
(define remove-first
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (cons (car los) (remove-first s (cdr los)))))))
```

> Upon editing the last line to `(remove-first s (cdr los))`, the function returns the rest of the list following the passed symbol, `s`.


Revised procedure:
```scheme
get-following : Sym x Listof(Sym) --> Listof(Sym)

#lang racket
(define get-following
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (remove-first s (cdr los))))))
```

## 3. ***[20 points]*** Define a procedure/function `remove` in Scheme, which is like `remove-first`, except that it removes _all_ occurrences of a given symbol from a list of symbols, not just the first.

