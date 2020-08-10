# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetOne::test_get_one_dept 1'] = {
    '10': [
        {
            'CRN': 20748,
            'course': '10',
            'dept': 'CS',
            'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
            'end': '12/11/2020',
            'raw_course': 'C S F010.01Z',
            'seats': 14,
            'section': '01Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '10',
            'dept': 'CS',
            'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
            'end': '12/11/2020',
            'raw_course': 'C S F010.02W',
            'seats': 0,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'full',
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
            'course': '1A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001A01Z',
            'seats': 19,
            'section': '01Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001A02W',
            'seats': 34,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001A03W',
            'seats': 0,
            'section': '03W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '1A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001A04W',
            'seats': 37,
            'section': '04W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001A05W',
            'seats': 25,
            'section': '05W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1B',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001B01Z',
            'seats': 31,
            'section': '01Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1B',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001B02W',
            'seats': 26,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1B',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001B03W',
            'seats': 4,
            'section': '03W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '1C',
            'dept': 'CS',
            'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
            'end': '12/11/2020',
            'raw_course': 'C S F001C02W',
            'seats': 0,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'full',
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
            'course': '22A',
            'dept': 'CS',
            'desc': 'JAVASCRIPT FOR PROGRAMMERS',
            'end': '12/11/2020',
            'raw_course': 'C S F022A01W',
            'seats': 20,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '2A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002A01Z',
            'seats': 31,
            'section': '01Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '2A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002A02W',
            'seats': 0,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '2A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002A03W',
            'seats': 26,
            'section': '03W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '2A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002A04W',
            'seats': 37,
            'section': '04W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '2A',
            'dept': 'CS',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002A05W',
            'seats': 0,
            'section': '05W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '2B',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002B01W',
            'seats': 27,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '2B',
            'dept': 'CS',
            'desc': 'INTERM SOFTWARE DESIGN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002B02W',
            'seats': 0,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '2C',
            'dept': 'CS',
            'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
            'end': '12/11/2020',
            'raw_course': 'C S F002C01W',
            'seats': 12,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '30A',
            'dept': 'CS',
            'desc': 'INTRODUCTION TO LINUX',
            'end': '12/11/2020',
            'raw_course': 'C S F030A01W',
            'seats': 12,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '30B',
            'dept': 'CS',
            'desc': 'LINUX SHELL PROGRAMMING',
            'end': '12/11/2020',
            'raw_course': 'C S F030B01W',
            'seats': 30,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '31A',
            'dept': 'CS',
            'desc': 'INTRO DATABASE MGMT SYSTEMS',
            'end': '12/11/2020',
            'raw_course': 'C S F031A01W',
            'seats': 4,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A01Z',
            'seats': 28,
            'section': '01Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A02W',
            'seats': 0,
            'section': '02W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A03W',
            'seats': 23,
            'section': '03W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A04W',
            'seats': 0,
            'section': '04W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A05W',
            'seats': 7,
            'section': '05W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3A',
            'dept': 'CS',
            'desc': 'OBJECT ORIEN PRGM METH PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003A06Z',
            'seats': 0,
            'section': '06Z',
            'start': '09/21/2020',
            'status': 'full',
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
            'course': '3B',
            'dept': 'CS',
            'desc': 'INTERMED SOFTWARE DESGN PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003B01W',
            'seats': 15,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3B',
            'dept': 'CS',
            'desc': 'INTERMED SOFTWARE DESGN PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003B02Z',
            'seats': 9,
            'section': '02Z',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '3C',
            'dept': 'CS',
            'desc': 'ADV DATA STRUCT/ALGRTHM PYTHON',
            'end': '12/11/2020',
            'raw_course': 'C S F003C01W',
            'seats': 20,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '48A',
            'dept': 'CS',
            'desc': 'DATA VISUALIZATION',
            'end': '12/11/2020',
            'raw_course': 'C S F048A01W',
            'seats': 0,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'waitlist',
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
            'course': '50A',
            'dept': 'CS',
            'desc': 'NETWORK BASICS (CCNA)',
            'end': '12/11/2020',
            'raw_course': 'C S F050A01W',
            'seats': 6,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '53A',
            'dept': 'CS',
            'desc': 'CYBERSECURITY FUNDAMENTALS',
            'end': '12/11/2020',
            'raw_course': 'C S F053A01W',
            'seats': 17,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '55A',
            'dept': 'CS',
            'desc': 'INTRO CLOUD COMPUTNG AWS',
            'end': '12/11/2020',
            'raw_course': 'C S F055A01W',
            'seats': 11,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
            'course': '55B',
            'dept': 'CS',
            'desc': 'DATABASE ESSENTIALS AWS',
            'end': '12/11/2020',
            'raw_course': 'C S F055B01W',
            'seats': 14,
            'section': '01W',
            'start': '09/21/2020',
            'status': 'open',
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
        'course': '2A',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'raw_course': 'C S F002A01Z',
        'seats': 31,
        'section': '01Z',
        'start': '09/21/2020',
        'status': 'open',
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
        'course': '2A',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'raw_course': 'C S F002A02W',
        'seats': 0,
        'section': '02W',
        'start': '09/21/2020',
        'status': 'waitlist',
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
        'course': '2A',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'raw_course': 'C S F002A03W',
        'seats': 26,
        'section': '03W',
        'start': '09/21/2020',
        'status': 'open',
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
        'course': '2A',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'raw_course': 'C S F002A04W',
        'seats': 37,
        'section': '04W',
        'start': '09/21/2020',
        'status': 'open',
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
        'course': '2A',
        'dept': 'CS',
        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
        'end': '12/11/2020',
        'raw_course': 'C S F002A05W',
        'seats': 0,
        'section': '05W',
        'start': '09/21/2020',
        'status': 'waitlist',
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
                'course': '10',
                'dept': 'CS',
                'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                'end': '12/11/2020',
                'raw_course': 'C S F010.01Z',
                'seats': 14,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'CS',
                'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                'end': '12/11/2020',
                'raw_course': 'C S F010.02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '1A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001A01Z',
                'seats': 19,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001A02W',
                'seats': 34,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001A03W',
                'seats': 0,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001A04W',
                'seats': 37,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001A05W',
                'seats': 25,
                'section': '05W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001B01Z',
                'seats': 31,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001B02W',
                'seats': 26,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001B03W',
                'seats': 4,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1C',
                'dept': 'CS',
                'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                'end': '12/11/2020',
                'raw_course': 'C S F001C02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '22A',
                'dept': 'CS',
                'desc': 'JAVASCRIPT FOR PROGRAMMERS',
                'end': '12/11/2020',
                'raw_course': 'C S F022A01W',
                'seats': 20,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002A01Z',
                'seats': 31,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002A02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '2A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002A03W',
                'seats': 26,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002A04W',
                'seats': 37,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2A',
                'dept': 'CS',
                'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002A05W',
                'seats': 0,
                'section': '05W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '2B',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002B01W',
                'seats': 27,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2B',
                'dept': 'CS',
                'desc': 'INTERM SOFTWARE DESIGN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002B02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '2C',
                'dept': 'CS',
                'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                'end': '12/11/2020',
                'raw_course': 'C S F002C01W',
                'seats': 12,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '30A',
                'dept': 'CS',
                'desc': 'INTRODUCTION TO LINUX',
                'end': '12/11/2020',
                'raw_course': 'C S F030A01W',
                'seats': 12,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '30B',
                'dept': 'CS',
                'desc': 'LINUX SHELL PROGRAMMING',
                'end': '12/11/2020',
                'raw_course': 'C S F030B01W',
                'seats': 30,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '31A',
                'dept': 'CS',
                'desc': 'INTRO DATABASE MGMT SYSTEMS',
                'end': '12/11/2020',
                'raw_course': 'C S F031A01W',
                'seats': 4,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A01Z',
                'seats': 28,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A03W',
                'seats': 23,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A04W',
                'seats': 0,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A05W',
                'seats': 7,
                'section': '05W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3A',
                'dept': 'CS',
                'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003A06Z',
                'seats': 0,
                'section': '06Z',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '3B',
                'dept': 'CS',
                'desc': 'INTERMED SOFTWARE DESGN PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003B01W',
                'seats': 15,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3B',
                'dept': 'CS',
                'desc': 'INTERMED SOFTWARE DESGN PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003B02Z',
                'seats': 9,
                'section': '02Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '3C',
                'dept': 'CS',
                'desc': 'ADV DATA STRUCT/ALGRTHM PYTHON',
                'end': '12/11/2020',
                'raw_course': 'C S F003C01W',
                'seats': 20,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'CS',
                'desc': 'DATA VISUALIZATION',
                'end': '12/11/2020',
                'raw_course': 'C S F048A01W',
                'seats': 0,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '50A',
                'dept': 'CS',
                'desc': 'NETWORK BASICS (CCNA)',
                'end': '12/11/2020',
                'raw_course': 'C S F050A01W',
                'seats': 6,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '53A',
                'dept': 'CS',
                'desc': 'CYBERSECURITY FUNDAMENTALS',
                'end': '12/11/2020',
                'raw_course': 'C S F053A01W',
                'seats': 17,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '55A',
                'dept': 'CS',
                'desc': 'INTRO CLOUD COMPUTNG AWS',
                'end': '12/11/2020',
                'raw_course': 'C S F055A01W',
                'seats': 11,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '55B',
                'dept': 'CS',
                'desc': 'DATABASE ESSENTIALS AWS',
                'end': '12/11/2020',
                'raw_course': 'C S F055B01W',
                'seats': 14,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.01V',
                'seats': 10,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.03W',
                'seats': 0,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.04W',
                'seats': 9,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.05W',
                'seats': 33,
                'section': '05W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.06W',
                'seats': 0,
                'section': '06W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.07Z',
                'seats': 0,
                'section': '07Z',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.08W',
                'seats': 15,
                'section': '08W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.09W',
                'seats': 35,
                'section': '09W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.10W',
                'seats': 1,
                'section': '10W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.11V',
                'seats': 0,
                'section': '11V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.12W',
                'seats': 34,
                'section': '12W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.13V',
                'seats': 21,
                'section': '13V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.14W',
                'seats': 37,
                'section': '14W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.16V',
                'seats': 14,
                'section': '16V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.17W',
                'seats': 33,
                'section': '17W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.18W',
                'seats': 39,
                'section': '18W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.19W',
                'seats': 31,
                'section': '19W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.20W',
                'seats': 36,
                'section': '20W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.21W',
                'seats': 36,
                'section': '21W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.22W',
                'seats': 38,
                'section': '22W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '10',
                'dept': 'MATH',
                'desc': 'ELEMENTARY STATISTICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F010.23W',
                'seats': 37,
                'section': '23W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '105',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F105.01W',
                'seats': 0,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '105',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F105.02W',
                'seats': 0,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '105',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F105.03W',
                'seats': 0,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '105',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F105.04V',
                'seats': 0,
                'section': '04V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '105',
                'dept': 'MATH',
                'desc': 'INTERMEDIATE ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F105.05W',
                'seats': 6,
                'section': '05W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '12',
                'dept': 'MATH',
                'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                'end': '12/11/2020',
                'raw_course': 'MATH F012.01Z',
                'seats': 30,
                'section': '01Z',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '12',
                'dept': 'MATH',
                'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                'end': '12/11/2020',
                'raw_course': 'MATH F012.02W',
                'seats': 25,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '180',
                'dept': 'MATH',
                'desc': 'QUANTITATIVE REASONING',
                'end': '12/11/2020',
                'raw_course': 'MATH F180.01W',
                'seats': 13,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A01V',
                'seats': 28,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A03V',
                'seats': 0,
                'section': '03V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A04V',
                'seats': 0,
                'section': '04V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A05V',
                'seats': 32,
                'section': '05V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A06V',
                'seats': 23,
                'section': '06V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A07W',
                'seats': 0,
                'section': '07W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1A',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001A08W',
                'seats': 28,
                'section': '08W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001B01W',
                'seats': 14,
                'section': '01W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001B02W',
                'seats': 26,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1B',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001B03V',
                'seats': 0,
                'section': '03V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1B',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001B04W',
                'seats': 0,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1C',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001C01V',
                'seats': 0,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '1C',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001C03W',
                'seats': 1,
                'section': '03W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '1C',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001C04W',
                'seats': 0,
                'section': '04W',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '1C',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001C9DV',
                'seats': 0,
                'section': '9DV',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '1D',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001D01V',
                'seats': 0,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '1D',
                'dept': 'MATH',
                'desc': 'CALCULUS',
                'end': '12/11/2020',
                'raw_course': 'MATH F001D02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '22',
                'dept': 'MATH',
                'desc': 'DISCRETE MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F022.01V',
                'seats': 0,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '22',
                'dept': 'MATH',
                'desc': 'DISCRETE MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F022.02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '248A',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'raw_course': 'MATH F248A3CV',
                'seats': 14,
                'section': '3CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '248A',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'raw_course': 'MATH F248A4CV',
                'seats': 26,
                'section': '4CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '248A',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'raw_course': 'MATH F248A5CV',
                'seats': 24,
                'section': '5CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '248A',
                'dept': 'MATH',
                'desc': 'SUPPORT FOR MATH 48A',
                'end': '12/11/2020',
                'raw_course': 'MATH F248A6CV',
                'seats': 1,
                'section': '6CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2A',
                'dept': 'MATH',
                'desc': 'DIFFERENTIAL EQUATIONS',
                'end': '12/11/2020',
                'raw_course': 'MATH F002A01V',
                'seats': 0,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '2A',
                'dept': 'MATH',
                'desc': 'DIFFERENTIAL EQUATIONS',
                'end': '12/11/2020',
                'raw_course': 'MATH F002A02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '2B',
                'dept': 'MATH',
                'desc': 'LINEAR ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F002B01V',
                'seats': 11,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '2B',
                'dept': 'MATH',
                'desc': 'LINEAR ALGEBRA',
                'end': '12/11/2020',
                'raw_course': 'MATH F002B02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048A02W',
                'seats': 9,
                'section': '02W',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048A3CV',
                'seats': 14,
                'section': '3CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048A4CV',
                'seats': 26,
                'section': '4CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048A5CV',
                'seats': 24,
                'section': '5CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048A6CV',
                'seats': 1,
                'section': '6CV',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048AMVP',
                'seats': 0,
                'section': 'MVP',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '48A',
                'dept': 'MATH',
                'desc': 'PRECALCULUS I',
                'end': '12/11/2020',
                'raw_course': 'MATH F048AVMP',
                'seats': 0,
                'section': 'VMP',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '48B',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'raw_course': 'MATH F048B02V',
                'seats': 31,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48B',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'raw_course': 'MATH F048B03V',
                'seats': 14,
                'section': '03V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48B',
                'dept': 'MATH',
                'desc': 'PRECALCULUS II',
                'end': '12/11/2020',
                'raw_course': 'MATH F048B04V',
                'seats': 29,
                'section': '04V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48C',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'raw_course': 'MATH F048C01V',
                'seats': 35,
                'section': '01V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48C',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'raw_course': 'MATH F048C02V',
                'seats': 0,
                'section': '02V',
                'start': '09/21/2020',
                'status': 'waitlist',
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
                'course': '48C',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'raw_course': 'MATH F048C03V',
                'seats': 16,
                'section': '03V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '48C',
                'dept': 'MATH',
                'desc': 'PRECALCULUS III',
                'end': '12/11/2020',
                'raw_course': 'MATH F048C04V',
                'seats': 19,
                'section': '04V',
                'start': '09/21/2020',
                'status': 'open',
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
                'course': '70R',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F070R01',
                'seats': 0,
                'section': '01',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '71R',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F071R01',
                'seats': 0,
                'section': '01',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '72R',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F072R01',
                'seats': 0,
                'section': '01',
                'start': '09/21/2020',
                'status': 'full',
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
                'course': '73R',
                'dept': 'MATH',
                'desc': 'INDEPENDENT STUDY MATHEMATICS',
                'end': '12/11/2020',
                'raw_course': 'MATH F073R01',
                'seats': 0,
                'section': '01',
                'start': '09/21/2020',
                'status': 'full',
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

snapshots['TestGetOne::test_get_one_dept_and_honors_course 1'] = [
    {
        'CRN': 21030,
        'course': '2AH',
        'dept': 'MUS',
        'desc': 'HONORS GREAT COMPOSR WSTRN CIV',
        'end': '12/11/2020',
        'raw_course': 'MUS F02AH01Z',
        'seats': 0,
        'section': '01Z',
        'start': '09/21/2020',
        'status': 'waitlist',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Barkley',
                'room': 'ONLINE',
                'time': 'TBA'
            },
            {
                'campus': 'FH',
                'days': 'MW',
                'instructor': 'Hartwell',
                'room': 'ONLINE',
                'time': '12:00 PM-01:50 PM'
            },
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Carey',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 5.0,
        'wait_cap': 5,
        'wait_seats': 2
    }
]

snapshots['TestGetOne::test_get_one_dept_and_complex_course 1'] = [
    {
        'CRN': 21149,
        'course': '12AL',
        'dept': 'CHEM',
        'desc': 'ORGANIC CHEMISTRY LABORATORY',
        'end': '12/11/2020',
        'raw_course': 'CHEM F12AL01Z',
        'seats': 0,
        'section': '01Z',
        'start': '09/21/2020',
        'status': 'waitlist',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Painter',
                'room': 'ONLINE',
                'time': 'TBA'
            },
            {
                'campus': 'FH',
                'days': 'MW',
                'instructor': 'Painter',
                'room': 'ONLINE',
                'time': '05:30 PM-07:20 PM'
            }
        ],
        'units': 2.0,
        'wait_cap': 8,
        'wait_seats': 8
    },
    {
        'CRN': 20661,
        'course': '12AL',
        'dept': 'CHEM',
        'desc': 'ORGANIC CHEMISTRY LABORATORY',
        'end': '12/11/2020',
        'raw_course': 'CHEM F12AL02Z',
        'seats': 12,
        'section': '02Z',
        'start': '09/21/2020',
        'status': 'open',
        'time': [
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Painter',
                'room': 'ONLINE',
                'time': 'TBA'
            },
            {
                'campus': 'FH',
                'days': 'MW',
                'instructor': 'Painter',
                'room': 'ONLINE',
                'time': '05:30 PM-07:20 PM'
            }
        ],
        'units': 2.0,
        'wait_cap': 8,
        'wait_seats': 8
    },
    {
        'CRN': 20662,
        'course': '12AL',
        'dept': 'CHEM',
        'desc': 'ORGANIC CHEMISTRY LABORATORY',
        'end': '12/11/2020',
        'raw_course': 'CHEM F12AL03Z',
        'seats': 9,
        'section': '03Z',
        'start': '09/21/2020',
        'status': 'open',
        'time': [
            {
                'campus': 'FH',
                'days': 'TTh',
                'instructor': 'Armstrong',
                'room': 'ONLINE',
                'time': '12:00 PM-01:50 PM'
            },
            {
                'campus': '',
                'days': 'TBA',
                'instructor': 'Armstrong',
                'room': '',
                'time': 'TBA'
            }
        ],
        'units': 2.0,
        'wait_cap': 8,
        'wait_seats': 8
    },
    {
        'CRN': 20740,
        'course': '12AL',
        'dept': 'CHEM',
        'desc': 'ORGANIC CHEMISTRY LABORATORY',
        'end': '12/11/2020',
        'raw_course': 'CHEM F12AL04Z',
        'seats': 0,
        'section': '04Z',
        'start': '09/21/2020',
        'status': 'waitlist',
        'time': [
            {
                'campus': 'FH',
                'days': 'TTh',
                'instructor': 'Armstrong',
                'room': 'ONLINE',
                'time': '12:00 PM-01:50 PM'
            },
            {
                'campus': 'FH',
                'days': 'TBA',
                'instructor': 'Armstrong',
                'room': 'ONLINE',
                'time': 'TBA'
            }
        ],
        'units': 2.0,
        'wait_cap': 8,
        'wait_seats': 7
    }
]
