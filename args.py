import os
from dotenv import load_dotenv


def env_args():
    load_dotenv()

    local_path = os.getenv("SD_LOCAL_FILE_PATH") or None
    remote_path = os.getenv("SD_REMOTE_TRANSFER_PATH") or None

    return [local_path, remote_path]