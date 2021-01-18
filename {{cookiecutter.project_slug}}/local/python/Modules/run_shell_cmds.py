from subprocess import Popen, PIPE


#  r u n _ s h e l l _ c m d s
#  Standard function for consistent method to run shell commands
def run_shell_cmds(cmds):

    process = Popen(
        cmds,
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )
#         universal_newlines=True,

    try:
        stdout, stderr = process.communicate()
    finally:
        rc = process.returncode

    return rc, stdout, stderr


def check_destination(destination):
    cmd = f'test -d {destination}'
    return run_shell_cmds(cmd)

