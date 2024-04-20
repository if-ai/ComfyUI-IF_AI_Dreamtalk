import os
import importlib.util
import glob
import shutil
from .IFDreamTalkNode import IFDreamTalk

NODE_CLASS_MAPPINGS = {
    "IF_DreamTalk": IFDreamTalk,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IF_DreamTalk": "IF DreamTalk🧏🏻",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
