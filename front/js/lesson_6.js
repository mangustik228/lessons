const person = Object.create({}, {
    name: {
        value: "Vasya", 
        enumerable: true, // Позволяет выводить 
        writable: true, // Позволяетт изменять поля
        configurable: true, // Позволяет удалить значение из объекта
    },
    birthYear: {
        value: 1989,
        enumerable: true
    }, 
    age: {
        get() {
            return new Date().getFullYear() - this.birthYear
        },
        set(value) {
            
        }
    }
})

// const person = {
//     name: "Vasya", 
//     birthYear: 1989
// }
person.name = "Ne Vasya"
person.birthYear = 2222

console.log(person)

for (let key in person) {
    console.log('key ', key)
}