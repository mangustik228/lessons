console.log('Request data ... ')


const p = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Preparing data...')
        const data = {'id':1,'data':[1,2,3]}
        resolve(data)
    }, 2000)
})


p.then(data => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            data.modified = true 
            console.log('Modified data...')
            resolve(data)
        }, 2000)
    })
}).then(data => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Start to request data....')
            resolve({data: data, value:''})
        }, 2000)
    })
}).then((obj) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Data successfull request!!!')
            if (obj.value) {
                console.log(`value = ${obj.value}`)
                resolve()
            } else {
                reject('jopa')
            }
        }, 2000)
    })
}).then().catch((r)=>console.log(r))




// const promis = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         console.log('Preparing data...')
//         const backenData = {
//             server: 'aws',
//             port: 2000,
//             status: 'working'
//         }
//         resolve(backenData) // Говорит что завершило выполнение
//     }, 2000)
// })


// promis.then((data) => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             data.modified = true
//             resolve(data)
//         }, 2000)
//     })
// }).then((cliendData) => {
//     console.log("Promise resolved", data)
// })