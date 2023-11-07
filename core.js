/**
@tutorial: JS PARADIGM AND USAGE 
@description: Some major paradigm in js include: 
    []_event-driven: fns can be made to respond to events, such as `clicks` on el
    `resize` of the browsing window, `mousehover`, `mouseenter`, `mouseleave` etc. 

    []_function: fns can be written as 'pure function(s)'--always having the same output for a given 
    set of args and never produce side-effects, 'first-class function(s)', or 'higher-order function(s)'. 
    The latter function(s) are treated as normal values, passed as args to other fns and returned from fns. 

    []_OOP: Objects are custom data stores and they can be made to inherit from each other
**/


/**
@tutorial: VARIABLES AND SCOPING 
@description: `let`, `var`, `const`, block scope, fn scope, hoisting 
    []_`let` vs `var` {
        []_`let` used 4 block-scoped VAR 2 init val(s)
        []_`var` used 4 fn-scoped VAR; automatically init 2 `undefined` 
        []_diff(let, var): var is fn-scope meaning that it is accessable anywhere within the fn it is 
        declared in. Whereas let is block-scoped; accessable within the block {...}
    }

    []_const: used for declaring a VAR that doesn't change nor be reassigned 

    []_block scope: behavior of VAR(s) only accessible inside the block it was defined. The block is {} 

    []_fn scope: the behavior of VAR(s) accessible anywhere inside the fn it was defined

    []_hoisting: VAR(s) declared with `var` are hoisted to the top--meaning that these VAR(s) can be 
    used before it is declared but it will have a default val of `undefined` 
**/


/**
@tutorial: ARRAY AND ARRAY BUILT-IN METHODS
@description: Arr ds, itr and traversal methods, searching/finding methods, add/rm el(s), manipulating methods, 
length and size methods, checking and conversion methods, cloning and copying methods, and Type-specific methods 
    []_arr are ds 4 storing info in a sequential order 


    []_itr methods {
        []_arr.forEach(cb)  -- itr(arr, el) and applies cb 2 each el 
        []_arr.map(cb)      -- creates new arr and applies cb 2 each el 
        []_arr.filter(cb)   -- creates a new arr w el(s) that pass a test defined by the cb 
        []_arr.reduce(cb, initVal) -- reduces arr 2 a single val (left-2-right)
        []_arr.every(cb)    -- checks if all els pass a test defined by the cb 
        []_arr.some(cb)     -- checks if at least 1 el passes a test defined by the cb 
    }


    []_searching methods {
        []_arr.indexOf(val)     -- returns the idx of a specific val 
        []_arr.lastIndexOf(val) -- returns last idx of a specified val 
        []_arr.find(cb)         -- returns 1st el 2 satisfy cond defined by cb 
        []_arr.findIndex(cb)    -- returns the idx of the 1st el 2 satisfy cond defined by cb  
        []_arr.includes(val)    -- checks if arr includes val 
    }


    []_add/rm el(s) {
        []_arr.push(el)     -- adds el to the end of arr 
        []_arr.unshift(el)  -- add el to front of arr 
        []_arr.pop()        -- rm the last el from arr 
        []_arr.shift()      -- rm first el from arr 
        []_arr.splice(idx, howMany, el1, ..., elN) -- adds/rm el from a specific idx 
        []_arr.concat(arr1, ... , arrN) -- combines arrs; returns new combined arr 
    }


    []_manipulating methods {
        []_arr.copyWithin(trg, start, end) -- copies els within the arr 
        []_arr.fill(val, start, end)       -- fills el with a static value 
        []_arr.reverse()                   -- reverses the order of els 
        []_arr.sort(cb)                    -- sorts the el according 2 cb 
        []_arr.slice(start, end)           -- extracts a section of the arr 
        []_arr.join(delimiter)             -- converts the arr in2 str, concatenated by the delimiter 
        []_arr.toString()                  -- alias 4 `.join`
        []_arr.concat(arr)                 -- combines arrs to create a new arr 
    }


    []_checking and conversion methods {
        []_arr.isArray(ds)                   -- checks if the ds is an arr 
        []_arr.from(arrLike, mapFn, thisArg) -- creates a new arr from an arrLike ds 
        []_arr.of(...els)                    -- creates a new arr from its args 
        []_arr.length                        -- prop that specifies the num of els in an arr 
    }
**/