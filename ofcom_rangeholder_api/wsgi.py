import sys
import os
from glob import glob

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from ofcom_rangeholder_api import app
from ofcom_rangeholder_api.datastore import Datastore
from ofcom_rangeholder_api.config import data_dir

files = glob(os.path.join(data_dir, '*'))
datastore = Datastore(*files)
application = app.build_with_datastore(datastore)
