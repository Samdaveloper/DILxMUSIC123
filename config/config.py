import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5333769332").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Samdaveloper/DILxMUSIC123")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN","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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/caption_marathi_status")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Marathi_Chatting_143")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
 
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID","19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET","409e31d3ddd64af08cfcc3b0f064fcbe")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION1", "BQBSIfqSeKaxilAdQR_j7cML7EhfD0x0w0VNsN5DT4nXwMXxqobkyG2aB7j6fQKdJR25TEVTjEgzwCM0px5e-sewBDRAl0KcexwwoV0zjxe_Wo8JeItQxmKypGKv2lYr5h3RRzUu_RFoL5G9r6jugzVueUzpzYfg5zQLCvR7VA-ppgNYXzpuefjxsfPGV93KTikabUui8mkWAm5eBSZ-95dIhi-XPShJ4AXFbwhOphOrn_VL1b5OYpypevUQO-kyHcxAi7arb7vSXVgo7RrwkKVrWcWmzaiW00acyGPYULasPSzEHLjWGv-dul0eS20qjulu3SftwNnk2vHxkU15s-R0M_HndwA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/2216295471987f377677c.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/2216295471987f377677c.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/810f874873e1565cf5732.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/16d7dd76f4ce8b8b01fdf.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/2216295471987f377677c.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/2216295471987f377677c.jpg"
