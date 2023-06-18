let interval

export default {
  mounted(el, binding) {
    console.log(el)
    console.log(binding)
    el.style.color = binding.value

    if (binding.modifiers.blink) {
      let flag = true
      interval = setInterval(() => {
        el.style.color = flag ? '#fff' : binding.value
        flag = !flag
      }, 400)
    }
  },

  updated(el, binding) {
    el.style.color = binding.value
  },
  unmounted() {
    console.log('unmounted interval')
    if (interval) {
      clearInterval(interval)
    }
  }
}
