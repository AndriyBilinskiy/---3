#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import DEBUG, debug, getLogger
import logging

getLogger().setLevel(DEBUG)
logging.basicConfig(filename="test.log", level = logging.DEBUG, 
format='%(asctime)s:%(funcName)s:%(message)s')

def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    debug(f"Description of the field: {l}")
parse_field_info()