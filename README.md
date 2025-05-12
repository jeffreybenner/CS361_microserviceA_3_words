# How to request and receive data from the microservice

> RUBRIC: README in screenshot(s) clearly describes how to request and receive data from the microservice you implemented.
> Include example calls.
> 
Microservice A server is named `three_words_server.py` and can be downloaded 
from this [Github repository link](https://github.com/jeffreybenner/CS361_microserviceA_3_words):

To run this server, make sure you have the following Python packages installed:

```shell
pip install RandomWords
pip install ZeroMQ
```

This server was tested on Python 3.13. Execute the server, which will run on ZeroMQ port 8765, with the following command:

```shell
python three_words_server.py
```

Your client will request the message via the request string 'words' and will receive a string of three concatenated, 
comma-delimited random words as response.

Here is a client code snippet that demonstrates how to request and receive data from the server:

```python
import zmq # For ZeroMQ

# How to create a context and socket
context = zmq.Context()
# Configure REQ - request socket
socket = context.socket(zmq.REQ)

# Connect socket to address string: tcp://localhost:8765
# Server must be running on this port or the client will hang
socket.connect("tcp://localhost:8765")

# How to send request to server
socket.send_string("words")

# How to receive a response - message response is string data type
response: str = socket.recv().decode()
print(f"Received 3 random words: {response}")
```

# UML Sequence Diagram
> RUBRIC: README in screenshot(s) has UML sequence diagram that clearly communicates how to request and receive data
> from the microservice you implemented; No obvious notational errors

![Sequence Diagram-three-words.png](Sequence%20Diagram-three-words.png)


