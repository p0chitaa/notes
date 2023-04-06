# Assignment 4

## 1. ***[25 points]*** In PROC, procedures have only one argument, but one can get the effect of multiple argument procedures by using procedures that return other procedures.

```
let f = 
  proc (x) proc (y) in
    -(x,-(0,y))
``` 

<hr>

## 2. ***[30 points]*** Suggest changes to the syntax (concrete and abstract syntax) of PROC as well as its semantics (value-of method) to add a new kind of procedure called a traceproc to the language.

```scheme
Syntax addition:
Expression ::== traceproc (Identifier) Expression ;concrete
                traceproc-exp (var body) ;abstract

Semantic addition:
(value-of (traceproc-exp var body) p)
= ((display `(procedure execution just started)) (newline)
      proc-val (procedure var body p))
```

## 3. ***[30 points]*** Suggest changes to the syntax (concrete and abstract syntax) of PROC as well as its semantics (value-of method) to have procedures with 2 parameters instead of 1.

```scheme
Syntax additions:
Expression ::== proc (Identifier) (Identifier) Expression ;concrete
                proc-exp (var1 var2 body) ;abstract

Expression ::== (Expression Expression) ;concrete
                call-exp (rator rand1 rand2) ;abstract

Semantic additions:
(value-of (proc-exp var1 var2 body) p)
= (proc-val (procedure var1 var2 body p))

(value-of (call-exp rator rand1 rand2) p)
= (let ((proc (expval->proc (value-of rator p)))
        (arg1 (value-of rand1 p))
        (arg2 (value-of rand2 p)))
    (apply-procedure proc arg1 arg2))

(apply-procedure (procedure var1 var2 body p) val1 val2)
= (value-of body [var1=val1][var2=val2]p)
```

## 4. ***[15 points]*** What is the value of the following PROC program?
```
let makemult = proc (maker)
                proc (x)
                  if zero?(x)
                    then 0
                      else -(((maker maker) -(x,1)), -4)
  in let times4 = proc (x) ((makemult makemult) x)
    in (times4 3)
```
*Explain, in plain English, how did you get this value.*

> This program evaluates to 12. Each time x is decremented, `makemult` increments by 4. So in this case, `x` is 3. The first iteration it increments and equals 4 and `x` gets decremented to 2. The second iteration, `makemult` is now 8, and `x` is down to 1. The third iteration, `makemult` is now 12 and `x` is 0.