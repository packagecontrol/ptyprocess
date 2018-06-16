import subprocess


RLIMIT_NOFILE = None


def getrlimit(resource):
    if resource == RLIMIT_NOFILE:
        soft_limit = int(subprocess.check_output(['ulimit', '-Sn']))
        hard_limit = None
        return (soft_limit, hard_limit)
