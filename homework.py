import datetime as dt
from typing import Any, List, Optional


class Record:
    """Класс для приведения записей в соответствующий вид."""
    FORMAT: str = '%d.%m.%Y'

    def __init__(self, amount: float, comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, self.FORMAT).date()

    def __str__(self) -> str:
        return f'{self.amount}, {self.comment}, {self.date}'


class Calculator:
    """Класс для сохранения записи, подсчета денег/калорий
        за день или неделю."""
    def __init__(self, limit: float) -> None:
        """Аннотация типов."""
        self.limit = limit
        self.records: List[Any] = []

    def add_record(self, record: Record) -> None:
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
        week_ago = date_today - dt.timedelta(days=6)
        return sum(record.amount for record in self.records
                   if week_ago <= record.date <= date_today)

    def limit_stats(self) -> float:
        return (self.get_today_stats() - self.limit)


class CashCalculator(Calculator):
    """Подсчитывает финансовое состояние на сегодняшний
    день в зависимости от лимита и валюты."""
    USD_RATE: float = 72.7
    EURO_RATE: float = 86.5
    RUB_RATE: int = 1

    def get_today_cash_remained(self, currency: str) -> str:
        """Сравнение финансового состояния с лимитом и вывод результата."""
        currencies = {'usd': (self.USD_RATE, 'USD'),
                      'eur': (self.EURO_RATE, 'Euro'),
                      'rub': (self.RUB_RATE, 'руб')}
        difference = self.limit_stats()
        spent = self.get_today_stats()
        diff = round((difference / currencies[currency][0]), 2)
        if spent > self.limit:
            return (f'Денег нет, держись: твой долг - '
                    f'{diff} {currencies[currency][1]}')
        elif spent == self.limit:
            return 'Денег нет, держись'
        return f'На сегодня осталось {abs(diff)} {currencies[currency][1]}'


class CaloriesCalculator(Calculator):
    """Выводит результат в зависимости от лимита."""
    def get_calories_remained(self) -> str:
        """Сравнение кол-ва калорий с лимитом и вывод результата."""
        consumed_calories = self.get_today_stats()
        difference = self.limit_stats()
        if consumed_calories < self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {abs(difference)} кКал')
        return 'Хватит есть!'
