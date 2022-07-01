from pipeline_proj.settings.common import *
import dj_database_url
import dropbox


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com"]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
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
DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"


DBX_TOKEN = os.environ["DBX_TOKEN"]
DROPBOX_OAUTH2_TOKEN = DBX_TOKEN

DROPBOX_ROOT_PATH = "/media/"


dbx = dropbox.Dropbox(DBX_TOKEN)

# create file
filename = "/local_files/file.json"
dbx.files_upload(f.read(), filename, mute=True)

# read file
filename = "/dropbox_root/file.json"
f, r = dbx.files_download(filename)
