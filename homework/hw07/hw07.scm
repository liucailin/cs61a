(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

(define (ascending? asc-lst) (cond
    ((null? (cdr asc-lst)) true)
    ((> (car asc-lst) (car (cdr asc-lst))) false)
    (else (ascending? (cdr asc-lst)))
))

(define (square n) (* n n))

(define (pow base exp) (cond
    ((= exp 0) 1)
    ((even? exp) (square (pow base (/ exp 2))))
    (else (* base (pow base (- exp 1))))
))
