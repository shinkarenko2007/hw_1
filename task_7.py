#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
          move_down()
    while wall_is_beneath():
          move_right()
    while not wall_is_beneath():
          move_down()
    while wall_is_above():
          move_left()
    pass


if __name__ == '__main__':
    run_tasks()
