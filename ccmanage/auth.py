import os
import sys

import keystoneauth1 as ksa
import keystoneauth1.loading
import keystoneauth1.session

from hammers import osapi


OS_ENV_PREFIX = 'OS_'


def add_arguments(parser):
    """
    Inject our args into the user's parser
    """
    parser.add_argument('--osrc', type=str,
        help='OpenStack parameters file that overrides envvars.')


def auth_from_rc(rc):
    """
    Generates a Keystone Auth object from an OS parameter dictionary.  Dict
    key format is the same as environment variables.

    We do some dumb gymnastics because everything expects the parameters
    in their own cap/delim format:
    * envvar name:          OS_AUTH_URL
    * loader option name:      auth-url
    * loader argument name:    auth_url
    """
    assert all(key.startswith(OS_ENV_PREFIX) for key in rc)
    rc_opt_keymap = {key[3:].lower().replace('_', '-'): key for key in rc}
    loader = ksa.loading.get_plugin_loader('password')
    credentials = {}
    for opt in loader.get_options():
        if opt.name not in rc_opt_keymap:
            continue
        credentials[opt.name.replace('-', '_')] = rc[rc_opt_keymap[opt.name]]
    auth = loader.load_from_options(**credentials)
    return auth


def session_from_args(args):
    """
    Combine the provided args with the environment vars and produce a Keystone
    session for use by clients.
    """
    os_vars = {k: os.environ[k] for k in os.environ if k.startswith(OS_ENV_PREFIX)}
    if args.osrc:
        os_vars.update(osapi.load_osrc(args.osrc))
    try:
        return ksa.session.Session(auth=auth_from_rc(os_vars))
    except ksa.exceptions.auth_plugins.MissingRequiredOptions as e:
        print(
            'Missing required OS values in env/rcfile ({})'
            .format(str(e)),
            file=sys.stderr
        )
        return -1
