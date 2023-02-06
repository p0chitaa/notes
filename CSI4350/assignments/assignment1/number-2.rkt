#lang racket
(define get-following
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (cdr los)
            (get-following s (cdr los))))))

(get-following `a `(a b c d))