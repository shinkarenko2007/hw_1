#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    while not wall_is_on_the_right():
       move_right()
    pass


if __name__ == '__main__':
    run_tasks()
