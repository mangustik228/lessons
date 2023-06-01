let url = 'https://api.sampleapis.com/countries/countries'

// const listPromies = fetch(url)
// listPromies.then(data => {
//     console.log('data')
// })
// console.log('hello')


// async function test () {
//     console.log('data send')
//     let data = await fetch(url)
//     console.log('data received')
//     return data 
// }

// async function second_function (data) {
//     console.log(await data)
// }


// console.log('start request')
// let data = test()
// console.log(data)
// console.log('after function')
// second_function(data)


// ----------------------------------- Example 2 -------------------------

// const family = [
//     {
//         member:"mother",
//         id:111,
//         coffee:'Black'
//     },
//     {
//         member:"father",
//         id:222,
//         coffee:'Espresso'
//     },
//     {
//         member:"sun",
//         id:333,
//         coffee:'Cappucino'
//     }
// ]


// const getFamilyMember = (id) => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             const member = family.find(res => res.id === id)
//             console.log(member)
//             if (member) {
//                 resolve(member)
//             } else {
//                 reject(Error('Члени семьи не найден'))
//             }
//         }, 2500)
//     })
// }


// getFamilyMember(111)
//     .then(data => {
//         return getCoffee(data)
//     })
//     .then(newMember => {
//         console.log('newMember > ', newMember)
//     })

// url = 'https:///api.sampleapis.com/coffee/hot'

// const getCoffee = (member) => {
//     const coffeePromise = fetch(url)
//     return coffeePromise
//             .then(data => data.json())
//             .then(list => {
//                 console.log('list >>> ', list)
//                 const coffee = list.find(res => res.title === member.coffee)
//                 return {
//                     ...member, 
//                     coffee
//                 }
//             })
// }

// ------------------------------------ Example 3 (ALL) -----------------------

// const makeCoffee = () => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve('Your coffee already')
//         }, 500)
//     })
// }

// const makeToast = () => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve('Your toasts are already')
//         }, 2500)
//     })
// }

// const coffeePromise = makeCoffee()
// const toastPromise = makeToast()

// Promise
//     .all([coffeePromise, toastPromise])
//     .then(([coffeePromise, toastPromise]) => {
//         console.log(coffeePromise)
//         console.log(toastPromise)
//     }
// )

// coffeePromise.then(data => console.log(data))
// toastPromise.then(data => console.log(data))



const beersPromise = fetch('https://api.sampleapis.com/beers/ale')
const winesPromise = fetch('https://api.sampleapis.com/wines/reds')

Promise
    .all([beersPromise, winesPromise])
    .then(data => Promise.all(data.map(res => res.json())))
    .then(finalData => console.log(finalData))