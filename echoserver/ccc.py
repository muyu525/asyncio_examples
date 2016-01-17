import asyncio
from multiprocessing import Process

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        #print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        #print('Data received: {!r}'.format(data.decode()))
        pass

    def connection_lost(self, exc):
        #print('The server closed the connection')
        #print('Stop the event lop')
        self.loop.stop()


def client(msg):
    loop = asyncio.get_event_loop()
    message = 'Hello World!'
    coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                                  '127.0.0.1', 8888)

    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    import time
    start = time.time()
    for num in range(1000):
        Process(target=client, args=("1")).start()
    end = time.time()
    print("over,interval:", end - start)

