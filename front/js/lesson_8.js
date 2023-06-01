const delay = ms => {
    return new Promise(r => setTimeout(r, ms))
}

// delay(2000).then(() => console.log('2sec'))
let url = 'https://jsonplaceholder.typicode.com/todos'


// function fetchTodos() {
//     console.log('fetch todo started')
//     return delay(2000).then(() => fetch(url))
//         .then(response => response.json())
// }

// fetchTodos()
//     .then(data => console.log('Data:', data))
//     .catch(e => console.error(e))


async function fetchAsyncTodos() { 
    try {
        console.log('start delay')
        await delay(2000)
        console.log('start response')
        const response = await fetch(url)
        const data = await response.json()
        console.log(`${data}`)
    } catch (e) {
        console.error(e)
    } finally {
        console.log('ego-go! nice code!')
    }
}

fetchAsyncTodos()