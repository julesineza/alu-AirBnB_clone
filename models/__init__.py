#!/usr/bin/python3
"""
Initialize models package
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Load data from file if it exists
storage.reload()