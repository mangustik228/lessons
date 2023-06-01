class Animal {

    static type = 'ANIMAL'

    constructor(options) {
        this.name = options.name 
        this._age = options.age 
        this.hasTail = options.age
    }

    voice(){
        console.log(`I am ${this.name}`)
    }

    get age() {
        return this._age * 7
    }
    set age(value) {
        return this._age = value 
    }
}

class Cat extends Animal {
    constructor(options) { 
        super(options)
        this.color = options.color 
    }
}


let cat = new Cat({
    name: 'Cat',
    age: 7,
    hasTail: true, 
    color: 'red'
})


let animal = new Animal({
    name: 'Animal',
    age: 25,
    hasTail: true
})




console.log(animal)
animal.voice()
cat.voice()
console.log(typeof Animal)
console.log(cat.age)
cat.age = 10
console.log(cat.age)


// -------------------------- Component --------------------- // 


class Component { 
    constructor(selector) {
        this.$el = document.querySelector(selector)
    }

    hide() { 
        this.$el.style.display = 'none'
    }
    
    show() {
        this.$el.style.display = 'block'
    }
}



class Box extends Component { 
    constructor(options) {
        super(options.selector)
        this.$el.style.width = this.$el.style.height = options.size + 'px'
        this.$el.style.background = options.color
    }
    set color (value) {
        this.$el.style.background = value 
    }
}

const box1 = new Box({
    selector: '#box1',
    size: 200, 
    color: 'blue'
})


class Circle extends Box {
    constructor(options) {
        super(options)
        this.$el.style.borderRadius = '50%'
    }
}

const circle = new Circle({
    selector: '#circle1',
    size: 300, 
    color: 'red'
})