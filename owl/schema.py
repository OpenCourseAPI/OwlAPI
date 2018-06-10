
definitions = {
    'status_filter': {
        'type': 'object',
        'properties': {
            'open': {'type': 'int'},
            'waitlist': {'type': 'int'},
            'full': {'type': 'int'},
        }
    },
    'type_filter': {
        'type': 'object',
        'properties': {
            'standard': {'type': 'int'},
            'online': {'type': 'int'},
            'hybrid': {'type': 'int'}
        }
    },
    'day_filter': {
        'type': 'object',
        'properties': {
            'M': {'type': 'int'},
            'T': {'type': 'int'},
            'W': {'type': 'int'},
            'Th': {'type': 'int'},
            'F': {'type': 'int'},
            'S': {'type': 'int'},
            'U': {'type': 'int'},
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
    }
}


def get_definition(definition: str):
    d = definitions[definition]
    d['definitions'] = definitions
    return d
