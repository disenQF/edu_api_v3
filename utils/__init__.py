#!/usr/bin/python3
# coding: utf-8

from redis import Redis

rd = Redis(host='10.36.174.19',
           db=9,
           decode_responses=True)
