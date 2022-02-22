from s_calendar.calendar_generator import Calendar_generator
from spider.spider import Spider


def main():
    list = Spider().init()
    Calendar_generator.generate_calendar(list)


if __name__ == "__main__":
    main()
