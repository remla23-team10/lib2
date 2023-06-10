"""Util to get metadata"""
from importlib import metadata

class VersionUtil:
    """Class to obtain current library version"""

    @classmethod
    def get_version(cls):
        """Function to obtain current library version"""
        try:
            return metadata.version('remla23-team10-preprocessing')
        except metadata.PackageNotFoundError:
            return 'Package not found'
