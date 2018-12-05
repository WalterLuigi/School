#!/usr/bin/env python

import zmq
context = zmq.Context()

peers = []
print("Enter your username.")
username = input("> ")

def PeerApproval(peer):
    '''
    Receives requests from broker to approve new peer
    '''

def ConnectToPeer(peer):
    '''
    Connect to all peers found in library on designated port
    '''



def main(peers):
    for peer in peers:


def sendchat(username):
    socketPUB = context.socket(zmq.PUB)
    socketPUB.bind("tcp://*:5556")
    message = input("> ")
    socketPUB.send_string("<%i>: %i" % (username, message))



socketSUB = context.socket(zmq.SUB)
socketSUB.bind()