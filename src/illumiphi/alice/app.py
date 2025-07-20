"""
run the main app
"""
from .alice import Alice


def run() -> None:
    reply = Alice().run()
    print(reply)
