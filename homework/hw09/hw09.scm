(define-macro (when condition exprs)
  (list 'if condition (cons 'begin exprs) ''okay)
)

(define-macro (switch expr cases)
  (cons _________
        (map (_________ (_________)
                        (cons _________ (cdr case)))
             cases)))
