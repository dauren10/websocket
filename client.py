
# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "wss://s3842.ams1.piesocket.com/v3/1?api_key=qunmkym6f1Wv3jD71t7qvMRuEfqo1lEHYOE6BiPo&notify_self"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        
        # Stay alive forever, listening to incoming msgs
        while True:
            
            msg = await ws.recv()
            print(msg)

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())