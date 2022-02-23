from calendar_controller.calendar_generator import Calendar_generator
from selenium_controller.auto_auth import AutoAuth
from spider.spider import Spider


def main():
    list = Spider(auth_token=AutoAuth().init()).init()
    Calendar_generator.generate_calendar(list)


if __name__ == "__main__":
    main()
