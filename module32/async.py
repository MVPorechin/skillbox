import time
import asyncio


def first_():
    def fun1(x):
        print(x ** 2)
        time.sleep(3)
        print('fun1 завершена')

    def fun2(x):
        print(x ** 0.5)
        time.sleep(3)
        print('fun2 завершена')

    def main():
        fun1(4)
        fun2(4)

    print(time.strftime('%X'))

    main()

    print(time.strftime('%X'))


def second_():
    async def fun1(x):
        print(x ** 2)
        await asyncio.sleep(3)
        print('fun1 завершена')

    async def fun2(x):
        print(x ** 0.5)
        await asyncio.sleep(3)
        print('fun2 завершена')

    async def main():
        task1 = asyncio.create_task(fun1(4))
        task2 = asyncio.create_task(fun2(4))

        await task1
        await task2

    print(time.strftime('%X'))

    asyncio.run(main())

    print(time.strftime('%X'))


def old_():
    async def fun1(x):
        print(x ** 2)
        await asyncio.sleep(3)
        print('fun1 завершена')

    async def fun2(x):
        print(x ** 0.5)
        await asyncio.sleep(3)
        print('fun2 завершена')

    print(time.strftime('%X'))

    loop = asyncio.get_event_loop()
    task1 = loop.create_task(fun1(4))
    task2 = loop.create_task(fun2(4))
    loop.run_until_complete(asyncio.wait([task1, task2]))

    print(time.strftime('%X'))


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    print(type(task1))
    print(task1.__class__.__bases__)

    await task1
    await task2


asyncio.run(main())