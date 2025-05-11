# Generate 3-random-word-string from bennerj for CS361
# Assignment 8 S.2.6 Microservice A for Colin Maloney
# 2025-05-10
# CS361 week 6 module

# This code connects (binds) to port 8765 on your local
# machine, it then waits for a message from the client.
# If it receives a message string "words" then this server will
# generate a comma-delimited string of 3 words and send it back to the client.

import random_words
import time # For time.sleep()
import zmq # For ZeroMQ

# Setting up context for zeromq
context = zmq.Context()

# Set up REP - reply socket
socket = context.socket(zmq.REP)

# Bind socket to address string: protocol://interface:port
socket.bind("tcp://*:8765")

while True:
    time.sleep(1)
    # Try receiving a message from the client, which is any non-zero length string.
    message = socket.recv()
    print(f"I am the server, waiting for a message from the client.\n")

    if len(message) > 0:
        my_message = message.decode()
        print(f"Received request from the client: {my_message}\n")
        # Need a way to quit clean without kill -9
        if message.decode() == 'Q': # Client asked server to quit
            break
        elif message.decode() == 'words': # Client asked for 3 random words
            r = random_words.RandomWords()
            # Create a comma-delimited string of the 3 words
            myMessage = ",".join([r.random_word() for _ in range(3)])
            print(f"Sending message: {myMessage}\n")
            # Now we must send a reply back to the client.
            socket.send_string(myMessage)

# Make a clean exit (with garbage cleanup).
# Only happens if we receive a 'Q' from the client.
context.destroy()
