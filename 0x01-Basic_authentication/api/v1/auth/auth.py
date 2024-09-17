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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None - no authorization header provided
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - no user is currently authenticated
        """
        return None
