# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetOne::test_get_one_dept 1'] = {
    '10': [
        {
            'CRN': 20748,
            'course': 'C S F010.01Z',
            'dept': 'CS',
            'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
            'end': '12/11/2020',
            'seats': 14,
            'section': '10',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TTh',
                    'instructor': 'Riordan',
                    'room': 'ONLINE',
                    'time': '06:00 PM-07:50 PM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Riordan',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20749,
            'course': 'C S F010.02W',
            'dept': 'CS',
            'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
            'end': '12/11/2020',
            'seats': 0,
            'section': '10',
            'start': '09/21/2020',
            'status': 'Full',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Lamble',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 0
        }
    ],
    '1A': [
        {
            'CRN': 20743,
            'course': 'C S F001A01Z',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'seats': 19,
            'section': '1A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TTh',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'time': '10:00 AM-11:50 AM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21639,
            'course': 'C S F001A02W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'seats': 34,
            'section': '1A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Weusijana',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20267,
            'course': 'C S F001A03W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'seats': 0,
            'section': '1A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Cecil',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 4
        },
        {
            'CRN': 20268,
            'course': 'C S F001A04W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'seats': 37,
            'section': '1A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Ibrahim',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20371,
            'course': 'C S F001A05W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'seats': 25,
            'section': '1A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Krishnamurthy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '1B': [
        {
            'CRN': 20339,
            'course': 'C S F001B01Z',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'seats': 31,
            'section': '1B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TTh',
                    'instructor': 'Mansouri Samani',
                    'room': 'ONLINE',
                    'time': '06:00 PM-07:50 PM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Mansouri Samani',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20744,
            'course': 'C S F001B02W',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'seats': 26,
            'section': '1B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Weusijana',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20463,
            'course': 'C S F001B03W',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'seats': 4,
            'section': '1B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Pham',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '1C': [
        {
            'CRN': 20270,
            'course': 'C S F001C02W',
            'dept': 'CS',
            'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
            'end': '12/11/2020',
            'seats': 0,
            'section': '1C',
            'start': '09/21/2020',
            'status': 'Full',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 0
        }
    ],
    '22A': [
        {
            'CRN': 20751,
            'course': 'C S F022A01W',
            'dept': 'CS',
            'desc': 'JAVASCRIPT FOR PROGRAMMERS',
            'end': '12/11/2020',
            'seats': 20,
            'section': '22A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Weusijana',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '2A': [
        {
            'CRN': 20269,
            'course': 'C S F002A01Z',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'seats': 31,
            'section': '2A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TTh',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'time': '08:00 AM-09:50 AM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20372,
            'course': 'C S F002A02W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'seats': 0,
            'section': '2A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Harden',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 1
        },
        {
            'CRN': 20745,
            'course': 'C S F002A03W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'seats': 26,
            'section': '2A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Cecil',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20325,
            'course': 'C S F002A04W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'seats': 37,
            'section': '2A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Pham',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21642,
            'course': 'C S F002A05W',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'seats': 0,
            'section': '2A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Dhagat',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 8
        }
    ],
    '2B': [
        {
            'CRN': 20417,
            'course': 'C S F002B01W',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN C++',
            'end': '12/11/2020',
            'seats': 27,
            'section': '2B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21644,
            'course': 'C S F002B02W',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN C++',
            'end': '12/11/2020',
            'seats': 0,
            'section': '2B',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Harden',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 4
        }
    ],
    '2C': [
        {
            'CRN': 20326,
            'course': 'C S F002C01W',
            'dept': 'CS',
            'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
            'end': '12/11/2020',
            'seats': 12,
            'section': '2C',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '30A': [
        {
            'CRN': 20327,
            'course': 'C S F030A01W',
            'dept': 'CS',
            'desc': 'INTRODUCTION TO LINUX',
            'end': '12/11/2020',
            'seats': 12,
            'section': '30A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '30B': [
        {
            'CRN': 20600,
            'course': 'C S F030B01W',
            'dept': 'CS',
            'desc': 'LINUX SHELL PROGRAMMING',
            'end': '12/11/2020',
            'seats': 30,
            'section': '30B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '31A': [
        {
            'CRN': 20338,
            'course': 'C S F031A01W',
            'dept': 'CS',
            'desc': 'INTRO DATABASE MGMT SYSTEMS',
            'end': '12/11/2020',
            'seats': 4,
            'section': '31A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Meade',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '3A': [
        {
            'CRN': 20674,
            'course': 'C S F003A01Z',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 28,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'MW',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': '06:00 PM-07:50 PM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21646,
            'course': 'C S F003A02W',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 0,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'time': 'TBA'
                },
                {
                    'campus': '',
                    'days': 'TBA',
                    'instructor': 'Mazloom',
                    'room': '',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 20747,
            'course': 'C S F003A03W',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 23,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 25,
            'wait_seats': 25
        },
        {
            'CRN': 20889,
            'course': 'C S F003A04W',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 0,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Meade',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 9
        },
        {
            'CRN': 21650,
            'course': 'C S F003A05W',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 7,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Lai',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21825,
            'course': 'C S F003A06Z',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'seats': 0,
            'section': '3A',
            'start': '09/21/2020',
            'status': 'Full',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'MW',
                    'instructor': 'Yang',
                    'room': 'ONLINE',
                    'time': '01:30 PM-03:20 PM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Yang',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 0,
            'wait_seats': 0
        }
    ],
    '3B': [
        {
            'CRN': 20845,
            'course': 'C S F003B01W',
            'dept': 'CS',
            'desc': 'INTERMED SOFTWARE DESGN PYTHON',
            'end': '12/11/2020',
            'seats': 15,
            'section': '3B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Trinh',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        },
        {
            'CRN': 21145,
            'course': 'C S F003B02Z',
            'dept': 'CS',
            'desc': 'INTERMED SOFTWARE DESGN PYTHON',
            'end': '12/11/2020',
            'seats': 9,
            'section': '3B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'MW',
                    'instructor': 'Yang',
                    'room': 'ONLINE',
                    'time': '10:00 AM-11:50 AM'
                },
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Yang',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '3C': [
        {
            'CRN': 21164,
            'course': 'C S F003C01W',
            'dept': 'CS',
            'desc': 'ADV DATA STRUCT/ALGRTHM PYTHON',
            'end': '12/11/2020',
            'seats': 20,
            'section': '3C',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Lamble',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '48A': [
        {
            'CRN': 21818,
            'course': 'C S F048A01W',
            'dept': 'CS',
            'desc': 'DATA VISUALIZATION',
            'end': '12/11/2020',
            'seats': 0,
            'section': '48A',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Lankester',
                    'room': 'ONLINE',
                    'time': 'TBA'
                },
                {
                    'campus': '',
                    'days': 'TBA',
                    'instructor': 'Lankester',
                    'room': '',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 5
        }
    ],
    '50A': [
        {
            'CRN': 21652,
            'course': 'C S F050A01W',
            'dept': 'CS',
            'desc': 'NETWORK BASICS (CCNA)',
            'end': '12/11/2020',
            'seats': 6,
            'section': '50A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '53A': [
        {
            'CRN': 21653,
            'course': 'C S F053A01W',
            'dept': 'CS',
            'desc': 'CYBERSECURITY FUNDAMENTALS',
            'end': '12/11/2020',
            'seats': 17,
            'section': '53A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Ryan',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '55A': [
        {
            'CRN': 21162,
            'course': 'C S F055A01W',
            'dept': 'CS',
            'desc': 'INTRO CLOUD COMPUTNG AWS',
            'end': '12/11/2020',
            'seats': 11,
            'section': '55A',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Sandor',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ],
    '55B': [
        {
            'CRN': 21654,
            'course': 'C S F055B01W',
            'dept': 'CS',
            'desc': 'DATABASE ESSENTIALS AWS',
            'end': '12/11/2020',
            'seats': 14,
            'section': '55B',
            'start': '09/21/2020',
            'status': 'Open',
            'time': [
                {
                    'campus': 'FH',
                    'days': 'TBA',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'time': 'TBA'
                }
            ],
            'units': 4.5,
            'wait_cap': 10,
            'wait_seats': 10
        }
    ]
}

snapshots['TestGetOne::test_get_one_dept_and_course 1'] = [
    {
        'CRN': 20269,
        'course': 'C S F002A01Z',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'seats': 31,
        'section': '2A',
        'start': '09/21/2020',
        'status': 'Open',
        'time': [
            {
                'campus': 'FH',
                'days': 'TTh',
                'instructor': 'Venkataraman',
                'room': 'ONLINE',
                'time': '08:00 AM-09:50 AM'
            },
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Venkataraman',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 4.5,
        'wait_cap': 10,
        'wait_seats': 10
    },
    {
        'CRN': 20372,
        'course': 'C S F002A02W',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'seats': 0,
        'section': '2A',
        'start': '09/21/2020',
        'status': 'Waitlist',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Harden',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 4.5,
        'wait_cap': 10,
        'wait_seats': 1
    },
    {
        'CRN': 20745,
        'course': 'C S F002A03W',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'seats': 26,
        'section': '2A',
        'start': '09/21/2020',
        'status': 'Open',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Cecil',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 4.5,
        'wait_cap': 10,
        'wait_seats': 10
    },
    {
        'CRN': 20325,
        'course': 'C S F002A04W',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'seats': 37,
        'section': '2A',
        'start': '09/21/2020',
        'status': 'Open',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Pham',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 4.5,
        'wait_cap': 10,
        'wait_seats': 10
    },
    {
        'CRN': 21642,
        'course': 'C S F002A05W',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'seats': 0,
        'section': '2A',
        'start': '09/21/2020',
        'status': 'Waitlist',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Dhagat',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 4.5,
        'wait_cap': 10,
        'wait_seats': 8
    }
]

snapshots['TestGetMany::test_get_many_dept 1'] = [
    {
        '10': [
            {
                'CRN': 20748,
                'course': 'C S F010.01Z',
                'dept': 'CS',
                'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                'end': '12/11/2020',
                'seats': 14,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Riordan',
                        'room': 'ONLINE',
                        'time': '06:00 PM-07:50 PM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Riordan',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20749,
                'course': 'C S F010.02W',
                'dept': 'CS',
                'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Lamble',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 0
            }
        ],
        '1A': [
            {
                'CRN': 20743,
                'course': 'C S F001A01Z',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'seats': 19,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'time': '10:00 AM-11:50 AM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21639,
                'course': 'C S F001A02W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'seats': 34,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Weusijana',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20267,
                'course': 'C S F001A03W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Cecil',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 4
            },
            {
                'CRN': 20268,
                'course': 'C S F001A04W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'seats': 37,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Ibrahim',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20371,
                'course': 'C S F001A05W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'seats': 25,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Krishnamurthy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '1B': [
            {
                'CRN': 20339,
                'course': 'C S F001B01Z',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'seats': 31,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Mansouri Samani',
                        'room': 'ONLINE',
                        'time': '06:00 PM-07:50 PM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mansouri Samani',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20744,
                'course': 'C S F001B02W',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'seats': 26,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Weusijana',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20463,
                'course': 'C S F001B03W',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'seats': 4,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Pham',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '1C': [
            {
                'CRN': 20270,
                'course': 'C S F001C02W',
                'dept': 'CS',
                'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1C',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 0
            }
        ],
        '22A': [
            {
                'CRN': 20751,
                'course': 'C S F022A01W',
                'dept': 'CS',
                'desc': 'JAVASCRIPT FOR PROGRAMMERS',
                'end': '12/11/2020',
                'seats': 20,
                'section': '22A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Weusijana',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '2A': [
            {
                'CRN': 20269,
                'course': 'C S F002A01Z',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'seats': 31,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'time': '08:00 AM-09:50 AM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20372,
                'course': 'C S F002A02W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Harden',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 1
            },
            {
                'CRN': 20745,
                'course': 'C S F002A03W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'seats': 26,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Cecil',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20325,
                'course': 'C S F002A04W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'seats': 37,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Pham',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21642,
                'course': 'C S F002A05W',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Dhagat',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 8
            }
        ],
        '2B': [
            {
                'CRN': 20417,
                'course': 'C S F002B01W',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN C++',
                'end': '12/11/2020',
                'seats': 27,
                'section': '2B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21644,
                'course': 'C S F002B02W',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN C++',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2B',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Harden',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 4
            }
        ],
        '2C': [
            {
                'CRN': 20326,
                'course': 'C S F002C01W',
                'dept': 'CS',
                'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                'end': '12/11/2020',
                'seats': 12,
                'section': '2C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '30A': [
            {
                'CRN': 20327,
                'course': 'C S F030A01W',
                'dept': 'CS',
                'desc': 'INTRODUCTION TO LINUX',
                'end': '12/11/2020',
                'seats': 12,
                'section': '30A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '30B': [
            {
                'CRN': 20600,
                'course': 'C S F030B01W',
                'dept': 'CS',
                'desc': 'LINUX SHELL PROGRAMMING',
                'end': '12/11/2020',
                'seats': 30,
                'section': '30B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '31A': [
            {
                'CRN': 20338,
                'course': 'C S F031A01W',
                'dept': 'CS',
                'desc': 'INTRO DATABASE MGMT SYSTEMS',
                'end': '12/11/2020',
                'seats': 4,
                'section': '31A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Meade',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '3A': [
            {
                'CRN': 20674,
                'course': 'C S F003A01Z',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 28,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': '06:00 PM-07:50 PM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21646,
                'course': 'C S F003A02W',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 0,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    },
                    {
                        'campus': '',
                        'days': 'TBA',
                        'instructor': 'Mazloom',
                        'room': '',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20747,
                'course': 'C S F003A03W',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 23,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 25,
                'wait_seats': 25
            },
            {
                'CRN': 20889,
                'course': 'C S F003A04W',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 0,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Meade',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 9
            },
            {
                'CRN': 21650,
                'course': 'C S F003A05W',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 7,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Lai',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21825,
                'course': 'C S F003A06Z',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'seats': 0,
                'section': '3A',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Yang',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:20 PM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Yang',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '3B': [
            {
                'CRN': 20845,
                'course': 'C S F003B01W',
                'dept': 'CS',
                'desc': 'INTERMED SOFTWARE DESGN PYTHON',
                'end': '12/11/2020',
                'seats': 15,
                'section': '3B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Trinh',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21145,
                'course': 'C S F003B02Z',
                'dept': 'CS',
                'desc': 'INTERMED SOFTWARE DESGN PYTHON',
                'end': '12/11/2020',
                'seats': 9,
                'section': '3B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Yang',
                        'room': 'ONLINE',
                        'time': '10:00 AM-11:50 AM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Yang',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '3C': [
            {
                'CRN': 21164,
                'course': 'C S F003C01W',
                'dept': 'CS',
                'desc': 'ADV DATA STRUCT/ALGRTHM PYTHON',
                'end': '12/11/2020',
                'seats': 20,
                'section': '3C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Lamble',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '48A': [
            {
                'CRN': 21818,
                'course': 'C S F048A01W',
                'dept': 'CS',
                'desc': 'DATA VISUALIZATION',
                'end': '12/11/2020',
                'seats': 0,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Lankester',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    },
                    {
                        'campus': '',
                        'days': 'TBA',
                        'instructor': 'Lankester',
                        'room': '',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 5
            }
        ],
        '50A': [
            {
                'CRN': 21652,
                'course': 'C S F050A01W',
                'dept': 'CS',
                'desc': 'NETWORK BASICS (CCNA)',
                'end': '12/11/2020',
                'seats': 6,
                'section': '50A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '53A': [
            {
                'CRN': 21653,
                'course': 'C S F053A01W',
                'dept': 'CS',
                'desc': 'CYBERSECURITY FUNDAMENTALS',
                'end': '12/11/2020',
                'seats': 17,
                'section': '53A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Ryan',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '55A': [
            {
                'CRN': 21162,
                'course': 'C S F055A01W',
                'dept': 'CS',
                'desc': 'INTRO CLOUD COMPUTNG AWS',
                'end': '12/11/2020',
                'seats': 11,
                'section': '55A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Sandor',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '55B': [
            {
                'CRN': 21654,
                'course': 'C S F055B01W',
                'dept': 'CS',
                'desc': 'DATABASE ESSENTIALS AWS',
                'end': '12/11/2020',
                'seats': 14,
                'section': '55B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 4.5,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ]
    },
    {
        '10': [
            {
                'CRN': 20673,
                'course': 'MATH F010.01V',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 10,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Francisco',
                        'room': 'ONLINE',
                        'time': '07:30 AM-09:45 AM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20964,
                'course': 'MATH F010.02V',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Morriss',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 2
            },
            {
                'CRN': 20976,
                'course': 'MATH F010.03W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 7
            },
            {
                'CRN': 20776,
                'course': 'MATH F010.04W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 9,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20977,
                'course': 'MATH F010.05W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 33,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20778,
                'course': 'MATH F010.06W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Sinclair',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 9
            },
            {
                'CRN': 20779,
                'course': 'MATH F010.07Z',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'T',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': '10:00 AM-11:15 AM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20780,
                'course': 'MATH F010.08W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 15,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Sinclair',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20781,
                'course': 'MATH F010.09W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 35,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Sinclair',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20786,
                'course': 'MATH F010.10W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 1,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20787,
                'course': 'MATH F010.11V',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Morriss',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20788,
                'course': 'MATH F010.12W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 34,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20789,
                'course': 'MATH F010.13V',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 21,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Munoz',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20790,
                'course': 'MATH F010.14W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 37,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21000,
                'course': 'MATH F010.16V',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 14,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Witschorik',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20792,
                'course': 'MATH F010.17W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 33,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20793,
                'course': 'MATH F010.18W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 39,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20794,
                'course': 'MATH F010.19W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 31,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Mudge',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20812,
                'course': 'MATH F010.20W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 36,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Tomutiu',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21001,
                'course': 'MATH F010.21W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 36,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Papay',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21002,
                'course': 'MATH F010.22W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 38,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Papay',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21312,
                'course': 'MATH F010.23W',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'seats': 37,
                'section': '10',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Florero Salinas',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 5,
                'wait_seats': 5
            }
        ],
        '105': [
            {
                'CRN': 20811,
                'course': 'MATH F105.01W',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '105',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Tomutiu',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 9
            },
            {
                'CRN': 20091,
                'course': 'MATH F105.02W',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '105',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Robledo',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 8
            },
            {
                'CRN': 20813,
                'course': 'MATH F105.03W',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '105',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Oruganti',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21018,
                'course': 'MATH F105.04V',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '105',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Low',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 7
            },
            {
                'CRN': 20814,
                'course': 'MATH F105.05W',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'seats': 6,
                'section': '105',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Sukumar',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '12': [
            {
                'CRN': 20277,
                'course': 'MATH F012.01Z',
                'dept': 'MATH',
                'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                'end': '12/11/2020',
                'seats': 30,
                'section': '12',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Knobel',
                        'room': 'ONLINE',
                        'time': '10:00 AM-11:50 AM'
                    },
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Knobel',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20843,
                'course': 'MATH F012.02W',
                'dept': 'MATH',
                'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                'end': '12/11/2020',
                'seats': 25,
                'section': '12',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Knobel',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '180': [
            {
                'CRN': 21380,
                'course': 'MATH F180.01W',
                'dept': 'MATH',
                'desc': 'QUANTITATIVE REASONING',
                'end': '12/11/2020',
                'seats': 13,
                'section': '180',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Gray',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 5,
                'wait_seats': 5
            }
        ],
        '1A': [
            {
                'CRN': 20086,
                'course': 'MATH F001A01V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 28,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Uilecan',
                        'room': 'ONLINE',
                        'time': '07:30 AM-09:45 AM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20087,
                'course': 'MATH F001A02V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Cembellin',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20088,
                'course': 'MATH F001A03V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Nghiem',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 2
            },
            {
                'CRN': 20257,
                'course': 'MATH F001A04V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Nghiem',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 3
            },
            {
                'CRN': 20761,
                'course': 'MATH F001A05V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 32,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Lam',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20762,
                'course': 'MATH F001A06V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 23,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Ni',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20305,
                'course': 'MATH F001A07W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 8
            },
            {
                'CRN': 21310,
                'course': 'MATH F001A08W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 28,
                'section': '1A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Lam',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '1B': [
            {
                'CRN': 20672,
                'course': 'MATH F001B01W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 14,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Litrus',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20089,
                'course': 'MATH F001B02W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 26,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Litrus',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20769,
                'course': 'MATH F001B03V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Nghiem',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 7
            },
            {
                'CRN': 20773,
                'course': 'MATH F001B04W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1B',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 5
            }
        ],
        '1C': [
            {
                'CRN': 20774,
                'course': 'MATH F001C01V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1C',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Knobel',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 7
            },
            {
                'CRN': 20177,
                'course': 'MATH F001C03W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 1,
                'section': '1C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Litrus',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 0
            },
            {
                'CRN': 20959,
                'course': 'MATH F001C04W',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1C',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Oruganti',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 0
            },
            {
                'CRN': 21675,
                'course': 'MATH F001C9DV',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1C',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Park Lee',
                        'room': 'ONLINE',
                        'time': '03:45 PM-06:00 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '1D': [
            {
                'CRN': 20194,
                'course': 'MATH F001D01V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1D',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Park Lee',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 0
            },
            {
                'CRN': 20178,
                'course': 'MATH F001D02V',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '1D',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Park Lee',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 0
            }
        ],
        '22': [
            {
                'CRN': 20798,
                'course': 'MATH F022.01V',
                'dept': 'MATH',
                'desc': 'DISCRETE MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '22',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Morriss',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 9
            },
            {
                'CRN': 20799,
                'course': 'MATH F022.02V',
                'dept': 'MATH',
                'desc': 'DISCRETE MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '22',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Witschorik',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '248A': [
            {
                'CRN': 20848,
                'course': 'MATH F248A3CV',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'seats': 14,
                'section': '248A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'W',
                        'instructor': 'Uilecan',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 2.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20849,
                'course': 'MATH F248A4CV',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'seats': 26,
                'section': '248A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'Th',
                        'instructor': 'Sukumar',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 2.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20850,
                'course': 'MATH F248A5CV',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'seats': 24,
                'section': '248A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'Th',
                        'instructor': 'Papay',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 2.5,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20851,
                'course': 'MATH F248A6CV',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'seats': 1,
                'section': '248A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'W',
                        'instructor': 'Robledo',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 2.5,
                'wait_cap': 10,
                'wait_seats': 3
            }
        ],
        '2A': [
            {
                'CRN': 20258,
                'course': 'MATH F002A01V',
                'dept': 'MATH',
                'desc': 'DIFFERENTIAL EQUATIONS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Park Lee',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20472,
                'course': 'MATH F002A02V',
                'dept': 'MATH',
                'desc': 'DIFFERENTIAL EQUATIONS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2A',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Park Lee',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '2B': [
            {
                'CRN': 20353,
                'course': 'MATH F002B01V',
                'dept': 'MATH',
                'desc': 'LINEAR ALGEBRA',
                'end': '12/11/2020',
                'seats': 11,
                'section': '2B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Ryker',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21135,
                'course': 'MATH F002B02V',
                'dept': 'MATH',
                'desc': 'LINEAR ALGEBRA',
                'end': '12/11/2020',
                'seats': 0,
                'section': '2B',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Nosratieh',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 0
            }
        ],
        '48A': [
            {
                'CRN': 20198,
                'course': 'MATH F048A02W',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 9,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Ryker',
                        'room': 'ONLINE',
                        'time': 'TBA'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20807,
                'course': 'MATH F048A3CV',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 14,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MT',
                        'instructor': 'Uilecan',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20808,
                'course': 'MATH F048A4CV',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 26,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TW',
                        'instructor': 'Sukumar',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20809,
                'course': 'MATH F048A5CV',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 24,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TW',
                        'instructor': 'Papay',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20810,
                'course': 'MATH F048A6CV',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 1,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MT',
                        'instructor': 'Robledo',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 3
            },
            {
                'CRN': 20199,
                'course': 'MATH F048AMVP',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 0,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Francisco',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 0,
                'wait_seats': 0
            },
            {
                'CRN': 21676,
                'course': 'MATH F048AVMP',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'seats': 0,
                'section': '48A',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Cembellin',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '48B': [
            {
                'CRN': 20260,
                'course': 'MATH F048B02V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'seats': 31,
                'section': '48B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Lam',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20261,
                'course': 'MATH F048B03V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'seats': 14,
                'section': '48B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Zwack',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20334,
                'course': 'MATH F048B04V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'seats': 29,
                'section': '48B',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Pham',
                        'room': 'ONLINE',
                        'time': '06:00 PM-08:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '48C': [
            {
                'CRN': 20606,
                'course': 'MATH F048C01V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'seats': 35,
                'section': '48C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Ni',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 21016,
                'course': 'MATH F048C02V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'seats': 0,
                'section': '48C',
                'start': '09/21/2020',
                'status': 'Waitlist',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Zwack',
                        'room': 'ONLINE',
                        'time': '10:00 AM-12:15 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 8
            },
            {
                'CRN': 20314,
                'course': 'MATH F048C03V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'seats': 16,
                'section': '48C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'MW',
                        'instructor': 'Low',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            },
            {
                'CRN': 20429,
                'course': 'MATH F048C04V',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'seats': 19,
                'section': '48C',
                'start': '09/21/2020',
                'status': 'Open',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TTh',
                        'instructor': 'Zwack',
                        'room': 'ONLINE',
                        'time': '01:30 PM-03:45 PM'
                    }
                ],
                'units': 5.0,
                'wait_cap': 10,
                'wait_seats': 10
            }
        ],
        '70R': [
            {
                'CRN': 20488,
                'course': 'MATH F070R01',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '70R',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'time': 'TBA'
                    }
                ],
                'units': 1.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '71R': [
            {
                'CRN': 20489,
                'course': 'MATH F071R01',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '71R',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'time': 'TBA'
                    }
                ],
                'units': 2.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '72R': [
            {
                'CRN': 20490,
                'course': 'MATH F072R01',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '72R',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'time': 'TBA'
                    }
                ],
                'units': 3.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ],
        '73R': [
            {
                'CRN': 20491,
                'course': 'MATH F073R01',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'seats': 0,
                'section': '73R',
                'start': '09/21/2020',
                'status': 'Full',
                'time': [
                    {
                        'campus': 'FH',
                        'days': 'TBA',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'time': 'TBA'
                    }
                ],
                'units': 4.0,
                'wait_cap': 0,
                'wait_seats': 0
            }
        ]
    }
]

snapshots['TestGetOne::test_get_one_dept_and_honors_course 1'] = {
    '21030': [
        {
            'CRN': '21030',
            'campus': 'FH',
            'course': 'MUS F02AH01Z',
            'days': 'TBA',
            'desc': 'HONORS GREAT COMPOSR WSTRN CIV',
            'end': '12/11/2020',
            'instructor': 'Barkley',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': 'TBA',
            'units': '5.00',
            'wait_cap': '5',
            'wait_seats': '2'
        },
        {
            'CRN': '21030',
            'campus': 'FH',
            'course': 'MUS F02AH01Z',
            'days': 'MW',
            'desc': 'HONORS GREAT COMPOSR WSTRN CIV',
            'end': '12/11/2020',
            'instructor': 'Hartwell',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': '12:00 PM-01:50 PM',
            'units': '5.00',
            'wait_cap': '5',
            'wait_seats': '2'
        },
        {
            'CRN': '21030',
            'campus': 'FH',
            'course': 'MUS F02AH01Z',
            'days': 'TBA',
            'desc': 'HONORS GREAT COMPOSR WSTRN CIV',
            'end': '12/11/2020',
            'instructor': 'Carey',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': 'TBA',
            'units': '5.00',
            'wait_cap': '5',
            'wait_seats': '2'
        }
    ]
}

snapshots['TestGetOne::test_get_one_dept_and_complex_course 1'] = {
    '20661': [
        {
            'CRN': '20661',
            'campus': 'FH',
            'course': 'CHEM F12AL02Z',
            'days': 'TBA',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Painter',
            'room': 'ONLINE',
            'seats': '12',
            'start': '09/21/2020',
            'status': 'Open',
            'time': 'TBA',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        },
        {
            'CRN': '20661',
            'campus': 'FH',
            'course': 'CHEM F12AL02Z',
            'days': 'MW',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Painter',
            'room': 'ONLINE',
            'seats': '12',
            'start': '09/21/2020',
            'status': 'Open',
            'time': '05:30 PM-07:20 PM',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        }
    ],
    '20662': [
        {
            'CRN': '20662',
            'campus': 'FH',
            'course': 'CHEM F12AL03Z',
            'days': 'TTh',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Armstrong',
            'room': 'ONLINE',
            'seats': '9',
            'start': '09/21/2020',
            'status': 'Open',
            'time': '12:00 PM-01:50 PM',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        },
        {
            'CRN': '20662',
            'campus': '',
            'course': 'CHEM F12AL03Z',
            'days': 'TBA',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Armstrong',
            'room': '',
            'seats': '9',
            'start': '09/21/2020',
            'status': 'Open',
            'time': 'TBA',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        }
    ],
    '20740': [
        {
            'CRN': '20740',
            'campus': 'FH',
            'course': 'CHEM F12AL04Z',
            'days': 'TTh',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Armstrong',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': '12:00 PM-01:50 PM',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '7'
        },
        {
            'CRN': '20740',
            'campus': 'FH',
            'course': 'CHEM F12AL04Z',
            'days': 'TBA',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Armstrong',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': 'TBA',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '7'
        }
    ],
    '21149': [
        {
            'CRN': '21149',
            'campus': 'FH',
            'course': 'CHEM F12AL01Z',
            'days': 'TBA',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Painter',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': 'TBA',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        },
        {
            'CRN': '21149',
            'campus': 'FH',
            'course': 'CHEM F12AL01Z',
            'days': 'MW',
            'desc': 'ORGANIC CHEMISTRY LABORATORY',
            'end': '12/11/2020',
            'instructor': 'Painter',
            'room': 'ONLINE',
            'seats': '0',
            'start': '09/21/2020',
            'status': 'Waitlist',
            'time': '05:30 PM-07:20 PM',
            'units': '2.00',
            'wait_cap': '8',
            'wait_seats': '8'
        }
    ]
}
