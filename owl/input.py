"""
This module contains request classes, which validate and facilitate
access to data passed by api users in get requests.

This module also allows more readable results to api users, that list
any potential issues with their requests, before they are acted on,
and without requiring error code lookups.
"""
import flask_inputs
from flask_inputs.validators import JsonSchema

from owl.schema import get_definition


class GetOneInput(flask_inputs.Inputs):
    json = [JsonSchema(schema=get_definition('get_one'))]


class GetManyInput(flask_inputs.Inputs):
    json = [JsonSchema(schema=get_definition('get_many'))]


class GetListInput(flask_inputs.Inputs):
    json = [JsonSchema(schema=get_definition('get_list'))]
