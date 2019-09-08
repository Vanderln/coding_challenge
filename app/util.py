#!/usr/bin/env python
"""
@author bvanderlaan
"""


def combine_objects(obj1, obj2):
    """
   Adds the individual properties of two objects together
   :param obj1:  object
   :param obj2: object
   :return: combined object
   """
    for key in obj1.__dict__:
        if key in obj2.__dict__:
            obj1.__dict__[key] = obj1.__dict__[key] + obj2.__dict__[key]
    return obj1
