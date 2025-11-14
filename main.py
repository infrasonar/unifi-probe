from libprobe.probe import Probe
from lib.check.unifi import CheckUnifi
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckUnifi,
    )

    probe = Probe("unifi", version, checks)

    probe.start()
