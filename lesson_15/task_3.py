import logging
from datetime import datetime
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='date.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)

MONTHS = ("", 'янв', 'фев', 'мар', "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
WEEKDAYS = ("по", "вт", "ср", "че", "пя", "су", "во")


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем дату datetime из строки')
    parser.add_argument('--count', default='1')
    parser.add_argument('--weekday', default=datetime.now().weekday())
    parser.add_argument('--month', default=datetime.now().month)
    args = parser.parse_args()
    print(args)
    weekday = WEEKDAYS[args.weekday] if isinstance(args.weekday, int) else args.weekday
    month = MONTHS[args.month] if isinstance(args.month, int) else args.month
    return get_date(f'{args.count} {weekday} {month}')


def get_date(string: str) -> datetime:
    year = datetime.now().year
    count, weekday, month = string.split()
    month = MONTHS.index(month[:3])
    weekday = WEEKDAYS.index(weekday[:2])
    count = int(count[0])
    spam_count = 0
    for day in range(1, 31 + 1):
        try:
            date = datetime(day=day, month=month, year=year)
            if date.weekday() == weekday:
                spam_count += 1
                if spam_count == count:
                    return date
        except ValueError:
            logger.info(string)


if __name__ == '__main__':
    # print(get_date('3-я среда мая'))
    # print(get_date('1-й четверг ноября'))
    # print(get_date('6-й четверг ноября'))
    print(parser_func())
