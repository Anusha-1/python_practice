import asyncio
#async/await

async def upload(): #cororutine1
    print('upload is active on the event loop and yielding control')
    await asyncio.sleep(4)  #await means second co routine starts
    print('upload completed')


async def download():  #coroutine2
    print('download is active on the event loop and yielding control')
    await asyncio.sleep(5)
    print('download completed')


if __name__=='__main__':
    print("parallel tasks started")
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather())
    loop.run_until_complete(asyncio.gather(upload(),download()))
    print("All works done")


    #kernel mode native threads  = os level threads

    #no dependencies use this usecase
