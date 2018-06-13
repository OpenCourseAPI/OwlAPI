
definitions = {
    'status_filter': {
        'type': 'object',
        'properties': {
            'open': {'type': 'number'},
            'waitlist': {'type': 'number'},
            'full': {'type': 'number'},
        },
        "additionalProperties": False
    },
    'type_filter': {
        'type': 'object',
        'properties': {
            'standard': {'type': 'number'},
            'online': {'type': 'number'},
            'hybrid': {'type': 'number'}
        },
        "additionalProperties": False
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
        },
        "additionalProperties": False
    },
    'time_filter': {
        'type': 'object',
        'properties': {
            'start': {'type': 'string'},
            'end': {'type': 'string'},
        },
        "additionalProperties": False
    },
    'instructor_filter': {
        'type': 'object',
        'properties': {},
        "additionalProperties": {
            "type": 'number'
        }
    },
    'conflict_filter': {
        'type': 'array',
        'items': {
            '$ref': '#/definitions/get_section'
        }
    },
    'filter': {
        'type': 'object',
        'properties': {
            'status': {'$ref': '#/definitions/status_filter'},
            'type': {'$ref': '#/definitions/type_filter'},
            'days': {'$ref': '#/definitions/day_filter'},
            'time': {'$ref': '#/definitions/time_filter'},
            'instructor': {'$ref': '#/definitions/instructor_filter'},
            'conflict_sections': {'$ref': '#/definitions/conflict_filter'}
        },
        "additionalProperties": False
    },
    'get_section': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'},
            'department': {'type': 'string'},
            'course': {'type': 'string'},
            'section': {'type': 'string'},
        },
        'required': ['department', 'course', 'section']
    },
    'get_one': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'},
            'department': {'type': 'string'},
            'course': {'type': 'string'},
            'filter': {'$ref': '#/definitions/filter'},
        },
        'required': ['department'],
        "additionalProperties": False
    },
    'get_many': {
        'type': 'object',
        'properties': {
            'courses': {
                'type': 'array',
                'items': {
                    '$ref': '#/definitions/get_one'
                }
            },
            'filter': {'$ref': '#/definitions/filter'},
        },
        'required': ['courses'],
        "additionalProperties": False
    },
    'get_list': {
        'type': 'object',
        'properties': {
            'quarter': {'type': 'string'},
            'department': {'type': 'string'},
            'course': {'type': 'string'},
        },
        'required': ['department'],
        "additionalProperties": False
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
