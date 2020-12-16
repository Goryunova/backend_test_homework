import datetime as dt


class Record:

    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = str(comment)
        if not isinstance(date, dt.date):
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT).date()
        else:
            self.date = date


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_stats(self, days_amount):
        result = 0
        past_date = dt.date.today() - dt.timedelta(days = days_amount)
        today = dt.date.today()
        for record in self.records:
            if past_date < record.date <= today:
                result += record.amount
        return result
    def get_taday_stats(self):
        return self.get_stats(1)
    def get_week_stats(self):
        return self.get_stats(7)


class CashCalcilator(Calculator):

    RUB_RATE = 1.0
    USD_RATE = 73.28
    EURO_RATE = 88.90
    def get_taday_cash_remained(self, currency):
        spent = self.get_taday_stats()
        remained = self.limit - spent
        if remained == 0:
            return print('Денег нет, держись')
        currency_switch = {
            'rub': (self.RUB_RATE, "руб"),
            'usd': (self.USD_RATE, "USD"),
            'eur': (self.EURO_RATE, "Euro")
        }
        str1 = round(abs(remained) / currency_switch[currency][0],2)
        currency_str = f"{str1}{currency_switch[currency][1]}"
        if remained < 0:
            return f"Денег нет, держись: твой долг - {currency_str}"
        return f"На сегодня осталось {currency_str}"


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        spent = self.get_taday_stats()
        remained = self.limit - spent
        if remained > 0:
            return f"Сегодня можно съесть что-нибудь еще, но с общей "\
            f"калорийностью не более {remained} кКал"
        return print('Хватит есть!')


if __name__ =="__main__":
    cash_calculator = CashCalcilator(1000.567)
    cash_calculator.add_record(Record(amount=145,
        comment="Безудержный шопинг", date="11.12.2020"))
    cash_calculator.add_record(Record(amount=1568,
        comment="Наполнение потребительской корзины", date="15.12.2020"))
    cash_calculator.add_record(Record(amount=691, 
        comment="Катание на такси", date="08.12.2020"))
    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=1186, 
        comment="Кусочек тортика. И еще одиню", date="12.12.2020"))
    calories_calculator.add_record(Record(amount=84,
        comment="Йогурт", date="15.12.2020"))
    calories_calculator.add_record(Record(amount=1140,
        comment="Баночка чипсов",date="24.11.2020"))
    print(cash_calculator.get_taday_cash_remained('rub'))
    print(calories_calculator.get_calories_remained())
