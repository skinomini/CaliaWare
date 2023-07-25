import os
import logging
from pathlib import Path
import json
import ast


ROOT = Path(__file__).parent.absolute()

def save_settings(settings: dict):
    with open(ROOT / 'config.json', 'w') as f:
        json.dump(settings, f, indent=4)


def load_default_settings() -> dict:
    with open(ROOT / 'configDefault.json') as f:
        return json.load(f)


def load_settings() -> dict:
    with open(ROOT / 'config.json', 'r') as f:
        return json.load(f)


def check_version(current: dict, default: dict):
    if current['version'] != default['version']:
        logging.warning(f'local version {current["version"]} does not match default version, config will be updated')
        new_settings = default | current
        new_settings['version'] = default['version']
        save_settings(new_settings)
        logging.info('wrote updated config to config.json')


def handle_wallpaper_initialization(settings: dict):
    default_wallpaper_dict = {'default': 'wallpaper.png'}
    logging.info('converting wallpaper string to dict')
    try:
        if settings['wallpaperDat'] == 'WPAPER_DEF':
            logging.info('default wallpaper data used')
            settings['wallpaperDat'] = default_wallpaper_dict
        else:
            print(settings['wallpaperDat'])
            if type(settings['wallpaperDat']) == dict:
                logging.info('wallpaperdat already dict')
                print('passed')
            else:
                settings['wallpaperDat'] = ast.literal_eval(settings['wallpaperDat'].replace('\\', '/'))
                logging.info('parsed wallpaper dict from string')
    except Exception as e:
        settings['wallpaperDat'] = default_wallpaper_dict
        logging.warning(f'failed to parse wallpaper from string, using default value instead\n\tReason: {e}')


default = load_default_settings()
if not (ROOT / 'config.json').exists():
    save_settings(default)
settings = load_settings()
check_version(settings, default)
handle_wallpaper_initialization(settings)

class Settings:
    RAW = settings

    DESKTOP_ROOT = os.path.join(os.environ['USERPROFILE'], 'Desktop') #desktop path for making shortcuts
    AVOID_LIST = ['EdgeWare', 'AppData'] #default avoid list for fill/replace
    FILE_TYPES = ['png', 'jpg', 'jpeg'] #recognized file types for replace
    RESOURCE_DIR = ROOT / 'resource'
    RESOURCE_ROOTS = [RESOURCE_DIR, RESOURCE_DIR / 'aud', RESOURCE_DIR / 'img', RESOURCE_DIR / 'vid']

    LIVE_FILL_THREADS = 0 #count of live threads for hard drive filling
    PLAYING_AUDIO = False #audio thread flag
    REPLACING_LIVE = False #replace thread flag
    HAS_PROMPTS = False #can use prompts flag
    MITOSIS_LIVE = False #flag for if the mitosis mode popup has been spawned

    #default data for generating working default asset resource folder
    DEFAULT_WEB = '{"urls":["https://duckduckgo.com/"], "args":["?q=why+are+you+gay"]}'
    DEFAULT_PROMPT = '{"moods":["no moods"], "freqList":[100], "minLen":1, "maxLen":1, "no moods":["no prompts"]}'
    DEFAULT_DISCORD = 'Playing with myself~'

    #naming each used variable from config for ease of use later
    #annoyance vars
    DELAY = settings['delay']
    POPUP_CHANCE = settings['popupMod']
    AUDIO_CHANCE = settings['audioMod']
    PROMPT_CHANCE = settings['promptMod']
    VIDEO_CHANCE = settings['vidMod']
    WEB_CHANCE = settings['webMod']

    VIDEOS_ONLY = settings['onlyVid']

    PANIC_DISABLED = settings['panicDisabled']

    #mode vars
    SHOW_ON_DISCORD = settings['showDiscord']
    LOADING_FLAIR = settings['showLoadingFlair']

    DOWNLOAD_ENABLED = settings['downloadEnabled']
    USE_WEB_RESOURCE = settings['useWebResource']

    MAX_FILL_THREADS = int(settings['maxFillThreads'])

    HIBERNATE_MODE = settings['hibernateMode']
    HIBERNATE_MIN = settings['hibernateMin']
    HIBERNATE_MAX = settings['hibernateMax']
    WAKEUP_ACTIVITY = settings['wakeupActivity']

    FILL_MODE = settings['fill']
    FILL_DELAY = settings['fill_delay']
    REPLACE_MODE = settings['replace']
    REPLACE_THRESHOLD = settings['replaceThresh']

    ROTATE_WALLPAPER = settings['rotateWallpaper']

    MITOSIS_MODE = settings['mitosisMode']
    LOWKEY_MODE = settings['lkToggle']

    TIMER_MODE = settings['timerMode']

    DRIVE_ROOT = settings['drivePath']
