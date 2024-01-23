

## `asyncio.Lock()`

**Lock** - базовый примитив синхронизации, который используется для ограничения доступа к общему ресурсу. Это один из самых базовых инструментов синхронизации и, вероятно, самый легко понятный.



```python 

lock - asyncio.Lock()

async def foo(): 
    async with lock:
        # blocked piece of code. 
        await bar()

```

## `asycnio.Event()` 

**Event** - это примитив синхронизации который позволяет одной корутине сигнализировать другим о том, что произошло какое-то событие. Корутины которые ожидают события, будут приостановлены до тех пор, пока событие не будет установлено.


```python 

event = asyncio.Event()

async def waiter():
    await event.wait()
    print('event done!')


async def setter():
    await asyncio.sleep(1)
    event.set()

async def main():
    await asyncio.gather(waiter(), setter())

```

## `asyncio.Semaphore()`

**Semaphore** - Это примитив синхронизации, который можно использовать для ограничения количества корутин, которые могут иметь одновременный доступ к определенному ресурсу. 


```python 

semapthore = asyncio.Semaphore(2)


async def foo(i: int):
    async with semapthore:
        print(f"coro [{i}] ACCESS")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(*[foo(i) for i in range(8)])

```


## `asyncio.Condition()` 

**Condition** - примитив синхронизации, который можно использовать для координации работы между несколькими корутинами. Он позволяет одной корутине ждать, пока другая корутина не установит определенное условие. 

```python 
async def consumer(condition: asyncio.Condition):
    async with condition:
        print('starting to wait condition...')
        await condition.wait()
        print(f"condition is True")


async def producer(condition: asyncio.Condition):
    await asyncio.sleep(1)
    async with condition:
        condition.notify_all()


async def main():
    await asyncio.gather(consumer(condition), producer(condition))
``` 

## `asyncio.BoundedSemaphore()` 

**BoundedSemaphore** - Таже фигня что и **Semaphore**, только с счётчиком 


## `asyncio.Barrier()` 

**Barrier** в asyncio - это механизм синхронизации, который позволяет программе ожидать, пока все участвующие задачи (или "корутины") не достигнут определенной точки. После того все участвующие задачи достигают этой точки, они могут продолжить свое выполнение. Иначе суть работы барера заключается в том что каждая задача, которая доходит до барьера, останавливается и ждет, пока все остальные задачи не достигнут барьера. Когда все задачи достигли барьера, они все продолжают выполнение... 

штука прикольная судя по всему... но только начинается в версии `python3.11`




