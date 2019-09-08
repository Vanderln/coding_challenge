#!/usr/bin/env python
from queue import Queue
from requests import get, codes
from threading import Thread


"""
A module to manage http connections and threading

@author bvanderlaan
"""


def make_call(url, headers, service, username=None, password=None):
    """
    Handles http calls to an external service
    """
    if username and password:
        response = get(url, auth=(username, password), headers=headers)
    else:
        response = get(url, headers=headers)
    if response.status_code == codes.ok:
        return response
    else:
        raise Exception(
            "Problem calling {} via: {}. Make sure your team/org is correct.".format(
                service, url
            )
        )


def each_delegate(fn, list_of_items, headers, service, username, password):
    """
    Method to create a thread for each item in a list
    """

    q = Queue()
    threads = []
    for item in list_of_items:
        t = Thread(
            name=fn,
            target=lambda q, *args: q.put(fn(*args)),
            args=(q, item, headers, service, username, password),
        )
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    responses = []
    while not q.empty():
        responses.append(q.get().content)
    return responses
