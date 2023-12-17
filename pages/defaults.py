from splashes.splash_screens import DEFAULT_SPLASH_PATH, PNG_EXT
from pages.modules.scroller import Scroller


class DefaultsPage(Scroller):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, DEFAULT_SPLASH_PATH, PNG_EXT)
