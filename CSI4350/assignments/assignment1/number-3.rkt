#lang racket
(define remove
  (lambda (s los)
    (if (null? los)
        `()
        (if (eqv? (car los) s)
            (remove s (cdr los))
            (cdr los)
            (remove s (cdr los))))))