import csv
from itertools import chain
from collections import defaultdict
import phonenumbers
from .number_range import NumberRange


class Datastore(object):
    ranges = defaultdict(lambda: defaultdict(list))

    def __init__(self, *files):
        for filename in files:
            self.parse_file(filename)

    def parse_file(self, filename):
        with open(filename) as file:
            for row in csv.DictReader(file, skipinitialspace=True):
                self.parse_row(row)

    def parse_row(self, row):
        outer = row.get('SABC')
        inner = row.get('DE', row.get('D/DE'))

        self.ranges[outer][inner].append(row)

    def find(self, number):
        try:
            number = str(phonenumbers.parse(number, 'GB').national_number)
        except phonenumbers.NumberParseException:
            return

        candidates = list(self.candidates(number))

        if len(candidates) == 1:
            return NumberRange(candidates[0])
        elif len(candidates) > 1:
            raise RuntimeError('Ambiguous result: %i number ranges found' %
                               len(candidates))

    def candidates(self, number):
        sabc = number[0:4]
        d, de = number[4], number[4:6]
        f, fg = number[6], number[6:8]
        fg_options = [f, fg, '']

        for nrange in chain(self.ranges[sabc][d], self.ranges[sabc][de]):
            if nrange['FG'] in fg_options:
                yield nrange
