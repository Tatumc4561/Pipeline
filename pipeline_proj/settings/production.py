from pipeline_proj.settings.common import *


DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com"]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# dropbox
DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"

DBX_TOKEN = os.environ.get("DBX_TOKEN")
DROPBOX_OAUTH2_TOKEN = DBX_TOKEN
DROPBOX_ROOT_PATH = "/media/"
