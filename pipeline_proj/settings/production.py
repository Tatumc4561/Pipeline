from pipeline_proj.settings.common import *


DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["the-pipeline.herokuapp.com"]
