#!/usr/bin/env python3
"""
Auth module for handling authentication.
"""
from typing import List, TypeVar
from flask import request

class Auth:
    """Auth class for API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False - authentication not yet implemented
        """
        if path is None:
           return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True


    def authorization_header(self, request=None) -> str:
        """
        Returns None - no authorization header provided
        """
        if request is None:
            return True

        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - no user is currently authenticated
        """
        return None
