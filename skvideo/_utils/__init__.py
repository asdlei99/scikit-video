from .xmltodict import parse as xmltodictparser
import subprocess as sp

# python2 only
binary_type = str

def read_n_bytes(f, N):
    """ read_n_bytes(file, n)
    
    Read n bytes from the given file, or less if the file has less
    bytes. Returns zero bytes if the file is closed.
    """
    bb = binary_type()
    while len(bb) < N:
        extra_bytes = f.read(N-len(bb))
        if not extra_bytes:
            break
        bb += extra_bytes
    return bb

def check_dict(dic, key, valueifnot):
    if key not in dic:
        dic[key] = valueifnot


# patch for python 2.6
def check_output(*popenargs, **kwargs):
    process = sp.Popen(stdout=sp.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        error = sp.CalledProcessError(retcode, cmd)
        error.output = output
        raise error
    return output