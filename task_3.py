#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    move_right(8)
    wall_is_on_the_right(1)
    pass


if __name__ == '__main__':
    run_tasks()
