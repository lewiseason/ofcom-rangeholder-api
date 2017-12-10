"""ofcom-rangeholder-api

Usage:
    ofcom-rangeholder-api update
    ofcom-rangeholder-api run [--host=<host>] [--port=<port>]

Options:
    --host=<host>    [default: 127.0.0.1]
    --port=<port>    [default: 5000]

"""

import pkg_resources
from docopt import docopt


def main():
    version = pkg_resources.get_distribution('ofcom-rangeholder-api').version
    arguments = docopt(__doc__, version=version)

    if arguments['run']:
        from werkzeug.serving import run_simple
        from .wsgi import application

        run_simple(arguments['--host'], int(arguments['--port']), application)

    elif arguments['update']:
        import os
        from six.moves import urllib
        from . import config

        try:
            os.mkdir(config.data_dir)
        except OSError:
            pass

        for url in config.remote_data_files:
            filename = os.path.join(config.data_dir, os.path.basename(url))
            urllib.request.urlretrieve(url, filename)
