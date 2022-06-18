from pipeline_proj.settings.common import *
import dotenv

DEBUG = False

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ["SECRET_KEY"]


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com", "127.0.0.1"]
