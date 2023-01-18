from libprobe.probe import Probe
from lib.check.unifi import check_unifi
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'unifi': check_unifi
    }

    probe = Probe("unifi", version, checks)

    probe.start()
