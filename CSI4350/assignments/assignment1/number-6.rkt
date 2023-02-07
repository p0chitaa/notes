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

(sort `(2 3 1 4 9 5 11 2 6))