from splashes.splash_screens import BACKUP_SPLASH_PATH, BACKUP_EXT
from pages.modules.scroller import Scroller


class BackupsPage(Scroller):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, BACKUP_SPLASH_PATH, BACKUP_EXT)
