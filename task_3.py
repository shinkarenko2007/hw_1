#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    while not wall_is_on_the_right():
<<<<<<< HEAD
          move_right()
=======
       move_right()
>>>>>>> 0471168818d62939340fe56fd71e3a52d37c458b
    pass


if __name__ == '__main__':
    run_tasks()
