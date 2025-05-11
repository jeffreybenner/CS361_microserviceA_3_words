# Test client for the three_words_server.py
# Author: Jeffrey Benner (bennerj)
# Assignment 8 S.2.6 Microservice A for Colin Maloney
# 2025-05-10
# CS361 week 6 module

# This code connects (binds) to port 8765 on your local
# machine, it then waits for a message from the client.
# If it receives a message string "words" then this server will
# generate a comma-delimited string of 3 words and send it back to the client.

import time # For time.sleep()
import zmq # For ZeroMQ


context = zmq.Context()
# Configure REQ - request socket
socket = context.socket(zmq.REQ)

# Connect socket to address string: protocol://interface:port
socket.connect("tcp://localhost:8765")

# Main prompt loop
while True:
    user_input = input("Do you want 3 random words? (y/n/q to quit server): ").lower().strip()

    if user_input in ['y', 'yes']:
        # Send message request string
        socket.send_string('words')
        # Wait for response
        response = socket.recv().decode()
        print(f"Received 3 random words: {response}")
    elif user_input in ['q', 'quit']:
        # Send quit command to server
        socket.send_string('Q')
        print("Quitting...")
        break
    else:
        # Clear prompt and continue
        print("Invalid input. Please try again.")

    print()  # Add blank line between prompts
