// ------------------------ Проксирование объектов ---------------

// const person = {
//     name: 'Vladilen', 
//     age: 25, 
//     job: 'Fullstack'
// }


// const obj_proxy = new Proxy(person, {
//     get (target, prop) {
//         console.log(`Getting prop ${prop}`)
//         return target[prop]
//     },
//     set (target, prop, value) {
//         if (prop in target) {
//             target[prop] = value
//         } else {
//             throw new Error(`No ${prop} field in target`)
//         }
//     }, 
//     has(target, prop) { // Проверяет на наличие полей
//         return ['age', 'name', 'job'].includes(prop)
//     },
//     deleteProperty (target, prop) {
//         console.log('Deleting...', prop)
//         delete target[prop]
//         return true // Возвращаем чтоб подтвердить удаление
//     }
// })

// -------------------- Проксирование функций -------------------

// const log = text => `log: ${text}`

// const fp = new Proxy(log, {
//     apply(target, thisArg, args) { // Когда функция вызывается
//         console.log(`Calling fn...`)
//         return target.apply(thisArg, args).toUpperCase()
//     }
// })

// console.log(fp('Hello world'))

// ------------------ Проксирование классов ------------------------

// class Person { 
//     constructor(name, age) {
//         this.name = name
//         this.age = age 
//     }
// }

// const PersonProxy = new Proxy(Person, {
//     construct(target, args) { // Инициализация класса 
//         console.log('Construct...')
//         return new target(...args)
//     }
// })

// let p = new PersonProxy('Vasya', 34)
// console.log(p)

// ---------------------- Проксирование Wrapper -----------------------

// const withDefaultValue = (target, defaultValue = 0 ) => {
//     return new Proxy(target, {
//         get (obj, prop) {
//             return prop in obj ? obj[prop] : defaultValue
//         }
//     })
// }

// const posititon = withDefaultValue({
//     x:25,
//     y:35,
//     z:42
// }, 0)

// console.log('position = ', posititon)
// console.log('x = ', posititon.x)
// console.log('y = ', posititon.y)
// console.log('z = ', posititon.z)
// console.log('v = ', posititon.v)

// ---------------------------- Hidden properties ----------------------


// const withHiddenProps = (target, prefix = '_') => {
//     return new Proxy(target, {
//         has: (obj, prop) => (prop in obj) && (!prop.startsWith(prefix)),
//         ownKeys: obj => {
//             Reflect
//                 .ownKeys(obj) // Получение всех атрибутов объектов
//                 .filter(p => !p.startsWith(prefix))
        
//         },
//         get: (obj, prop, receiver) => (prop in receiver) ? obj[prop] : undefined
//     })
// }

// const obj = withHiddenProps({
//     hello:'world',
//     _name:'vasya',
//     _age:35
// }) 
// console.log(obj)

// ---------------------------- Optimaze --------------------------------



const IndexedArray = new Proxy(Array, {
    construct(target, [args]) {
        const index = {}
        args.forEach(item => index[item.id] = item)


        return new Proxy(new target(...args), {
            get(arr, prop) {
                switch (prop) {
                    case "push": 
                        return item => {
                            index[item.id] = item
                            arr[prop].call(arr, item)
                        }
                    case 'findById': 
                        return id => index[id] 
                    default: 
                        return arr[prop]

                }
            }
        })
    }
})

const users = new IndexedArray([
    {id:1, name:'Vasya',job:'Fullstack', age: 34},
    {id:2, name:'Danya',job:'student', age: 35},
    {id:3, name:'Renat',job:'frontend', age: 36},
    {id:4, name:'Egor',job:'backend', age: 37},
])