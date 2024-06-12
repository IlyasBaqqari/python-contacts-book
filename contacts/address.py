from dataclasses import dataclass

@dataclass
class Address:
    line1: str = ''
    line2: str = ''
    city: str = ''
    country: str = ''
    postcode: str = ''

    def __str__(self):
        output = ''
        if self.line1:
            output += f'\n{self.line1}'
        if self.line2:
            output += f'\n{self.line2}'

        if self.city and self.country:
            output += f'\n{self.city}, {self.country}'
        elif self.city and (not self.country):
            output += f'\n{self.city}'
        elif (not self.city) and self.country:
            output += f'\n{self.country}'

        if self.postcode:
            output += f'\n{self.postcode}'

        return output