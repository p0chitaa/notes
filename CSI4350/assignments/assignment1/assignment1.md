# Assignment 1
Drew Bonde

> quick little sidenote: I will definitely attach the .rkt files in my submission, but I will also have them showing up in here for the sake of looking pretty lol

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

#lang scheme
(define remove-first
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (cons (car los) (remove-first s (cdr los)))))))
```

---
> Upon editing the last line to `(remove-first s (cdr los))`, the function returns the rest of the list following the passed symbol, `s`.


Revised procedure:
```scheme
get-following : Sym x Listof(Sym) --> Listof(Sym)

#lang scheme
(define get-following
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (remove-first s (cdr los))))))
```

## 3. ***[20 points]*** Define a procedure/function `remove` in Scheme, which is like `remove-first`, except that it removes _all_ occurrences of a given symbol from a list of symbols, not just the first.

After asking a really stupid question on piazza, I finally figured this out lol.

For the life of me I wanted to figure out how to do this without using `else` but here we are.

The code:
```scheme
#lang scheme
#lang scheme
(define remove
  (lambda (s los)
    (cond
      ((null? los)
       '())
      ((eqv? (car los) s)
       (remove s (cdr los)))
      (else
       (cons (car los) (remove s (cdr los)))))))

```

## 4. ***[20 points]*** Define a procedure `duple` in Scheme with the following usage.
***Usage:*** `(duple n x)` returns a list containing `n` copies of `x`.

***Usage sample 1:*** 
```scheme
(duple 2 3) 

outputs 

`(3 3)
```

***Usage sample 2:***
```scheme
(duple 4 `(ha ha)) 

outputs 

`((ha ha) (ha ha) (ha ha) (ha ha))
```

***Usage sample 3:***
```scheme
(duple 0 `(blah)) 

outputs 

`()
```

You can use Dr. Racket, as discussed in the class to write, debug and execute your code.

---
The code:
```scheme
#lang scheme
(define duple
  (lambda (n x)
    (if (zero? n)
      `()
      (cons x (duple (- n 1) x)))))
```

## 5. ***[20 points]*** Define a procedure `invert` in Scheme with the following usage.

***Usage:*** `(invert lst)` where `lst` is a list of 2-lists (lists of length two), return s a list with each 2-list reversed.

***Usage sample:***
```scheme
(invert `((a 1) (a 2) (1 b) (2 b)))

outputs

`((1 a) (1 a) (b 1) (b 2))
```

---
Ok, so for this one I decided to write two functions:
1. `inner-invert` to handle reversing the contents of each nested list
2. `invert` to handle running `inner-invert` on each nested list in the parent list

The code:
```scheme
#lang scheme
(define inner-invert
  (lambda (lst)
    (if (null? lst)
      `()
      (append (inner-invert (cdr lst)) (list (car lst))))))

(define invert
  (lambda (lst)
    (if (null? lst)
        `()
        (cons (inner-invert (car lst)) (invert (cdr lst))))))
```

## 6. ***[20 points]*** Define a procedure `sort` in Scheme with the following usage.

***Usage:*** `(sort loi)` returns a list of the elements of `loi` in ascending order.

***Usage sample:***
```scheme
(sort `(8 2 5 2 3))

outputs

`(2 2 3 5 8)
```

---
So I'm sure there is a much much better way of doing this, but mine completely revolves around finding the smallest element.
* I started doing it this way and I was in **way** too deep to start over so I stuck with it.

I wrote three functions:
1. `get-smallest` to return the smallest element in a passed list of numbers
2. `remove-first` the given function from number 2 in this assignment to remove the first instance of the smallest element
3. `sort` to handle returning the sorted array with the above two functions

```scheme
#lang scheme
(define get-smallest
  (lambda (loi)
    (cond
      ((null? (cdr loi))
       (car loi))
      ((<= (car loi) (get-smallest (cdr loi)))
       (car loi))
      (else
       (get-smallest (cdr loi))))))

(define remove-first
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (cons (car los) (remove-first s (cdr los)))))))

(define sort
  (lambda (loi)
    (if (null? loi)
        `()
        (append (list (get-smallest loi)) (sort (remove-first(get-smallest loi) loi))))))
```