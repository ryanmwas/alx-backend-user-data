#!/usr/bin/env python3
"""
Manage the API Authentication
This class is the template for all authentications
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Manage API Authentication """
    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        """ Will be handled later """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ The request will be a flask object """
        return None
