function hello() {
    console.log('Hello', this);
}

const person = {
    name: 'Vlad',
    age:25, 
    sayHello: hello,
    // sayHelloWindow: hello.bind(window), 
    logInfo: function(job) {
        console.group(`${this.name} info:`)
        console.log(`name is ${this.name}`)
        console.log(`age is ${this.name}`)
        console.log(`job is ${job}`)
        console.groupEnd()
    }
}

person.sayHello()
// person.sayHelloWindow()
person.logInfo()

let lena = {
    name: "Elena" 
}

person.logInfo.bind(lena)('pivovar')

person.logInfo.call(lena, 'front') 

const array = [1,2,3,4,5]

function multBy(n, arr) {
    return arr.map((i) => i * n)
}

console.log(multBy(15, array))

Array.prototype.multBy = function (n) {
    return this.map((i) => i * n)
}

console.log(array.multBy(2))