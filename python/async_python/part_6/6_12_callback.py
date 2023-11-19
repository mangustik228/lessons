import asyncio


# Асинхронная функция, имитирующая асинхронную операцию (тренер занимается другими делами)
async def simulate_async_operation():
    await asyncio.sleep(3)


# Callback-функция, которая вызывается, когда тренировка начинается
def notify_start_training(task):
    print("Тренировка начинается, идите в спортзал.")


# Callback-функция, которая вызывается, когда тренировка отменяется
def cancel_training(task):
    print("Тренировка отменена.")

# Асинхронная функция для подготовки тренировки


async def prepare_training():
    await simulate_async_operation()

# Основная асинхронная функция


async def main(is_training_scheduled):
    # Создание задачи из асинхронной функции prepare_training
    task = asyncio.create_task(prepare_training())
    # Регистрация callback-функций
    task.add_done_callback(notify_start_training)
    task.add_done_callback(cancel_training)
    # Если тренировка назначена, удаляем callback-функцию cancel_training
    if is_training_scheduled:
        task.remove_done_callback(cancel_training)
    # Если тренировка отменена, удаляем callback-функцию notify_start_training
    else:
        task.remove_done_callback(notify_start_training)
    await task                                          # Ждем завершения задачи

# Флаг для определения состояния тренировки:
# True - тренировка назначена
# False - тренировка отменена
asyncio.run(main(True))
