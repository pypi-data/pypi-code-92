from .column import Column
from ..autodoc.schema import Integer as AutoDocInteger


class Integer(Column):
    _auto_doc_class = AutoDocInteger

    def from_backend(self, value):
        return int(value)

    def input_error_for_value(self, value):
        return f'{self.name} must be an integer' if type(value) != int else ''

    def build_condition(self, value, operator=None):
        if not operator:
            operator = '='
        return f"{self.name}{operator}{value}"

    def is_allowed_operator(self, operator):
        return operator in ['=', '<', '>', '<=', '>=']
