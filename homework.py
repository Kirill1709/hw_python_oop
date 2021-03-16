import datetime as dt


class Record:
<<<<<<< HEAD
    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
=======
    def __init__(self, amount: float, comment: str, date= None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date == None:
>>>>>>> 3cb3f1f3fe6a224eb0f064100196a2cc2fed96a6
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date()

    def show(self):
        print(f'{self.amount}, {self.comment}, {self.date}')


<<<<<<< HEAD
class Calculator:
=======

class Calculator:

    def __init__(self, limit: float):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = 0
        for record in self.records:
             if record.date == dt.date.today():
                today += record.amount
        return today

    def get_week_stats(self):
        week = 0
        week_ago = dt.date.today() - dt.timedelta(days=6) 
        for record in self.records:
            if record.date >= week_ago and record.date <= dt.date.today():
                week += record.amount
        return week

class CashCalculator(Calculator):
    USD_RATE: float = 72.7
    EURO_RATE: float = 86.5

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            if self.get_today_stats() > self.limit:
                difference = self.get_today_stats() - self.limit
                return f'Денег нет, держись: твой долг - {difference} руб'
            elif self.get_today_stats() == self.limit:
                return f'Денег нет, держись'
            else:
                difference = self.limit - self.get_today_stats()
                return f'На сегодня осталось {difference} руб'
        if currency == 'usd': 
            if self.get_today_stats() > self.limit:
                difference = round((self.get_today_stats() - self.limit)/ self.USD_RATE, 2)
                return f'Денег нет, держись: твой долг - {difference} USD'
            elif self.get_today_stats() == self.limit:
                return f'Денег нет, держись'
            else:
                difference = round((self.limit - self.get_today_stats()) / self.USD_RATE, 2)
                return f'На сегодня осталось {difference} USD'
        if currency == 'eur': 
            if self.get_today_stats() > self.limit:
                difference = round((self.get_today_stats() - self.limit)/ self.EURO_RATE, 2)
                return f'Денег нет, держись: твой долг - {difference} Euro'
            elif self.get_today_stats() == self.limit:
                return f'Денег нет, держись'
            else:
                difference = round((self.limit - self.get_today_stats()) / self.EURO_RATE, 2)
                return f'На сегодня осталось {difference} Euro'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if  self.get_today_stats() < self.limit:
            difference = self.limit - self.get_today_stats()
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {difference} кКал'
        else:
            return f'Хватит есть!'

>>>>>>> 3cb3f1f3fe6a224eb0f064100196a2cc2fed96a6

    def __init__(self, limit: float):
        self.limit = limit
        self.records = []

<<<<<<< HEAD
    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = 0
        for record in self.records:
            if record.date == dt.date.today():
                today += record.amount
        return today

    def get_week_stats(self):
        week = 0
        week_ago = dt.date.today() - dt.timedelta(days=6)
        for record in self.records:
            if record.date >= week_ago and record.date <= dt.date.today():
                week += record.amount
        return week


class CashCalculator(Calculator):
    USD_RATE: float = 72.7
    EURO_RATE: float = 86.5

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            if self.get_today_stats() > self.limit:
                difference = self.get_today_stats() - self.limit
                return f'Денег нет, держись: твой долг - {difference} руб'
            elif self.get_today_stats() == self.limit:
                return 'Денег нет, держись'
            else:
                difference = self.limit - self.get_today_stats()
                return f'На сегодня осталось {difference} руб'
        if currency == 'usd':
            if self.get_today_stats() > self.limit:
                difference = self.get_today_stats() - self.limit
                difference = round((difference / self.USD_RATE), 2)
                return f'Денег нет, держись: твой долг - {difference} USD'
            elif self.get_today_stats() == self.limit:
                return 'Денег нет, держись'
            else:
                difference = self.limit - self.get_today_stats()
                difference = round((difference / self.USD_RATE), 2)
                return f'На сегодня осталось {difference} USD'
        if currency == 'eur':
            if self.get_today_stats() > self.limit:
                difference = self.get_today_stats() - self.limit
                difference = round((difference / self.EURO_RATE), 2)
                return f'Денег нет, держись: твой долг - {difference} Euro'
            elif self.get_today_stats() == self.limit:
                return 'Денег нет, держись'
            else:
                difference = self.limit - self.get_today_stats()
                difference = round((difference / self.EURO_RATE), 2)
                return f'На сегодня осталось {difference} Euro'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            difference = self.limit - self.get_today_stats()
            return ('Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {difference} кКал')
        else:
            return 'Хватит есть!'
=======
>>>>>>> 3cb3f1f3fe6a224eb0f064100196a2cc2fed96a6
