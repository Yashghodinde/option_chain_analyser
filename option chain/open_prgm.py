from subprocess import call
import time


def open_py_file():
    call(["python", "analyse_chain.py"])


while True:
    open_py_file()
    time.sleep(180)
