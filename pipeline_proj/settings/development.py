# from pipeline_proj.settings.common import *
# import dotenv

# DEBUG = True

# dotenv_file = os.path.join(BASE_DIR, ".env")
# if os.path.isfile(dotenv_file):
#     dotenv.load_dotenv(dotenv_file)

# SECRET_KEY = os.environ["SECRET_KEY"]


# # SECURITY WARNING: don't run with debug turned on in production!

# ALLOWED_HOSTS = ["127.0.0.1"]


# ---------------------------  Production.py not running?

from pipeline_proj.settings.common import *


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com"]


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# dropbox
DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"


DBX_TOKEN = os.environ.get("DBX_TOKEN")
DROPBOX_OAUTH2_TOKEN = DBX_TOKEN

DROPBOX_ROOT_PATH = "/media/"
