import datetime


class NumberRange(object):
    data = {}

    def __init__(self, fields):
        self.fields = fields

        self.use_value('prefix', self.prefix)
        self.use_field('status', 'Status')
        self.use_field('date', 'Date', self.format_date)
        self.use_field('provider', 'Communications Provider')
        self.use_field('format', 'Number Length')
        self.use_field('change', 'Change', self.format_date)
        self.use_field('use', 'Use', self.none_if_empty)
        self.use_field('notes', 'Notes', self.none_if_empty)
        self.use_field('tariff_notes', 'Tariff Notes', self.none_if_empty)

    @property
    def prefix(self):
        return self.fields.get('SABC', '') + \
                 self.fields.get('DE', self.fields.get('D', '')) + \
                 self.fields.get('FG', '')

    def use_field(self, key, field, converter=None):
        value = self.fields.get(field)
        if converter:
            value = converter(value)

        self.data[key] = value

    def use_value(self, key, value, converter=None):
        if converter:
            value = converter(value)

        self.data[key] = value

    def format_date(self, value):
        if value is None or value == '':
            return

        slashes = value.count('/')
        fmt = '%d/%m/%Y' if slashes == 2 else '%m/%Y'

        return datetime.datetime.strptime(value, fmt).date().isoformat()

    def none_if_empty(self, value):
        return None if value == '' else value

    def __iter__(self):
        for key, value in self.data.items():
            yield (key, value)
