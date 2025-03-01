from dataclasses import dataclass

@dataclass
class Money:
    integer: int
    fraction: int = 0
    currency: str = 'hryvnia'

    def __str__(self):
        return f'{self.integer},{self.fraction} {self.currency}\'s'

    def __sub_errors(self, other):
        if other.get_value() < 0:
            raise Exception('Amount cannot be negative')
        elif other.get_value() > self.get_value():
            raise Exception('Amount cannot be greater than price')
        elif other.currency != self.currency:
            raise Exception('Currency does not match')

    def __sub_result(self, other):
        result = str(self.get_value() - other.get_value())
        return result.split('.')

    def __sub__(self, other):
        self.__sub_errors(other)
        result = self.__sub_result(other)
        return Money(int(result[0]), int(result[1]), self.currency)


    def get_value(self):
        return self.integer + (self.fraction / 100)
