"""
This module contains input classes, which validate data passed by api
users in requests.

This module also allows more readable results to api users, that list
any potential issues with their requests, before they are acted on,
and without requiring error code lookups.
"""
from itertools import chain

from flask_inputs.validators import JsonSchema
import flask_inputs

from owl.schema import get_definition


class Inputs(flask_inputs.Inputs):
    """
    Extends flask_inputs.Input in order to fix issues with validate method.
    """

    def validate(self):
        """
        Validate incoming request data. Returns True if all data
        is valid.
        Adds each of the validator's error messages to Inputs.errors if
        not valid.

        :returns: Boolean
        """
        success = True

        for attribute, form in self._forms.items():  # Fixed iterator here.
            if '_input' in form._fields:
                form.process(self._get_values(attribute, coerse=False))
            else:
                form.process(self._get_values(attribute))

            if not form.validate():
                success = False
                self.errors += chain(*form.errors.values())

        return success


class GetOneInput(Inputs):
    json = [JsonSchema(schema=get_definition('get_one'))]


class GetManyInput(Inputs):
    json = [JsonSchema(schema=get_definition('get_many'))]


class GetListInput(Inputs):
    json = [JsonSchema(schema=get_definition('get_list'))]
