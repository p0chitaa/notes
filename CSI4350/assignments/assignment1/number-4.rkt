#lang scheme
(define duple
  (lambda (n x)
    (if (zero? n)
      `()
      (cons x (duple (- n 1) x)))))

(duple 2 `(3 4))