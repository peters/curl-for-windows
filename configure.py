import optparse
import os
import sys
import shutil

script_dir = os.path.dirname(__file__)
root_dir = os.path.normpath(script_dir)
output_dir = os.path.join(os.path.abspath(root_dir), 'out')
ninja_root = os.path.join(os.path.abspath(root_dir), 'build\\ninja')
curl_root = os.path.join(os.path.abspath(root_dir), 'curl')

sys.path.insert(0, os.path.join(root_dir, 'build', 'gyp', 'pylib'))

try:
    import gyp
except ImportError:
    print('You need to install gyp in build/gyp first. See the README.')
    sys.exit(42)

# parse our options
parser = optparse.OptionParser()

parser.add_option("--debug",
                  action="store_true",
                  dest="debug",
                  help="Also build debug build")

parser.add_option("--ninja",
                  action="store_true",
                  dest="use_ninja",
                  help="Generate files for the ninja build system")

parser.add_option("--msvs",
                  action="store_true",
                  dest="use_msvs",
                  help="Generate files for the msvs build system")

parser.add_option("--msvs-toolchain",
                  action="store",
                  type="choice",
                  dest="msvs_toolchain",
                  choices=[2008, 2010, 2012],
                  help="msvs toolchain to build for. [default: %default]",
                  default=2012)

parser.add_option("--target-arch",
                  action="store",
                  dest="target_arch",
                  type='choice',
                  choices=['x86', 'x64'],
                  help="CPU architecture to build for. [default: %default]",
                  default='x86')

(options, args) = parser.parse_args()


def getoption(value, default):
    if not value:
        return default
    return value


def os_env_scan(target, executable):
    """
    Scan for executable presence in a given environment variable
    :param target: environment variable type, i.e "PATH"
    :param executable: executable name, i.e "ninja.exe"
    """
    for p in os.environ[target].split(os.pathsep):
        if os.path.exists(os.path.join(p, executable)):
            return True
    return False


def configure_defines(o):
    """
    Configures libcurl
    """
    o.append('-D=target_arch=' + getoption(options.target_arch, host_arch_win()))
    o.append('-D=library=static_library')


def configure_buildsystem(o):
    """
    Configures buildsystem
    """

    # gyp target
    args.append(os.path.join(root_dir, 'curl.gyp'))

    # includes
    args.extend(['-I', os.path.join(root_dir, 'common.gypi')])

    # msvs
    if options.use_msvs:
        o.extend(['-f', 'msvs'])
        o.append('--generator-output=' + output_dir)
        if options.msvs_toolchain:
            o.extend(['-G', str(options.msvs_toolchain)])
    else:
        o.extend(['-f', 'ninja'])
        # check for ninja presence globally
        if not os_env_scan('PATH', 'ninja.exe'):
            # add our own ninja version
            os.environ['PATH'] += os.pathsep + ninja_root
            # ninja probably not compiled
            if not os_env_scan('PATH', 'ninja.exe'):
                print "Ninja not found. Did you forget to compile it? Please see README."
            sys.exit(42)

    # generic
    o.append('--depth=' + root_dir)
    o.extend(['--build', 'Release'])

    # also build debug release
    if options.debug:
        o.extend(['--build', 'Debug'])

    # copy curlbuild.h
    shutil.copy(os.path.join(root_dir, "curlbuild.h"),
                os.path.join(curl_root, "include\\curl\\curlbuild.h"))


def host_arch_win():
    """Host architecture check using environ vars (better way to do this?)"""

    arch = os.environ.get('PROCESSOR_ARCHITECTURE', 'x86')

    matchup = {
        'AMD64': 'x64',
        'x86': 'ia32',
    }

    return matchup.get(arch, 'ia32')


def run_gyp(args):
    """
    Executes gyp
    """
    rc = gyp.main(args)
    if rc != 0:
        print 'Error running GYP'
        sys.exit(rc)

# gyp arguments
args = []

# gyp configure
configure_buildsystem(args)
configure_defines(args)

# build
gyp_args = list(args)
print gyp_args
run_gyp(gyp_args)
