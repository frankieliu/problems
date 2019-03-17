
Python Recursion, No Stack, with Explanations

https://leetcode.com/problems/parse-lisp-expression/discuss/109723

* Lang:    python3
* Author:  flamesofmoon
* Votes:   0

I defined five functions for structural clearness: `isnum`, `find`, `helper`, `compute`, `let`.

`isnum` is to check if the given string is composed of numbers.

`find` is to go along `expression` and find the next object and evaluate it

`helper` is a task-assigner. It assigns tasks depends on whether the operator is `let` or not.

`compute` is to do addition or multiplication.

`let` is to execute 'let' operation. Note that there is a nonlocal dictionary `values` that is accessible everywhere in the program. To handle different layer of value assignment, a local dictionary `changed` is established. Before returning the result of `let` function, `changed` is used to recover the `values` before executing the current `let`.

The program keeps going forward, never turn back, and only passes indices when doing recursion, so it is O(n) and should be pretty fast.

```
        def isnum(s):     # check if s is composed of numbers
            try:
                int(s)
                return True
            except:
                return False

        def find(start, need_num = True): # find the next expression and evaluate it
            # need_num is to indicate whether numeric answer is preferred
            
            if expression[start] == '(':
                return helper(start+1)
            else:
                i = start
                while expression[i] not in ' )':
                    i += 1
                    
                ans = expression[start:i]

                return (int(ans) if isnum(ans) \\
                                 else values[ans] if need_num \\
                                                  else ans, \\
                        i-1)
                    
        def helper(start):        # return the answer and the index of the ending ')'
            i = start
            while expression[i] != ' ':
                i += 1
            
            op = expression[start:i]
            if op == 'let':
                return let(i+1)
            else:                 # op is either 'add' or 'mult'
                return compute(i+1, op)
        
        def compute(start, op):   # return the answer and the index of the ending ')'
            x, i = find(start)
            y, j = find(i+2)
            
            return ( x+y if op=='add' else x*y, j+1 )
        
        def let(start):           # return the answer and the index of the ending ')'  
            changed = {}          # this is to record those values changed in the current 'let'

            while True:
                x, i = find(start, False)
                
                if expression[i+1] == ')':      # the end of 'let' expression is reached 
                    temp = (values[x] if x in values else x, i+1)

                    for x in changed:           # this is to discard the changes we made to 'values' in the current 'let'
                        if changed[x] != None:
                            values[x] = changed[x]
                        else:
                            del values[x]

                    return temp
                
                y, j = find(i+2)

                changed[x] = values[x] if x in values else None
                values[x] = y
                
                start = j + 2
        
        values = {}
        return helper(1)[0] 
```
