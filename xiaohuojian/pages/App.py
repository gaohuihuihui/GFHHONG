from driver.AndroidClient import AndroidClient
from pages.MainPage import MainPage


class App(object):
    @classmethod
    def main(self):
        AndroidClient.install_app()
        return MainPage()
