import datetime as dt
from typing import Any, Optional


class Record:
    """Класс для приведения записей в соответствующий вид"""
    def __init__(self, amount: float, comment: str,
                 date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date()

    def __str__(self) -> str:
        return f'{self.amount}, {self.comment}, {self.date}'


class Calculator:
    """Класс для сохранения записи, подсчета денег/калорий
        за день или неделю"""
    def __init__(self, limit: float) -> None:
        """Аннотация типов"""
        self.limit = limit
        self.records: list[Any] = []

    def add_record(self, record: Any) -> None:
        """Сохранение записи в список"""
        self.records.append(record)

    def get_today_stats(self) -> float:
        """Подсчет денег/калорий за день"""
        today_stats = 0
        date_today = dt.date.today()
        for record in self.records:
            if record.date == date_today:
                today_stats += record.amount
                sum(record.amount for record in self.records)
        return today_stats

    def get_week_stats(self) -> float:
        """Подсчет денег/калорий за неделю"""
        week_stats = 0
        week_ago = dt.date.today() - dt.timedelta(days=6)
        for record in self.records:
            if week_ago <= record.date <= dt.date.today():
                week_stats += record.amount
        return week_stats


class CashCalculator(Calculator):
    """Подсчитывает финансовое состояние на сегодняшний
    день в зависимости от лимита и валюты"""
    USD_RATE: float = 72.7
    EURO_RATE: float = 86.5

    def get_today_cash_remained(self, currency: str) -> str:
        """Сравнение финансового состояния с лимитом и вывод результата"""
        spent = self.get_today_stats()
        difference = spent - self.limit
        if currency == 'rub':
            diff = round(difference, 2)
            currency = 'руб'
        elif currency == 'usd':
            diff = round((difference / self.USD_RATE), 2)
            currency = 'USD'
        else:
            diff = round((difference / self.EURO_RATE), 2)
            currency = 'Euro'
        if spent > self.limit:
            return f'Денег нет, держись: твой долг - {diff} {currency}'
        elif spent == self.limit:
            return 'Денег нет, держись'
        else:
            return f'На сегодня осталось {abs(diff)} {currency}'


class CaloriesCalculator(Calculator):
    """Выводит результат в зависимости от лимита"""
    def get_calories_remained(self) -> str:
        """Сравнение кол-ва калорий с лимитом и вывод результата"""
        consumed_calories = self.get_today_stats()
        if consumed_calories < self.limit:
            difference = self.limit - consumed_calories
            return ('Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {difference} кКал')
        return 'Хватит есть!'
