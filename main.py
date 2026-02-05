import os
import sys

def main():
    """
    A simple entry point script.
    """
    print("Application started successfully.")
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")

if __name__ == '__main__':
    main()