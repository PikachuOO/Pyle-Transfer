import datetime
import md5
import socket
import sys
import os

RECV_BUFFER     = 576

def init_recv_socket(address):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(address)
    udp_socket.setblocking(True)
    return udp_socket

def init_send_socket(address):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(address)
    udp_socket.setblocking(True)
    return udp_socket