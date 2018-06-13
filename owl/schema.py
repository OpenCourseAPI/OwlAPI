
definitions = {
    'status_filter': {
        'type': 'object',
        'properties': {
            'open': {'type': 'number'},
            'waitlist': {'type': 'number'},
            'full': {'type': 'number'},
        }
    },
    'type_filter': {
        'type': 'object',
        'properties': {
            'standard': {'type': 'number'},
            'online': {'type': 'number'},
            'hybrid': {'type': 'number'}
        }
    },
    'day_filter': {
        'type': 'object',
        'properties': {
            'M': {'type': 'number'},
            'T': {'type': 'number'},
            'W': {'type': 'number'},
            'Th': {'type': 'number'},
            'F': {'type': 'number'},
            'S': {'type': 'number'},
            'U': {'type': 'number'},
        }
    },
    'time_filter': {
        'type': 'object',
        'properties': {
            'start': {'type': 'string'},
            'end': {'type': 'string'},
        }
    },
    'filter': {
        'type': 'object',
        'properties': {
            'status': {'$ref': '#/definitions/status_filter'},
            'type': {'$ref': '#/definitions/type_filter'},
            'days': {'$ref': '#/definitions/day_filter'},
            'time': {'$ref': '#/definitions/time_filter'},
        },
    },
    'get_one': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'},
            'department': {'type': 'string'},
            'course': {'type': 'string'},
            'filter': {'$ref': '#/definitions/filter'},
        },
        'required': ['department']
    },
    'get_many': {
        'type': 'object',
        'properties': {
            'courses': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'additionalProperties': {
                        '$ref': '#/definitions/get_one'
                    }
                }
            },
            'filter': {'$ref': '#/definitions/filter'},
        },
        'required': ['courses']
    },
    'get_list': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'},
            'department': {'type': 'string'},
            'course': {'type': 'string'},
        },
        'required': ['department']
    },
    'get_urls': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'}
        },
        'additionalProperties': False
    }
}


def get_definition(definition: str):
    """
    Gets schema definition with the passed name.
    :param definition: str name of definition
    :return: dict representation of json schema.
    """
    d = definitions[definition].copy()
    d['definitions'] = definitions
    return d
