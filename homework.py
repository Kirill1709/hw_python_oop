import datetime as dt
from typing import List, Optional

FORMAT: str = '%d.%m.%Y'


class Record:
    """Класс для приведения записей в соответствующий вид."""

    def __init__(self, amount: float, comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, FORMAT).date()

    def __str__(self) -> str:
        return f'{self.amount}, {self.comment}, {self.date}'


class Calculator:
    """Класс для сохранения записи, подсчета денег/калорий
        за день или неделю."""
    def __init__(self, limit: float) -> None:
        """Аннотация типов."""
        self.limit = limit
        self.records: List['Record'] = []

    def add_record(self, record: 'Record') -> None:
        """Сохранение записи в список."""
        self.records.append(record)

    def get_today_stats(self) -> float:
        """Подсчет денег/калорий за день."""
        date_today = dt.date.today()
        return sum(record.amount for record in self.records
                   if record.date == date_today)

    def get_week_stats(self) -> float:
        """Подсчет денег/калорий за неделю."""
        date_today = dt.date.today()
        week_ago = date_today - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                   if week_ago < record.date <= date_today)

    def limit_stats(self) -> float:
        """Вычисление разницы между лимитом и
        количеством денег/калорий за сегодняшний день."""
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    """Подсчитывает финансовое состояние на сегодняшний
    день в зависимости от лимита и валюты."""
    USD_RATE: float = 72.7
    EURO_RATE: float = 86.5
    RUB_RATE: int = 1

    def get_today_cash_remained(self, currency: str) -> str:
        """Сравнение финансового состояния с лимитом и вывод результата."""
        difference = self.limit_stats()
        if difference == 0:
            return 'Денег нет, держись'
        currencies = {'usd': (self.USD_RATE, 'USD'),
                      'eur': (self.EURO_RATE, 'Euro'),
                      'rub': (self.RUB_RATE, 'руб')}
        if currency not in currencies:
            raise ValueError('Такой валюты в списке нет')
        currency_rate, currency_name = currencies[currency]
        quantity = round(difference / currency_rate, 2)
        if difference < 0:
            quantity = abs(quantity)
            return (f'Денег нет, держись: твой долг - '
                    f'{quantity} {currency_name}')
        return (f'На сегодня осталось {quantity} {currency_name}')


class CaloriesCalculator(Calculator):
    """Выводит результат в зависимости от лимита."""
    def get_calories_remained(self) -> str:
        """Сравнение кол-ва калорий с лимитом и вывод результата."""
        difference = self.limit_stats()
        if difference > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {difference} кКал')
        return 'Хватит есть!'
