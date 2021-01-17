'''
{{cookiecutter.app_name}} - 
'''

import config
import logging
import subprocess
import sys

from run_shell_cmds import run_shell_cmds


def std_begin():
    logging.info("{{cookiecutter.app_name}} is starting...")


def std_end(rc=0, sysout=None, syserr=None, gword=None):
    logging.shutdown()
    sys.stdout.flush()
    sys.exit(rc)


def get_config():
    my_config = config.Config('{{cookiecutter.app_name}}.yaml')
    return my_config 


def main():
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])
    logging.info("begin main()")

    std_begin()
    my_config = get_config()

    #  Test that the destination for the output is available.
    rc, stdout, stderr = check_destination(destination)
    if rc:
        std_end2(rc)

    #  Build the command string.
    cmd = build_command_string("echo \"Hello World from {{ cookiecutter.app_name }}!\"")

    #  Run the command.
    rc, stdout, stderr = run_shell_cmds(cmd)
    sys.stdout.buffer.write(stdout)
    if not rc:
        sys.stderr.buffer.write(stderr)

    std_end(rc, stdout, stderr)


if __name__ == "__main__":
    main()
