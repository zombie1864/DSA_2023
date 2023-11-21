/**
@tutorial   : JS PARADIGM AND USAGE 
@description: Some major paradigm in js include: 
    []_event-driven: fns can be made to respond to events, such as `clicks` on el
    `resize` of the browsing window, `mousehover`, `mouseenter`, `mouseleave` etc. 

    []_function: fns can be written as 'pure function(s)'--always having the same output for a given 
    set of args and never produce side-effects, 'first-class function(s)', or 'higher-order function(s)'. 
    The latter function(s) are treated as normal values, passed as args to other fns and returned from fns. 

    []_OOP: Objects are custom data stores and they can be made to inherit from each other
**/



/**
@tutorial   : VARIABLES AND SCOPING 
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
@tutorial   : ARRAY AND ARRAY BUILT-IN METHODS
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



/**
@tutorial   : THE `switch` STATEMENT 
@kind       : ADVANCE TOPIC
@description: Boolean logic looks at cond in order 2 exec blocks of codes. A switch is similar but does not use 
cond 2 compare against in order 2 exec blocks. Instead it compares val. 
@example    : ```

    let usrRank = 'private'; // default rank 
    getUserRank(); // dev define fn that gets usr rank and mutates the val in VAR usrRank 

    switch(usrRank) {
        case 'sergent': 
            print('You are not authorized. Please wait while I seek further assistance'); 
            alertAdminOfAttempt(); // dev defined fn 
            callCommander(); // dev defined fn 
            setVideoInterface_Wcommander(); // dev defined fn 
            getUserRank_WcommanderPermissionKey(); // dev defined fn 
            break; 
        case 'commander': 
            print('Hello commander! what can i do for you today?'); 
            promptCommanderRankOpt(); // dev defined fn 
            break; 
        case 'captain': 
            print('Hello captain! I will do anything you wish.'); 
            promptCaptainRankOpt(); // dev defined fn 
            grantCaptainAdminAccessInterface(); // dev defined fn 
            break; 
        default: 
            print('Greetings cadet. How can i help you?'); 
            promptCadetOpt(); // dev defined fn 
            alertAdminOfCadetUsage(); // dev defined fn 
    }
    
``` 
**/



/**
@tutorial   : `obj.hasOwnProperty(prop)`
@kind       : ADVANCE TOPIC 
@description: itr over an obj ds can yeild members who don't actually belong 2 the obj. The `obj.hasOwnProperty(prop)`
is a built-in methid that checks if prop belongs 2 the obj and is not inherited from its prototype chain. 
The prototype chain are props/methods that an object inherits from another ds class. In the case of the object ds 
it inherits from the `Object` class. When you access a prop on an obj ds, js 1st checks if that prop exists 
directly on the obj ds. If it doesn't then it looks up the prototype chain until it finds the prop. 

    []_in js every inst of the `Object` class has a a bunch of built-in key-value pair containing meta info abt the obj {
        @example: ``` 
            let obj = {'fruits': ['apple']}
        ``` 

        []_list of prototype chain methods {
            __proto__: ''
            constructor: f Object() 
            hasOwnProperty: f hasOwnPeropty() 
            isPrototypeOf: f isPrototypeOf() 
            propertyIsEnumerable: f propertyIsEnumerable() 
            toLocaleString: f toLocaleString() 
            toString: f toString() 
            valueOf: f valueOf() 
            ... 
        }
    }

    

    []_When itr over the props of an obj ds, it checks if the prop exist in the obj itself but if it doesn't find it 
    it then looks into the prototype chain. If the obj mutates over time w/o direct dev knowledge this could led 2 bugs 


    []_if you have full control of the lifecycle of the obj then you wouldn't need 2 use `obj.hasOwnProperty(prop)`. 
    But if you do not then using the method would prevent potential bugs in the code 

@example: ``` 
    let fruitObj = {
        'name': 'Apple', 
        'shape': 'round', 
        'taste': 'sweet' 
    }; 
    print(fruitObj.hasOwnProperty('name')) // => true 
    print(fruitObh.hasOwnProperty('placeOfOrigins')) // => false. b.c. this is not a key in the obj 
    print(fruitObh.hasOwnProperty('toString')) // => false. b.c. the obj itself does not have this method 
    print(fruitObh.prototype.hasOwnProperty('toString')) // true b.c. the obj inherits from the `Object` class w this method 
```

@example: ```
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) { // always checks the obj itself and not the prototype chain 
            print(`the val ${obj[key]} is in obj as prop ${key}`)
        }
    }
``` 
**/



