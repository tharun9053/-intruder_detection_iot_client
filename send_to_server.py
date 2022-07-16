#!/bin/python
import threading
import socketio
import time
import requests
import capture_footage
import queue


sio = socketio.Client()

@sio.event(namespace='/iot')
def failsafe_ping():
    print("Recieved ping")
    try:
        sio.emit('failsafe_response', namespace='/iot')
        print("Emitted response")
    except socketio.exceptions.BadNamespaceError: # Client not yet connected to server
        print("Not yet connected")
        time.sleep(2)
        failsafe_ping()

def stream_footage_to_server(sio):
    for data in capture_footage.recordToStream():
        sio.emit('stream_footage',data,namespace='/iot')

@sio.event(namespace='/iot')
def connect():
    print("Starting to stream")
    sio.emit('start_pinging',namespace='/iot')
    sio.start_background_task(stream_footage_to_server, sio)
    

if __name__ == '__main__':
    sio.connect("http://54.244.102.39:80",namespaces=['/iot'])
    while(not sio.connected):
        print("Waiting to connect")
        time.sleep(2)
    
