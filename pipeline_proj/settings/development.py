from pipeline_proj.settings.common import *
import dotenv
import dj_database_url


DEBUG = True

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ["SECRET_KEY"]


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["NAME"],
        "USER": os.environ["USER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ["HOST"],
        "PORT": os.environ["PORT"],
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)
