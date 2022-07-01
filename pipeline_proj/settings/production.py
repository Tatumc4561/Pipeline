from pipeline_proj.settings.common import *
import dj_database_url


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com"]


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["NAME"],
        # "USER": os.environ["USER"],
        # "PASSWORD": os.environ["PASSWORD"],
        # "HOST": os.environ["HOST"],
        # "PORT": os.environ["PORT"],
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)

# dropbox

# DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"


# DBX_TOKEN = os.environ["DBX_TOKEN"]
# DROPBOX_OAUTH2_TOKEN = DBX_TOKEN

# DROPBOX_ROOT_PATH = "/media/"


# dropbox v2
# DEFAULT_FILE_STORAGE = "django_dropbox_storage.storage.DropboxStorage"

# from io import StringIO

# DBX_TOKEN = os.environ["DBX_TOKEN"]


# DROPBOX_ACCESS_TOKEN = DBX_TOKEN
# DROPBOX_ROOT_FOLDER = "/media"


# google storages

GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"]
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "the-pipeline"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
