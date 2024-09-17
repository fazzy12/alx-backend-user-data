#!/usr/bin/env python3
"""
Auth module for handling authentication.
"""
import base64
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


    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the
        Authorization header for Basic Authentication."""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None
        # Return the part after "Basic "
        return authorization_header[len("Basic "):]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 part of the Authorization header.
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
