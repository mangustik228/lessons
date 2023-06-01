function createCalcFunction(n) {
    return function() {
        console.log(1000 * n)
    }
}

const calc = createCalcFunction(42)
calc(42)

function createIncrementor(n){
    return function(num){
        return n + num
    }
}

const addOne = createIncrementor(1)
console.log(addOne(2));


function urlGenerator(domain){
    return function(url) {
        return `https://${url}.${domain}`
    }
}
const comUrl = urlGenerator('com')

console.log(comUrl('google'))



function logPerson(){
    console.log(`Person ${this.name}, ${this.age}`)
}

const person1 = {'name':'Vasya','age':34}

function my_bind(ctx, func) {
    ctx.func = func
    return ctx.func
}


my_bind(person1, logPerson)()
