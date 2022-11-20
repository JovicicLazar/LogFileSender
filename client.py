import asyncio
import json

class Client:
    def __init__(self):
        file = open('config.json')
        config = json.load(file)
        self.host = config['host']
        self.port = config['port_blocks']
        self.queue_size = config['client_queue_size']

    async def recieve_messages(self) -> None:
        reader, writer = await asyncio.open_connection(self.host, self.port)

        await writer.drain()

        while True:
            data = await reader.read(self.queue_size)

            if not data:
                raise Exception("socket closed")

            print(f"Recieved: {data.decode()}")

    def start_client(self) -> None:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.recieve_messages())

if __name__ == '__main__':
    client = Client()
    client.start_client()