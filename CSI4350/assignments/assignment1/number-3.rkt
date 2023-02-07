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


(remove `a `(a b a b a c d e a))