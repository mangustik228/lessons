const person = {
    name:'maxim',
    age:25,
    greet: function() {
        console.log('Greet!')
    }
}

person.greet()


Object.prototype.sayHello = function() {
    console.log('Hello!')
}

person.sayHello()

const lena = Object.create(person)
lena.name = 'Elena'
lena.sayHello()

'jopa'.sayHello()