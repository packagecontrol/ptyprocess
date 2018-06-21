import subprocess


RLIMIT_NOFILE = 7


def getrlimit(resource):
    if resource == RLIMIT_NOFILE:
        soft_limit = int(subprocess.check_output(['sh', '-c', 'ulimit -Sn']))
        hard_limit = None
        return (soft_limit, hard_limit)
