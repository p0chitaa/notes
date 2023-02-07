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

(invert `((2 1 2 1) (3 4 3 4) (6 7 6 7)))
      