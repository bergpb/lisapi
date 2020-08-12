from wtforms.validators import ValidationError
from flask import request


class UniqueCheckerCreate(object):
    def __init__(self, model, field, message="* Data exists!"):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class UniqueCheckerUpdate(object):
    def __init__(self, id, model, field, message="* Data exists!"):
        self.id = id
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        '''Get id from item argument in url, if id from object is different
        from id item in database validate, else pass'''
        item_id = request.view_args[self.id]
        check = self.model.query.filter(self.field == field.data).first()
        if check and item_id != check.id:
            raise ValidationError(self.message)
