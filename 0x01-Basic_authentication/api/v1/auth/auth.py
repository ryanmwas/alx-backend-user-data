#!/usr/bin/env python3
"""
This class manages the API Authentication
"""
from flask import request
from typing import TypeVar


class Auth:
    """ Manage API Authentication """
    def require_auth(
            self,
            path: str,
            excluded_paths: list[str]
            ) -> bool:
        """ Will be handled later """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ The request will be a flask object """
        return None