/**
@tutorial   : CALLBACKS
@description: cb r fns that r passed as arg 2 other fns. Methods like `arr.forEach(cb)`, and `arr.map(cb)` take 
a cb fn as an arg. The concept of cb as arg is an imp feature of asynch programming. 
@example: ``` 
    let cb = function() {
        print('done'); 
    }; 

    setTimeout(cb, 5000) // prints done after 5sec delay. `setTimeout(cb, t)` is an asynch fn 
```
**/



/**
@tutorial   : PROMISES
@description: promises build on the concept of asynch programming. They are objs that repr the eventual completion or failure 
of an asynch operation and its resulting val. These objs help manage asynch code and make it easier 2 handle and reason abt
asynch tasks. Asynch operations can include fetching data from a remote server, reading file content, or waiting 4 
usr input/interaction.  
        
@example: The following is a BAD ex. It shows fetch isn't used```
    function getServerStatus() {
        let resp = fetch('/server/stat'); 

        // THIS WILL NOT WORK 
        print('The status from the server is: ', resp.ok) ERR 
    }
``` 
    []_In python this would work but that is b/c it runs synch not asynch 


@example: The correct way of fetching data from a server ``` 
    function gerServerStatus() {
        let resp = fetch('/server/stat'); 

        resp.then(function(stat) {
            print('The status from the server is', stat.ok)
        })
    }
``` 
    []_the `.then(cb)` is a consumer method b/c it consumes/proc(data) resp from the server 
    
@description: The `Promise` class posses 2 traits: 
    []_it takes a single cb arg known as the executor. The executor takes 2 cb args, the `resolve` and `reject` fn 
    that are provided by js of which the executor exec(resolve) or exec(reject). 
        []_when the exector obtains a val it uses either of the cb arg but NEVER both and changes the state of the promise: 
            []_`resolve(val)` -- if job finished with result `val`
            []_`reject(err)` -- if job results in an err, yields an err obj 
    []_a `.then(cb)` proc(res) obtain from the promise obj 

    []_schematic design of `Promise` state  
        new Promise(executor)               resolve(val)
        {                           -->     {
            state: 'pending',                   state: 'fulfilled', 
            result: undefined                   result: val 
        }                                   }

        OR 

        new Promise(executor)               Reject(val)
        {                           -->     {
            state: 'pending',                   state: 'rejected', 
            result: undefined                   result: err
        }                                   }

@example: ``` 
    function asynchSum(a, b) {
        let res = new Promise(function(resolve, reject) {
            resolve(a + b); 
        })

        return res // this returns the promise not the val 
    }

    asynchSum(3, 5).then(function(res) {
        print(`The result of the addition is: ${res}`); 
    })
``` 

@example: short-hand notation``` 
    function asynchSum(a, b) {
        return Promise.resolve(a + b); 
    }

    asynchSum.then(function(res) {
        print(`The result of the addition is: ${res}`); 
    })
``` 
**/



/**
@tutorial   : PROMISE USE CASES
@description: promises are widely used in js. 
    []_Fetching data from a db, APIs, or external source where the resp time is unpredictable and making http req 2 
    fetch(data) is asynch 
**/



/**
@tutorial   : PROMISE W `setTimeout(cb)`
@description: Using time delay 2 `produce code`
@example    :```
    let promise = new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve('done')
        }, 1000)
    })

    promise.then(function(msg) {
        print(msg); 
    })
``` 

@example    :``` 
    let promise = new Promise(function(resolve, reject) {
        setTimeout(function() {
            reject(new Error('Error!'))
        }, 1000); 
    })

    promise.then(function(msg) {
        print(msg)
    })
``` 
**/