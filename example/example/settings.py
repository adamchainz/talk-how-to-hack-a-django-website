import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "vj%*ft9%*%t04j*m!nn2_mt-vp1$s*phu(z+-2(c)1=wwa0v9s"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "example.core",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

# TEST_RUNNER = "example.superfast.SuperFastTestRunner"
TEST_RUNNER = "example.test.EmojiTestRunner"
