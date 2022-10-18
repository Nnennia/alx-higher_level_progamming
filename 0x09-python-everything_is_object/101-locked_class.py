#!/usr/bin/pythoss
"""Defines a locked class"""


class LockedClass:
    """Prevent the user from instantiating new LockeClass attributes"""
    _slots__ = ["first_name"]
