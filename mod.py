from MeowerBot import Client
from requests import get, post
from os import (environ as env, system as run, getpid as pid)
from time import sleep
from better_profanity import profanity
import sys
import json
from random import randint, choice
#import keepalive

prefix = 'Hey,'
commands = ['newmeme','meme','inform','say','spam','world-status','save','run','wait']
tips = ['Bored? Try the new "meme" command!','Are you a nerd looking for the bots specs? Try the "inform" command!','Need help? Try the-','Tired of using a boring prefix? Try the "run" command!']
whitelist = ['https://u.cubeupload.com']
file = open('memes','r')
memes = ''.join(file.readlines()).split('\n')
file.close()
http_status = [
    {
        "status": 100,
        "message": "Continue "
    },
    {
        "status": 101,
        "message": "Switching Protocols "
    },
    {
        "status": 102,
        "message": "Processing "
    },
    {
        "status": 200,
        "message": "OK "
    },
    {
        "status": 201,
        "message": "Created "
    },
    {
        "status": 202,
        "message": "Accepted "
    },
    {
        "status": 203,
        "message": "Non - authoritative Information "
    },
    {
        "status": 204,
        "message": "No Content "
    },
    {
        "status": 205,
        "message": "Reset Content "
    },
    {
        "status": 206,
        "message": "Partial Content "
    },
    {
        "status": 207,
        "message": "Multi - Status "
    },
    {
        "status": 208,
        "message": "Already Reported "
    },
    {
        "status": 226,
        "message": "IM Used "
    },
    {
        "status": 300,
        "message": "Multiple Choices "
    },
    {
        "status": 301,
        "message": "Moved Permanently "
    },
    {
        "status": 302,
        "message": "Found "
    },
    {
        "status": 303,
        "message": "See Other "
    },
    {
        "status": 304,
        "message": "Not Modified "
    },
    {
        "status": 305,
        "message": "Use Proxy "
    },
    {
        "status": 307,
        "message": "Temporary Redirect "
    },
    {
        "status": 308,
        "message": "Permanent Redirect "
    },
    {
        "status": 400,
        "message": "Bad Request "
    },
    {
        "status": 401,
        "message": "Unauthorized "
    },
    {
        "status": 402,
        "message": "Payment Required "
    },
    {
        "status": 403,
        "message": "Forbidden "
    },
    {
        "status": 404,
        "message": "Not Found "
    },
    {
        "status": 405,
        "message": "Method Not Allowed "
    },
    {
        "status": 406,
        "message": "Not Acceptable "
    },
    {
        "status": 407,
        "message": "Proxy Authentication Required "
    },
    {
        "status": 408,
        "message": "Request Timeout "
    },
    {
        "status": 409,
        "message": "Conflict "
    },
    {
        "status": 410,
        "message": "Gone "
    },
    {
        "status": 411,
        "message": "Length Required "
    },
    {
        "status": 412,
        "message": "Precondition Failed "
    },
    {
        "status": 413,
        "message": "Payload Too Large "
    },
    {
        "status": 414,
        "message": "Request - URI Too Long "
    },
    {
        "status": 415,
        "message": "Unsupported Media Type "
    },
    {
        "status": 416,
        "message": "Requested Range Not Satisfiable "
    },
    {
        "status": 417,
        "message": "Expectation Failed "
    },
    {
        "status": 418,
        "message": "I’m a teapot "
    },
    {
        "status": 421,
        "message": "Misdirected Request "
    },
    {
        "status": 422,
        "message": "Unprocessable Entity "
    },
    {
        "status": 423,
        "message": "Locked "
    },
    {
        "status": 424,
        "message": "Failed Dependency "
    },
    {
        "status": 426,
        "message": "Upgrade Required "
    },
    {
        "status": 429,
        "message": "Too Many Requests "
    },
    {
        "status": 431,
        "message": "Request Header Fields Too Large "
    },
    {
        "status": 444,
        "message": "Connection Closed Without Response "
    },
    {
        "status": 451,
        "message": "Unavailable For Legal Reasons "
    },
    {
        "status": 499,
        "message": "Client Closed Request "
    },
    {
        "status": 500,
        "message": "Internal Server Error "
    },
    {
        "status": 501,
        "message": "Not Implemented "
    },
    {
        "status": 502,
        "message": "Bad Gateway "
    },
    {
        "status": 503,
        "message": "Service Unavailable "
    },
    {
        "status": 504,
        "message": "Gateway Timeout "
    },
    {
        "status": 505,
        "message": "HTTP Version Not Supported "
    },
    {
        "status": 506,
        "message": "Variant Also Negotiates "
    },
    {
        "status": 507,
        "message": "Insufficient Storage "
    },
    {
        "status": 508,
        "message": "Loop Detected "
    },
    {
        "status": 510,
        "message": "Not Extended "
    },
    {
        "status": 511,
        "message": "Network Authentication Required "
    },
    {
        "status": 599,
        "message": "Network Connect Timeout Error"
    },
]