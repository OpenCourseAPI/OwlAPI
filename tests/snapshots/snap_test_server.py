# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetOne::test_get_one_dept 1'] = [
    {
        '10': {
            '40408': [
                {
                    'CRN': '40408',
                    'campus': 'FH',
                    'course': 'C S F010.01Y',
                    'days': 'TTh',
                    'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                    'end': '06/29/2018',
                    'instructor': 'Riordan',
                    'room': '5610',
                    'seats': '15',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:30 PM-08:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40408',
                    'campus': 'FH',
                    'course': 'C S F010.01Y',
                    'days': 'TBA',
                    'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                    'end': '06/29/2018',
                    'instructor': 'Riordan',
                    'room': 'ONLINE',
                    'seats': '15',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40890': [
                {
                    'CRN': '40890',
                    'campus': 'FH',
                    'course': 'C S F010.02W',
                    'days': 'TBA',
                    'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                    'end': '06/29/2018',
                    'instructor': 'Lamble',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Full',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '0'
                }
            ]
        },
        '18': {
            '41406': [
                {
                    'CRN': '41406',
                    'campus': 'FH',
                    'course': 'C S F018.01',
                    'days': 'MW',
                    'desc': 'DISCRETE MATHEMATICS',
                    'end': '06/29/2018',
                    'instructor': 'Morriss',
                    'room': '4502',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Full',
                    'time': '01:30 PM-03:45 PM',
                    'units': '  5.00',
                    'wait_cap': '0',
                    'wait_seats': '0'
                }
            ],
            '41407': [
                {
                    'CRN': '41407',
                    'campus': 'FH',
                    'course': 'C S F018.02',
                    'days': 'MW',
                    'desc': 'DISCRETE MATHEMATICS',
                    'end': '06/29/2018',
                    'instructor': 'Witschorik',
                    'room': '5601',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Full',
                    'time': '06:00 PM-08:15 PM',
                    'units': '  5.00',
                    'wait_cap': '0',
                    'wait_seats': '0'
                }
            ]
        },
        '1A': {
            '40397': [
                {
                    'CRN': '40397',
                    'campus': 'FH',
                    'course': 'C S F001A01Y',
                    'days': 'TTh',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Haight',
                    'room': '4308',
                    'seats': '26',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '10:00 AM-11:50 AM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40397',
                    'campus': 'FH',
                    'course': 'C S F001A01Y',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Haight',
                    'room': 'ONLINE',
                    'seats': '26',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40568': [
                {
                    'CRN': '40568',
                    'campus': 'FH',
                    'course': 'C S F001A04W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Cecil',
                    'room': 'ONLINE',
                    'seats': '4',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42061': [
                {
                    'CRN': '42061',
                    'campus': 'FH',
                    'course': 'C S F001A02Y',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'seats': '31',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42061',
                    'campus': 'FH',
                    'course': 'C S F001A02Y',
                    'days': 'TTh',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Mazloom',
                    'room': '4308',
                    'seats': '31',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '01:30 PM-03:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42062': [
                {
                    'CRN': '42062',
                    'campus': 'FH',
                    'course': 'C S F001A03Y',
                    'days': 'MW',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': '5614',
                    'seats': '30',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-07:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42062',
                    'campus': 'FH',
                    'course': 'C S F001A03Y',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '30',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42063': [
                {
                    'CRN': '42063',
                    'campus': 'FH',
                    'course': 'C S F001A05W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Krishnan',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Waitlist',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '7'
                }
            ],
            '42064': [
                {
                    'CRN': '42064',
                    'campus': 'FH',
                    'course': 'C S F001A06W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Ibrahim',
                    'room': 'ONLINE',
                    'seats': '39',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42065': [
                {
                    'CRN': '42065',
                    'campus': 'FH',
                    'course': 'C S F001A07W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '05/21/2018',
                    'status': 'Full',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '0',
                    'wait_seats': '0'
                }
            ]
        },
        '1B': {
            '40400': [
                {
                    'CRN': '40400',
                    'campus': 'FH',
                    'course': 'C S F001B02Y',
                    'days': 'TTh',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': '5602',
                    'seats': '36',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:30 PM-08:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40400',
                    'campus': 'FH',
                    'course': 'C S F001B02Y',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '36',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40856': [
                {
                    'CRN': '40856',
                    'campus': 'FH',
                    'course': 'C S F001B03W',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Pham',
                    'room': 'ONLINE',
                    'seats': '13',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42067': [
                {
                    'CRN': '42067',
                    'campus': 'FH',
                    'course': 'C S F001B01Y',
                    'days': 'MW',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Mazloom',
                    'room': '4308',
                    'seats': '12',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '10:00 AM-11:50 AM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42067',
                    'campus': 'FH',
                    'course': 'C S F001B01Y',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'seats': '12',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42068': [
                {
                    'CRN': '42068',
                    'campus': 'FH',
                    'course': 'C S F001B04W',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Harden',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Full',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '0'
                }
            ],
            '42069': [
                {
                    'CRN': '42069',
                    'campus': 'FH',
                    'course': 'C S F001B05W',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '12',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '1C': {
            '40402': [
                {
                    'CRN': '40402',
                    'campus': 'FH',
                    'course': 'C S F001C01Y',
                    'days': 'MW',
                    'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Weusijana',
                    'room': '5602',
                    'seats': '22',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '01:30 PM-03:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40402',
                    'campus': 'FH',
                    'course': 'C S F001C01Y',
                    'days': 'TBA',
                    'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Weusijana',
                    'room': 'ONLINE',
                    'seats': '22',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40746': [
                {
                    'CRN': '40746',
                    'campus': 'FH',
                    'course': 'C S F001C02W',
                    'days': 'TBA',
                    'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                    'end': '06/29/2018',
                    'instructor': 'Mazloom',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Full',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '0'
                }
            ]
        },
        '20A': {
            '42127': [
                {
                    'CRN': '42127',
                    'campus': 'FH',
                    'course': 'C S F020A01W',
                    'days': 'TBA',
                    'desc': 'PROGRAMMING IN C#',
                    'end': '06/29/2018',
                    'instructor': 'Meade',
                    'room': 'ONLINE',
                    'seats': '23',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '21A': {
            '40597': [
                {
                    'CRN': '40597',
                    'campus': 'FH',
                    'course': 'C S F021A02W',
                    'days': 'TBA',
                    'desc': 'PYTHON FOR PROGRAMMERS',
                    'end': '06/29/2018',
                    'instructor': 'Khayrallah',
                    'room': 'ONLINE',
                    'seats': '2',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '41543': [
                {
                    'CRN': '41543',
                    'campus': 'FH',
                    'course': 'C S F021A03W',
                    'days': 'TBA',
                    'desc': 'PYTHON FOR PROGRAMMERS',
                    'end': '06/29/2018',
                    'instructor': 'Xiong',
                    'room': 'ONLINE',
                    'seats': '38',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42090': [
                {
                    'CRN': '42090',
                    'campus': 'FH',
                    'course': 'C S F021A01Y',
                    'days': 'TTh',
                    'desc': 'PYTHON FOR PROGRAMMERS',
                    'end': '06/29/2018',
                    'instructor': 'Van Der Linden',
                    'room': '5609',
                    'seats': '32',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:30 PM-08:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42090',
                    'campus': 'FH',
                    'course': 'C S F021A01Y',
                    'days': 'TBA',
                    'desc': 'PYTHON FOR PROGRAMMERS',
                    'end': '06/29/2018',
                    'instructor': 'Van Der Linden',
                    'room': 'ONLINE',
                    'seats': '32',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42091': [
                {
                    'CRN': '42091',
                    'campus': 'FH',
                    'course': 'C S F021A04W',
                    'days': 'TBA',
                    'desc': 'PYTHON FOR PROGRAMMERS',
                    'end': '06/29/2018',
                    'instructor': 'Cecil',
                    'room': 'ONLINE',
                    'seats': '34',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '21B': {
            '42093': [
                {
                    'CRN': '42093',
                    'campus': 'FH',
                    'course': 'C S F021B02W',
                    'days': 'TBA',
                    'desc': 'INTRM PYTHON PROGRAMMING',
                    'end': '06/29/2018',
                    'instructor': 'Lamble',
                    'room': 'ONLINE',
                    'seats': '4',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '22A': {
            '40571': [
                {
                    'CRN': '40571',
                    'campus': 'FH',
                    'course': 'C S F022A01W',
                    'days': 'TBA',
                    'desc': 'JAVASCRIPT FOR PROGRAMERS',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '39',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42128': [
                {
                    'CRN': '42128',
                    'campus': 'FH',
                    'course': 'C S F022A02W',
                    'days': 'TBA',
                    'desc': 'JAVASCRIPT FOR PROGRAMERS',
                    'end': '06/29/2018',
                    'instructor': 'Meade',
                    'room': 'ONLINE',
                    'seats': '11',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42133': [
                {
                    'CRN': '42133',
                    'campus': 'FH',
                    'course': 'C S F022A03W',
                    'days': 'TBA',
                    'desc': 'JAVASCRIPT FOR PROGRAMERS',
                    'end': '06/29/2018',
                    'instructor': 'Weusijana',
                    'room': 'ONLINE',
                    'seats': '37',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '2A': {
            '40403': [
                {
                    'CRN': '40403',
                    'campus': 'FH',
                    'course': 'C S F002A01Y',
                    'days': 'TTh',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Venkataraman',
                    'room': '5609',
                    'seats': '23',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '08:00 AM-09:50 AM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40403',
                    'campus': 'FH',
                    'course': 'C S F002A01Y',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'seats': '23',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40405': [
                {
                    'CRN': '40405',
                    'campus': 'FH',
                    'course': 'C S F002A03W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'seats': '7',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40589': [
                {
                    'CRN': '40589',
                    'campus': 'FH',
                    'course': 'C S F002A04W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Harden',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Waitlist',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '9'
                }
            ],
            '42071': [
                {
                    'CRN': '42071',
                    'campus': 'FH',
                    'course': 'C S F002A02Y',
                    'days': 'TTh',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Oluwasanmi',
                    'room': '5607',
                    'seats': '37',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:30 PM-08:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42071',
                    'campus': 'FH',
                    'course': 'C S F002A02Y',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Oluwasanmi',
                    'room': 'ONLINE',
                    'seats': '37',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42072': [
                {
                    'CRN': '42072',
                    'campus': 'FH',
                    'course': 'C S F002A05W',
                    'days': 'TBA',
                    'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Gentry-Kolen',
                    'room': 'ONLINE',
                    'seats': '30',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '2B': {
            '40406': [
                {
                    'CRN': '40406',
                    'campus': 'FH',
                    'course': 'C S F002B02W',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Harden',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '04/09/2018',
                    'status': 'Waitlist',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '4'
                }
            ],
            '40651': [
                {
                    'CRN': '40651',
                    'campus': 'FH',
                    'course': 'C S F002B01Y',
                    'days': 'MW',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Dhagat',
                    'room': '5602',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:30 PM-08:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40651',
                    'campus': 'FH',
                    'course': 'C S F002B01Y',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Dhagat',
                    'room': 'ONLINE',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '41360': [
                {
                    'CRN': '41360',
                    'campus': 'FH',
                    'course': 'C S F002B03W',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Pham',
                    'room': 'ONLINE',
                    'seats': '34',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42112': [
                {
                    'CRN': '42112',
                    'campus': 'FH',
                    'course': 'C S F002B04Y',
                    'days': 'MW',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Lankester',
                    'room': '5610',
                    'seats': '32',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '01:30 PM-03:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42112',
                    'campus': 'FH',
                    'course': 'C S F002B04Y',
                    'days': 'TBA',
                    'desc': 'INTERM SOFTWARE DESIGN C++',
                    'end': '06/29/2018',
                    'instructor': 'Lankester',
                    'room': 'ONLINE',
                    'seats': '32',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '2C': {
            '40407': [
                {
                    'CRN': '40407',
                    'campus': 'FH',
                    'course': 'C S F002C01Y',
                    'days': 'TTh',
                    'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Lankester',
                    'room': '5607',
                    'seats': '17',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '01:30 PM-03:20 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40407',
                    'campus': 'FH',
                    'course': 'C S F002C01Y',
                    'days': 'TBA',
                    'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Lankester',
                    'room': 'ONLINE',
                    'seats': '17',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '40754': [
                {
                    'CRN': '40754',
                    'campus': 'FH',
                    'course': 'C S F002C02W',
                    'days': 'TBA',
                    'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                    'end': '06/29/2018',
                    'instructor': 'Venkataraman',
                    'room': 'ONLINE',
                    'seats': '3',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '30A': {
            '40572': [
                {
                    'CRN': '40572',
                    'campus': 'FH',
                    'course': 'C S F030A01W',
                    'days': 'TBA',
                    'desc': 'INTRODUCTION TO LINUX',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'seats': '13',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '30B': {
            '41311': [
                {
                    'CRN': '41311',
                    'campus': 'FH',
                    'course': 'C S F030B01W',
                    'days': 'TBA',
                    'desc': 'LINUX SHELL PROGRAMMING',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'seats': '30',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '31A': {
            '40654': [
                {
                    'CRN': '40654',
                    'campus': 'FH',
                    'course': 'C S F031A01W',
                    'days': 'TBA',
                    'desc': 'INTRO DATABASE MGMT SYSTEMS',
                    'end': '06/29/2018',
                    'instructor': 'Ibrahim',
                    'room': 'ONLINE',
                    'seats': '17',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '3A': {
            '42073': [
                {
                    'CRN': '42073',
                    'campus': 'FH',
                    'course': 'C S F003A01Y',
                    'days': 'MW',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Haight',
                    'room': '4306',
                    'seats': '28',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '10:00 AM-11:50 AM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42073',
                    'campus': 'FH',
                    'course': 'C S F003A01Y',
                    'days': 'TBA',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Haight',
                    'room': 'ONLINE',
                    'seats': '28',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42074': [
                {
                    'CRN': '42074',
                    'campus': 'FH',
                    'course': 'C S F003A02W',
                    'days': 'TBA',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Lai',
                    'room': 'ONLINE',
                    'seats': '2',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42075': [
                {
                    'CRN': '42075',
                    'campus': 'FH',
                    'course': 'C S F003A03W',
                    'days': 'TBA',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Xiong',
                    'room': 'ONLINE',
                    'seats': '29',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42076': [
                {
                    'CRN': '42076',
                    'campus': 'FH',
                    'course': 'C S F003A04W',
                    'days': 'TBA',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Lai',
                    'room': 'ONLINE',
                    'seats': '32',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42077': [
                {
                    'CRN': '42077',
                    'campus': 'FH',
                    'course': 'C S F003A05W',
                    'days': 'TBA',
                    'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '0',
                    'start': '05/21/2018',
                    'status': 'Full',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '0',
                    'wait_seats': '0'
                }
            ]
        },
        '49': {
            '40891': [
                {
                    'CRN': '40891',
                    'campus': 'FH',
                    'course': 'C S F049.02W',
                    'days': 'TBA',
                    'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                    'end': '06/29/2018',
                    'instructor': 'Agarwal',
                    'room': 'ONLINE',
                    'seats': '16',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  2.00',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42094': [
                {
                    'CRN': '42094',
                    'campus': 'FH',
                    'course': 'C S F049.01Y',
                    'days': 'TBA',
                    'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                    'end': '06/29/2018',
                    'instructor': 'Barnard',
                    'room': 'ONLINE',
                    'seats': '31',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  2.00',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42094',
                    'campus': 'FH',
                    'course': 'C S F049.01Y',
                    'days': 'W',
                    'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                    'end': '06/29/2018',
                    'instructor': 'Barnard',
                    'room': '4302',
                    'seats': '31',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '01:30 PM-03:20 PM',
                    'units': '  2.00',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '50A': {
            '40410': [
                {
                    'CRN': '40410',
                    'campus': 'FH',
                    'course': 'C S F050A01Y',
                    'days': 'T',
                    'desc': 'NETWORK BASICS (CCNA)',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': '4308',
                    'seats': '34',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40410',
                    'campus': 'FH',
                    'course': 'C S F050A01Y',
                    'days': 'TBA',
                    'desc': 'NETWORK BASICS (CCNA)',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'seats': '34',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '50C': {
            '42095': [
                {
                    'CRN': '42095',
                    'campus': 'FH',
                    'course': 'C S F050C01Y',
                    'days': 'M',
                    'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': '4308',
                    'seats': '36',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42095',
                    'campus': 'FH',
                    'course': 'C S F050C01Y',
                    'days': 'TBA',
                    'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'seats': '36',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42115': [
                {
                    'CRN': '42115',
                    'campus': 'FH',
                    'course': 'C S F050C02W',
                    'days': 'TBA',
                    'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                    'end': '06/29/2018',
                    'instructor': 'Murphy',
                    'room': 'ONLINE',
                    'seats': '36',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '50E': {
            '41312': [
                {
                    'CRN': '41312',
                    'campus': 'FH',
                    'course': 'C S F050E01Y',
                    'days': 'W',
                    'desc': 'INTRO TO IP NETWORK SECURITY',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': '4308',
                    'seats': '38',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '41312',
                    'campus': 'FH',
                    'course': 'C S F050E01Y',
                    'days': 'TBA',
                    'desc': 'INTRO TO IP NETWORK SECURITY',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '38',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '53A': {
            '42116': [
                {
                    'CRN': '42116',
                    'campus': 'FH',
                    'course': 'C S F053A01Y',
                    'days': 'M',
                    'desc': 'CYBERSECURITY FUNDAMENTALS',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': '4306',
                    'seats': '39',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42116',
                    'campus': 'FH',
                    'course': 'C S F053A01Y',
                    'days': 'TBA',
                    'desc': 'CYBERSECURITY FUNDAMENTALS',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': 'ONLINE',
                    'seats': '39',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42117': [
                {
                    'CRN': '42117',
                    'campus': 'FH',
                    'course': 'C S F053A02W',
                    'days': 'TBA',
                    'desc': 'CYBERSECURITY FUNDAMENTALS',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': 'ONLINE',
                    'seats': '22',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '53B': {
            '42118': [
                {
                    'CRN': '42118',
                    'campus': 'FH',
                    'course': 'C S F053B01Y',
                    'days': 'W',
                    'desc': 'FIREWALLS & THREAT MANAGEMENT',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': '5609',
                    'seats': '37',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42118',
                    'campus': 'FH',
                    'course': 'C S F053B01Y',
                    'days': 'TBA',
                    'desc': 'FIREWALLS & THREAT MANAGEMENT',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': 'ONLINE',
                    'seats': '37',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ],
            '42119': [
                {
                    'CRN': '42119',
                    'campus': 'FH',
                    'course': 'C S F053B02W',
                    'days': 'TBA',
                    'desc': 'FIREWALLS & THREAT MANAGEMENT',
                    'end': '06/29/2018',
                    'instructor': 'Ryan',
                    'room': 'ONLINE',
                    'seats': '33',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '60A': {
            '42120': [
                {
                    'CRN': '42120',
                    'campus': 'FH',
                    'course': 'C S F060A01Y',
                    'days': 'W',
                    'desc': 'INSTALL/CONFIRG WINDOW SERVR 1',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': '4306',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '06:00 PM-09:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '42120',
                    'campus': 'FH',
                    'course': 'C S F060A01Y',
                    'days': 'TBA',
                    'desc': 'INSTALL/CONFIRG WINDOW SERVR 1',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '63A': {
            '42121': [
                {
                    'CRN': '42121',
                    'campus': 'FH',
                    'course': 'C S F063A01W',
                    'days': 'TBA',
                    'desc': 'DEVELOPING APPLICATION FOR IOS',
                    'end': '06/29/2018',
                    'instructor': 'Gentry-Kolen',
                    'room': 'ONLINE',
                    'seats': '27',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '80A': {
            '42122': [
                {
                    'CRN': '42122',
                    'campus': 'FH',
                    'course': 'C S F080A01W',
                    'days': 'TBA',
                    'desc': 'OPEN SOURCE CONTRIBUTION',
                    'end': '06/29/2018',
                    'instructor': 'Kosar',
                    'room': 'ONLINE',
                    'seats': '29',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '81A': {
            '42123': [
                {
                    'CRN': '42123',
                    'campus': 'FH',
                    'course': 'C S F081A01W',
                    'days': 'TBA',
                    'desc': '3-D GRAPHICS PROGRAMMING',
                    'end': '06/29/2018',
                    'instructor': 'Trinh',
                    'room': 'ONLINE',
                    'seats': '28',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        },
        '82A': {
            '40662': [
                {
                    'CRN': '40662',
                    'campus': 'FC',
                    'course': 'C S F082A50Y',
                    'days': 'S',
                    'desc': 'INTRO SOFTWARE QUALITY ASSURAN',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'SV222',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': '09:00 AM-12:50 PM',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                },
                {
                    'CRN': '40662',
                    'campus': 'FC',
                    'course': 'C S F082A50Y',
                    'days': 'TBA',
                    'desc': 'INTRO SOFTWARE QUALITY ASSURAN',
                    'end': '06/29/2018',
                    'instructor': 'Staff',
                    'room': 'ONLINE',
                    'seats': '35',
                    'start': '04/09/2018',
                    'status': 'Open',
                    'time': 'TBA',
                    'units': '  4.50',
                    'wait_cap': '10',
                    'wait_seats': '10'
                }
            ]
        }
    }
]

snapshots['TestGetOne::test_get_one_dept_and_course 1'] = {
    '40403': [
        {
            'CRN': '40403',
            'campus': 'FH',
            'course': 'C S F002A01Y',
            'days': 'TTh',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Venkataraman',
            'room': '5609',
            'seats': '23',
            'start': '04/09/2018',
            'status': 'Open',
            'time': '08:00 AM-09:50 AM',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        },
        {
            'CRN': '40403',
            'campus': 'FH',
            'course': 'C S F002A01Y',
            'days': 'TBA',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Venkataraman',
            'room': 'ONLINE',
            'seats': '23',
            'start': '04/09/2018',
            'status': 'Open',
            'time': 'TBA',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        }
    ],
    '40405': [
        {
            'CRN': '40405',
            'campus': 'FH',
            'course': 'C S F002A03W',
            'days': 'TBA',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Venkataraman',
            'room': 'ONLINE',
            'seats': '7',
            'start': '04/09/2018',
            'status': 'Open',
            'time': 'TBA',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        }
    ],
    '40589': [
        {
            'CRN': '40589',
            'campus': 'FH',
            'course': 'C S F002A04W',
            'days': 'TBA',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Harden',
            'room': 'ONLINE',
            'seats': '0',
            'start': '04/09/2018',
            'status': 'Waitlist',
            'time': 'TBA',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '9'
        }
    ],
    '42071': [
        {
            'CRN': '42071',
            'campus': 'FH',
            'course': 'C S F002A02Y',
            'days': 'TTh',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Oluwasanmi',
            'room': '5607',
            'seats': '37',
            'start': '04/09/2018',
            'status': 'Open',
            'time': '06:30 PM-08:20 PM',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        },
        {
            'CRN': '42071',
            'campus': 'FH',
            'course': 'C S F002A02Y',
            'days': 'TBA',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Oluwasanmi',
            'room': 'ONLINE',
            'seats': '37',
            'start': '04/09/2018',
            'status': 'Open',
            'time': 'TBA',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        }
    ],
    '42072': [
        {
            'CRN': '42072',
            'campus': 'FH',
            'course': 'C S F002A05W',
            'days': 'TBA',
            'desc': 'OBJ-ORIENT PROG METHOD IN C++',
            'end': '06/29/2018',
            'instructor': 'Gentry-Kolen',
            'room': 'ONLINE',
            'seats': '30',
            'start': '04/09/2018',
            'status': 'Open',
            'time': 'TBA',
            'units': '  4.50',
            'wait_cap': '10',
            'wait_seats': '10'
        }
    ]
}

snapshots['TestGetMany::test_get_many_dept 1'] = [
    [
        {
            '10': {
                '40408': [
                    {
                        'CRN': '40408',
                        'campus': 'FH',
                        'course': 'C S F010.01Y',
                        'days': 'TTh',
                        'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                        'end': '06/29/2018',
                        'instructor': 'Riordan',
                        'room': '5610',
                        'seats': '15',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40408',
                        'campus': 'FH',
                        'course': 'C S F010.01Y',
                        'days': 'TBA',
                        'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                        'end': '06/29/2018',
                        'instructor': 'Riordan',
                        'room': 'ONLINE',
                        'seats': '15',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40890': [
                    {
                        'CRN': '40890',
                        'campus': 'FH',
                        'course': 'C S F010.02W',
                        'days': 'TBA',
                        'desc': 'COMPUTER ARCHITEC/ORGANIZATION',
                        'end': '06/29/2018',
                        'instructor': 'Lamble',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ]
            },
            '18': {
                '41406': [
                    {
                        'CRN': '41406',
                        'campus': 'FH',
                        'course': 'C S F018.01',
                        'days': 'MW',
                        'desc': 'DISCRETE MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Morriss',
                        'room': '4502',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ],
                '41407': [
                    {
                        'CRN': '41407',
                        'campus': 'FH',
                        'course': 'C S F018.02',
                        'days': 'MW',
                        'desc': 'DISCRETE MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Witschorik',
                        'room': '5601',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '1A': {
                '40397': [
                    {
                        'CRN': '40397',
                        'campus': 'FH',
                        'course': 'C S F001A01Y',
                        'days': 'TTh',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Haight',
                        'room': '4308',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40397',
                        'campus': 'FH',
                        'course': 'C S F001A01Y',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Haight',
                        'room': 'ONLINE',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40568': [
                    {
                        'CRN': '40568',
                        'campus': 'FH',
                        'course': 'C S F001A04W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Cecil',
                        'room': 'ONLINE',
                        'seats': '4',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42061': [
                    {
                        'CRN': '42061',
                        'campus': 'FH',
                        'course': 'C S F001A02Y',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42061',
                        'campus': 'FH',
                        'course': 'C S F001A02Y',
                        'days': 'TTh',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Mazloom',
                        'room': '4308',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42062': [
                    {
                        'CRN': '42062',
                        'campus': 'FH',
                        'course': 'C S F001A03Y',
                        'days': 'MW',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': '5614',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-07:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42062',
                        'campus': 'FH',
                        'course': 'C S F001A03Y',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42063': [
                    {
                        'CRN': '42063',
                        'campus': 'FH',
                        'course': 'C S F001A05W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Krishnan',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '7'
                    }
                ],
                '42064': [
                    {
                        'CRN': '42064',
                        'campus': 'FH',
                        'course': 'C S F001A06W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Ibrahim',
                        'room': 'ONLINE',
                        'seats': '39',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42065': [
                    {
                        'CRN': '42065',
                        'campus': 'FH',
                        'course': 'C S F001A07W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENTED PROG METHOD JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '05/21/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '1B': {
                '40400': [
                    {
                        'CRN': '40400',
                        'campus': 'FH',
                        'course': 'C S F001B02Y',
                        'days': 'TTh',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': '5602',
                        'seats': '36',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40400',
                        'campus': 'FH',
                        'course': 'C S F001B02Y',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '36',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40856': [
                    {
                        'CRN': '40856',
                        'campus': 'FH',
                        'course': 'C S F001B03W',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Pham',
                        'room': 'ONLINE',
                        'seats': '13',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42067': [
                    {
                        'CRN': '42067',
                        'campus': 'FH',
                        'course': 'C S F001B01Y',
                        'days': 'MW',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Mazloom',
                        'room': '4308',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42067',
                        'campus': 'FH',
                        'course': 'C S F001B01Y',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42068': [
                    {
                        'CRN': '42068',
                        'campus': 'FH',
                        'course': 'C S F001B04W',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Harden',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ],
                '42069': [
                    {
                        'CRN': '42069',
                        'campus': 'FH',
                        'course': 'C S F001B05W',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN IN JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '1C': {
                '40402': [
                    {
                        'CRN': '40402',
                        'campus': 'FH',
                        'course': 'C S F001C01Y',
                        'days': 'MW',
                        'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Weusijana',
                        'room': '5602',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40402',
                        'campus': 'FH',
                        'course': 'C S F001C01Y',
                        'days': 'TBA',
                        'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Weusijana',
                        'room': 'ONLINE',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40746': [
                    {
                        'CRN': '40746',
                        'campus': 'FH',
                        'course': 'C S F001C02W',
                        'days': 'TBA',
                        'desc': 'ADV DATA STRUCT/ALGORMS JAVA',
                        'end': '06/29/2018',
                        'instructor': 'Mazloom',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ]
            },
            '20A': {
                '42127': [
                    {
                        'CRN': '42127',
                        'campus': 'FH',
                        'course': 'C S F020A01W',
                        'days': 'TBA',
                        'desc': 'PROGRAMMING IN C#',
                        'end': '06/29/2018',
                        'instructor': 'Meade',
                        'room': 'ONLINE',
                        'seats': '23',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '21A': {
                '40597': [
                    {
                        'CRN': '40597',
                        'campus': 'FH',
                        'course': 'C S F021A02W',
                        'days': 'TBA',
                        'desc': 'PYTHON FOR PROGRAMMERS',
                        'end': '06/29/2018',
                        'instructor': 'Khayrallah',
                        'room': 'ONLINE',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41543': [
                    {
                        'CRN': '41543',
                        'campus': 'FH',
                        'course': 'C S F021A03W',
                        'days': 'TBA',
                        'desc': 'PYTHON FOR PROGRAMMERS',
                        'end': '06/29/2018',
                        'instructor': 'Xiong',
                        'room': 'ONLINE',
                        'seats': '38',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42090': [
                    {
                        'CRN': '42090',
                        'campus': 'FH',
                        'course': 'C S F021A01Y',
                        'days': 'TTh',
                        'desc': 'PYTHON FOR PROGRAMMERS',
                        'end': '06/29/2018',
                        'instructor': 'Van Der Linden',
                        'room': '5609',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42090',
                        'campus': 'FH',
                        'course': 'C S F021A01Y',
                        'days': 'TBA',
                        'desc': 'PYTHON FOR PROGRAMMERS',
                        'end': '06/29/2018',
                        'instructor': 'Van Der Linden',
                        'room': 'ONLINE',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42091': [
                    {
                        'CRN': '42091',
                        'campus': 'FH',
                        'course': 'C S F021A04W',
                        'days': 'TBA',
                        'desc': 'PYTHON FOR PROGRAMMERS',
                        'end': '06/29/2018',
                        'instructor': 'Cecil',
                        'room': 'ONLINE',
                        'seats': '34',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '21B': {
                '42093': [
                    {
                        'CRN': '42093',
                        'campus': 'FH',
                        'course': 'C S F021B02W',
                        'days': 'TBA',
                        'desc': 'INTRM PYTHON PROGRAMMING',
                        'end': '06/29/2018',
                        'instructor': 'Lamble',
                        'room': 'ONLINE',
                        'seats': '4',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '22A': {
                '40571': [
                    {
                        'CRN': '40571',
                        'campus': 'FH',
                        'course': 'C S F022A01W',
                        'days': 'TBA',
                        'desc': 'JAVASCRIPT FOR PROGRAMERS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '39',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42128': [
                    {
                        'CRN': '42128',
                        'campus': 'FH',
                        'course': 'C S F022A02W',
                        'days': 'TBA',
                        'desc': 'JAVASCRIPT FOR PROGRAMERS',
                        'end': '06/29/2018',
                        'instructor': 'Meade',
                        'room': 'ONLINE',
                        'seats': '11',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42133': [
                    {
                        'CRN': '42133',
                        'campus': 'FH',
                        'course': 'C S F022A03W',
                        'days': 'TBA',
                        'desc': 'JAVASCRIPT FOR PROGRAMERS',
                        'end': '06/29/2018',
                        'instructor': 'Weusijana',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '2A': {
                '40403': [
                    {
                        'CRN': '40403',
                        'campus': 'FH',
                        'course': 'C S F002A01Y',
                        'days': 'TTh',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Venkataraman',
                        'room': '5609',
                        'seats': '23',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40403',
                        'campus': 'FH',
                        'course': 'C S F002A01Y',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'seats': '23',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40405': [
                    {
                        'CRN': '40405',
                        'campus': 'FH',
                        'course': 'C S F002A03W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'seats': '7',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40589': [
                    {
                        'CRN': '40589',
                        'campus': 'FH',
                        'course': 'C S F002A04W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Harden',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '9'
                    }
                ],
                '42071': [
                    {
                        'CRN': '42071',
                        'campus': 'FH',
                        'course': 'C S F002A02Y',
                        'days': 'TTh',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Oluwasanmi',
                        'room': '5607',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42071',
                        'campus': 'FH',
                        'course': 'C S F002A02Y',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Oluwasanmi',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42072': [
                    {
                        'CRN': '42072',
                        'campus': 'FH',
                        'course': 'C S F002A05W',
                        'days': 'TBA',
                        'desc': 'OBJ-ORIENT PROG METHOD IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Gentry-Kolen',
                        'room': 'ONLINE',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '2B': {
                '40406': [
                    {
                        'CRN': '40406',
                        'campus': 'FH',
                        'course': 'C S F002B02W',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Harden',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '4'
                    }
                ],
                '40651': [
                    {
                        'CRN': '40651',
                        'campus': 'FH',
                        'course': 'C S F002B01Y',
                        'days': 'MW',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Dhagat',
                        'room': '5602',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40651',
                        'campus': 'FH',
                        'course': 'C S F002B01Y',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Dhagat',
                        'room': 'ONLINE',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41360': [
                    {
                        'CRN': '41360',
                        'campus': 'FH',
                        'course': 'C S F002B03W',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Pham',
                        'room': 'ONLINE',
                        'seats': '34',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42112': [
                    {
                        'CRN': '42112',
                        'campus': 'FH',
                        'course': 'C S F002B04Y',
                        'days': 'MW',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Lankester',
                        'room': '5610',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42112',
                        'campus': 'FH',
                        'course': 'C S F002B04Y',
                        'days': 'TBA',
                        'desc': 'INTERM SOFTWARE DESIGN C++',
                        'end': '06/29/2018',
                        'instructor': 'Lankester',
                        'room': 'ONLINE',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '2C': {
                '40407': [
                    {
                        'CRN': '40407',
                        'campus': 'FH',
                        'course': 'C S F002C01Y',
                        'days': 'TTh',
                        'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Lankester',
                        'room': '5607',
                        'seats': '17',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:20 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40407',
                        'campus': 'FH',
                        'course': 'C S F002C01Y',
                        'days': 'TBA',
                        'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Lankester',
                        'room': 'ONLINE',
                        'seats': '17',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40754': [
                    {
                        'CRN': '40754',
                        'campus': 'FH',
                        'course': 'C S F002C02W',
                        'days': 'TBA',
                        'desc': 'ADV DATA  STRUCT/ALGRM IN C++',
                        'end': '06/29/2018',
                        'instructor': 'Venkataraman',
                        'room': 'ONLINE',
                        'seats': '3',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '30A': {
                '40572': [
                    {
                        'CRN': '40572',
                        'campus': 'FH',
                        'course': 'C S F030A01W',
                        'days': 'TBA',
                        'desc': 'INTRODUCTION TO LINUX',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'seats': '13',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '30B': {
                '41311': [
                    {
                        'CRN': '41311',
                        'campus': 'FH',
                        'course': 'C S F030B01W',
                        'days': 'TBA',
                        'desc': 'LINUX SHELL PROGRAMMING',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '31A': {
                '40654': [
                    {
                        'CRN': '40654',
                        'campus': 'FH',
                        'course': 'C S F031A01W',
                        'days': 'TBA',
                        'desc': 'INTRO DATABASE MGMT SYSTEMS',
                        'end': '06/29/2018',
                        'instructor': 'Ibrahim',
                        'room': 'ONLINE',
                        'seats': '17',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '3A': {
                '42073': [
                    {
                        'CRN': '42073',
                        'campus': 'FH',
                        'course': 'C S F003A01Y',
                        'days': 'MW',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Haight',
                        'room': '4306',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42073',
                        'campus': 'FH',
                        'course': 'C S F003A01Y',
                        'days': 'TBA',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Haight',
                        'room': 'ONLINE',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42074': [
                    {
                        'CRN': '42074',
                        'campus': 'FH',
                        'course': 'C S F003A02W',
                        'days': 'TBA',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Lai',
                        'room': 'ONLINE',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42075': [
                    {
                        'CRN': '42075',
                        'campus': 'FH',
                        'course': 'C S F003A03W',
                        'days': 'TBA',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Xiong',
                        'room': 'ONLINE',
                        'seats': '29',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42076': [
                    {
                        'CRN': '42076',
                        'campus': 'FH',
                        'course': 'C S F003A04W',
                        'days': 'TBA',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Lai',
                        'room': 'ONLINE',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42077': [
                    {
                        'CRN': '42077',
                        'campus': 'FH',
                        'course': 'C S F003A05W',
                        'days': 'TBA',
                        'desc': 'OBJECT ORIEN PRGM METH PYTHON',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '05/21/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '49': {
                '40891': [
                    {
                        'CRN': '40891',
                        'campus': 'FH',
                        'course': 'C S F049.02W',
                        'days': 'TBA',
                        'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                        'end': '06/29/2018',
                        'instructor': 'Agarwal',
                        'room': 'ONLINE',
                        'seats': '16',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  2.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42094': [
                    {
                        'CRN': '42094',
                        'campus': 'FH',
                        'course': 'C S F049.01Y',
                        'days': 'TBA',
                        'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                        'end': '06/29/2018',
                        'instructor': 'Barnard',
                        'room': 'ONLINE',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  2.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42094',
                        'campus': 'FH',
                        'course': 'C S F049.01Y',
                        'days': 'W',
                        'desc': 'FOUNDATIONS OF COMPUTER PROGRA',
                        'end': '06/29/2018',
                        'instructor': 'Barnard',
                        'room': '4302',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:20 PM',
                        'units': '  2.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '50A': {
                '40410': [
                    {
                        'CRN': '40410',
                        'campus': 'FH',
                        'course': 'C S F050A01Y',
                        'days': 'T',
                        'desc': 'NETWORK BASICS (CCNA)',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': '4308',
                        'seats': '34',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40410',
                        'campus': 'FH',
                        'course': 'C S F050A01Y',
                        'days': 'TBA',
                        'desc': 'NETWORK BASICS (CCNA)',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'seats': '34',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '50C': {
                '42095': [
                    {
                        'CRN': '42095',
                        'campus': 'FH',
                        'course': 'C S F050C01Y',
                        'days': 'M',
                        'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': '4308',
                        'seats': '36',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42095',
                        'campus': 'FH',
                        'course': 'C S F050C01Y',
                        'days': 'TBA',
                        'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'seats': '36',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42115': [
                    {
                        'CRN': '42115',
                        'campus': 'FH',
                        'course': 'C S F050C02W',
                        'days': 'TBA',
                        'desc': 'SCALING LOCAL AREA NTWR (CCNA)',
                        'end': '06/29/2018',
                        'instructor': 'Murphy',
                        'room': 'ONLINE',
                        'seats': '36',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '50E': {
                '41312': [
                    {
                        'CRN': '41312',
                        'campus': 'FH',
                        'course': 'C S F050E01Y',
                        'days': 'W',
                        'desc': 'INTRO TO IP NETWORK SECURITY',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': '4308',
                        'seats': '38',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '41312',
                        'campus': 'FH',
                        'course': 'C S F050E01Y',
                        'days': 'TBA',
                        'desc': 'INTRO TO IP NETWORK SECURITY',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '38',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '53A': {
                '42116': [
                    {
                        'CRN': '42116',
                        'campus': 'FH',
                        'course': 'C S F053A01Y',
                        'days': 'M',
                        'desc': 'CYBERSECURITY FUNDAMENTALS',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': '4306',
                        'seats': '39',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42116',
                        'campus': 'FH',
                        'course': 'C S F053A01Y',
                        'days': 'TBA',
                        'desc': 'CYBERSECURITY FUNDAMENTALS',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': 'ONLINE',
                        'seats': '39',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42117': [
                    {
                        'CRN': '42117',
                        'campus': 'FH',
                        'course': 'C S F053A02W',
                        'days': 'TBA',
                        'desc': 'CYBERSECURITY FUNDAMENTALS',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': 'ONLINE',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '53B': {
                '42118': [
                    {
                        'CRN': '42118',
                        'campus': 'FH',
                        'course': 'C S F053B01Y',
                        'days': 'W',
                        'desc': 'FIREWALLS & THREAT MANAGEMENT',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': '5609',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42118',
                        'campus': 'FH',
                        'course': 'C S F053B01Y',
                        'days': 'TBA',
                        'desc': 'FIREWALLS & THREAT MANAGEMENT',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42119': [
                    {
                        'CRN': '42119',
                        'campus': 'FH',
                        'course': 'C S F053B02W',
                        'days': 'TBA',
                        'desc': 'FIREWALLS & THREAT MANAGEMENT',
                        'end': '06/29/2018',
                        'instructor': 'Ryan',
                        'room': 'ONLINE',
                        'seats': '33',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '60A': {
                '42120': [
                    {
                        'CRN': '42120',
                        'campus': 'FH',
                        'course': 'C S F060A01Y',
                        'days': 'W',
                        'desc': 'INSTALL/CONFIRG WINDOW SERVR 1',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': '4306',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-09:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42120',
                        'campus': 'FH',
                        'course': 'C S F060A01Y',
                        'days': 'TBA',
                        'desc': 'INSTALL/CONFIRG WINDOW SERVR 1',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '63A': {
                '42121': [
                    {
                        'CRN': '42121',
                        'campus': 'FH',
                        'course': 'C S F063A01W',
                        'days': 'TBA',
                        'desc': 'DEVELOPING APPLICATION FOR IOS',
                        'end': '06/29/2018',
                        'instructor': 'Gentry-Kolen',
                        'room': 'ONLINE',
                        'seats': '27',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '80A': {
                '42122': [
                    {
                        'CRN': '42122',
                        'campus': 'FH',
                        'course': 'C S F080A01W',
                        'days': 'TBA',
                        'desc': 'OPEN SOURCE CONTRIBUTION',
                        'end': '06/29/2018',
                        'instructor': 'Kosar',
                        'room': 'ONLINE',
                        'seats': '29',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '81A': {
                '42123': [
                    {
                        'CRN': '42123',
                        'campus': 'FH',
                        'course': 'C S F081A01W',
                        'days': 'TBA',
                        'desc': '3-D GRAPHICS PROGRAMMING',
                        'end': '06/29/2018',
                        'instructor': 'Trinh',
                        'room': 'ONLINE',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '82A': {
                '40662': [
                    {
                        'CRN': '40662',
                        'campus': 'FC',
                        'course': 'C S F082A50Y',
                        'days': 'S',
                        'desc': 'INTRO SOFTWARE QUALITY ASSURAN',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'SV222',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-12:50 PM',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40662',
                        'campus': 'FC',
                        'course': 'C S F082A50Y',
                        'days': 'TBA',
                        'desc': 'INTRO SOFTWARE QUALITY ASSURAN',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'ONLINE',
                        'seats': '35',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  4.50',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            }
        }
    ],
    [
        {
            '10': {
                '40153': [
                    {
                        'CRN': '40153',
                        'campus': 'FH',
                        'course': 'MATH F010.01Y',
                        'days': 'M',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': '5502',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:30 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40153',
                        'campus': 'FH',
                        'course': 'MATH F010.01Y',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40156': [
                    {
                        'CRN': '40156',
                        'campus': 'FH',
                        'course': 'MATH F010.03W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Low',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '9'
                    }
                ],
                '40312': [
                    {
                        'CRN': '40312',
                        'campus': 'FH',
                        'course': 'MATH F010.08W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40335': [
                    {
                        'CRN': '40335',
                        'campus': 'FH',
                        'course': 'MATH F010.02',
                        'days': 'TTh',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Munoz',
                        'room': '5601',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40335',
                        'campus': 'FH',
                        'course': 'MATH F010.02',
                        'days': 'F',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Munoz',
                        'room': '5601',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40374': [
                    {
                        'CRN': '40374',
                        'campus': 'FH',
                        'course': 'MATH F010.07',
                        'days': 'TTh',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Morriss',
                        'room': '4604',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '8'
                    }
                ],
                '40375': [
                    {
                        'CRN': '40375',
                        'campus': 'FH',
                        'course': 'MATH F010.09W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Seelbach',
                        'room': 'ONLINE',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40519': [
                    {
                        'CRN': '40519',
                        'campus': 'FH',
                        'course': 'MATH F010.06',
                        'days': 'TThF',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Francisco',
                        'room': '4310',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '12:00 PM-01:25 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40523': [
                    {
                        'CRN': '40523',
                        'campus': 'FH',
                        'course': 'MATH F010.04',
                        'days': 'F',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Tomutiu',
                        'room': '4606',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40523',
                        'campus': 'FH',
                        'course': 'MATH F010.04',
                        'days': 'MW',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Tomutiu',
                        'room': '4606',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40525': [
                    {
                        'CRN': '40525',
                        'campus': 'FC',
                        'course': 'MATH F010.50',
                        'days': 'MW',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Butterworth',
                        'room': 'SV204',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40731': [
                    {
                        'CRN': '40731',
                        'campus': 'FH',
                        'course': 'MATH F010.10W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Maskalevich',
                        'room': 'ONLINE',
                        'seats': '39',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40755': [
                    {
                        'CRN': '40755',
                        'campus': 'FH',
                        'course': 'MATH F010.05',
                        'days': 'F',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Morriss',
                        'room': '4606',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '4'
                    },
                    {
                        'CRN': '40755',
                        'campus': 'FH',
                        'course': 'MATH F010.05',
                        'days': 'TTh',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Morriss',
                        'room': '4606',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '4'
                    }
                ],
                '40903': [
                    {
                        'CRN': '40903',
                        'campus': 'FH',
                        'course': 'MATH F010.11W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Maskalevich',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41912': [
                    {
                        'CRN': '41912',
                        'campus': 'FH',
                        'course': 'MATH F010.12',
                        'days': 'MW',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Papay',
                        'room': '4601',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42060': [
                    {
                        'CRN': '42060',
                        'campus': 'FH',
                        'course': 'MATH F010.13W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Butterworth',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '05/21/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ],
                '42157': [
                    {
                        'CRN': '42157',
                        'campus': 'FH',
                        'course': 'MATH F010.14W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Low',
                        'room': 'ONLINE',
                        'seats': '8',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42224': [
                    {
                        'CRN': '42224',
                        'campus': 'FH',
                        'course': 'MATH F010.15W',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Seelbach',
                        'room': 'ONLINE',
                        'seats': '37',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42227': [
                    {
                        'CRN': '42227',
                        'campus': 'FC',
                        'course': 'MATH F010.07Y',
                        'days': 'F',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': 'SV203',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-12:20 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42227',
                        'campus': 'FC',
                        'course': 'MATH F010.07Y',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY STATISTICS',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '105': {
                '40159': [
                    {
                        'CRN': '40159',
                        'campus': 'FH',
                        'course': 'MATH F105.02Y',
                        'days': 'TBA',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Sinclair',
                        'room': 'ONLINE',
                        'seats': '18',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40159',
                        'campus': 'FH',
                        'course': 'MATH F105.02Y',
                        'days': 'MW',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Sinclair',
                        'room': '4302',
                        'seats': '18',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40160': [
                    {
                        'CRN': '40160',
                        'campus': 'FH',
                        'course': 'MATH F105.03Y',
                        'days': 'T',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': '5609',
                        'seats': '18',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:30 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40160',
                        'campus': 'FH',
                        'course': 'MATH F105.03Y',
                        'days': 'TBA',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Martinez',
                        'room': 'ONLINE',
                        'seats': '18',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40161': [
                    {
                        'CRN': '40161',
                        'campus': 'FH',
                        'course': 'MATH F105.04',
                        'days': 'F',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '5614',
                        'seats': '13',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40161',
                        'campus': 'FH',
                        'course': 'MATH F105.04',
                        'days': 'TTh',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '5614',
                        'seats': '13',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40165': [
                    {
                        'CRN': '40165',
                        'campus': 'FH',
                        'course': 'MATH F105.06Y',
                        'days': 'TBA',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'McLennan',
                        'room': 'ONLINE',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40165',
                        'campus': 'FH',
                        'course': 'MATH F105.06Y',
                        'days': 'M',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'McLennan',
                        'room': '5607',
                        'seats': '32',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40348': [
                    {
                        'CRN': '40348',
                        'campus': 'FH',
                        'course': 'MATH F105.07W',
                        'days': 'TBA',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Perino',
                        'room': 'ONLINE',
                        'seats': '16',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40544': [
                    {
                        'CRN': '40544',
                        'campus': 'FH',
                        'course': 'MATH F105.01',
                        'days': 'F',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '5609',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40544',
                        'campus': 'FH',
                        'course': 'MATH F105.01',
                        'days': 'MW',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '5609',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40936': [
                    {
                        'CRN': '40936',
                        'campus': 'FH',
                        'course': 'MATH F105.08W',
                        'days': 'TBA',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'seats': '9',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41952': [
                    {
                        'CRN': '41952',
                        'campus': 'FH',
                        'course': 'MATH F105.05',
                        'days': 'MWF',
                        'desc': 'INTERMEDIATE ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Reese',
                        'room': '5610',
                        'seats': '19',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '12:00 PM-01:25 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '108': {
                '42212': [
                    {
                        'CRN': '42212',
                        'campus': 'FH',
                        'course': 'MATH F108.01Y',
                        'days': 'TBA',
                        'desc': 'ACCELERATED ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Sinclair',
                        'room': 'ONLINE',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': ' 10.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42212',
                        'campus': 'FH',
                        'course': 'MATH F108.01Y',
                        'days': 'MTWTh',
                        'desc': 'ACCELERATED ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Sinclair',
                        'room': '5610',
                        'seats': '30',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '07:30 AM-09:20 AM',
                        'units': ' 10.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '12': {
                '40376': [
                    {
                        'CRN': '40376',
                        'campus': 'FC',
                        'course': 'MATH F012.50',
                        'days': 'TTh',
                        'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                        'end': '06/29/2018',
                        'instructor': 'Witschorik',
                        'room': 'SV209',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41920': [
                    {
                        'CRN': '41920',
                        'campus': 'FH',
                        'course': 'MATH F012.01Y',
                        'days': 'TTh',
                        'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                        'end': '06/29/2018',
                        'instructor': 'Knobel',
                        'room': '4604',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '41920',
                        'campus': 'FH',
                        'course': 'MATH F012.01Y',
                        'days': 'TBA',
                        'desc': 'CALCULUS FOR BUSINESS & ECONOM',
                        'end': '06/29/2018',
                        'instructor': 'Knobel',
                        'room': 'ONLINE',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '1A': {
                '40142': [
                    {
                        'CRN': '40142',
                        'campus': 'FH',
                        'course': 'MATH F001A02',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4604',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '1'
                    },
                    {
                        'CRN': '40142',
                        'campus': 'FH',
                        'course': 'MATH F001A02',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4604',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '1'
                    }
                ],
                '40143': [
                    {
                        'CRN': '40143',
                        'campus': 'FH',
                        'course': 'MATH F001A03',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Knobel',
                        'room': '4601',
                        'seats': '24',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40143',
                        'campus': 'FH',
                        'course': 'MATH F001A03',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Knobel',
                        'room': '4601',
                        'seats': '24',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40369': [
                    {
                        'CRN': '40369',
                        'campus': 'FH',
                        'course': 'MATH F001A04',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4601',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40369',
                        'campus': 'FH',
                        'course': 'MATH F001A04',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4601',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40893': [
                    {
                        'CRN': '40893',
                        'campus': 'FH',
                        'course': 'MATH F001A06',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Knobel',
                        'room': '4605',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '41852': [
                    {
                        'CRN': '41852',
                        'campus': 'FH',
                        'course': 'MATH F001A07W',
                        'days': 'TBA',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '5'
                    }
                ],
                '42059': [
                    {
                        'CRN': '42059',
                        'campus': 'FH',
                        'course': 'MATH F001A08W',
                        'days': 'TBA',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '05/21/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '1B': {
                '40144': [
                    {
                        'CRN': '40144',
                        'campus': 'FH',
                        'course': 'MATH F001B01',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4601',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40144',
                        'campus': 'FH',
                        'course': 'MATH F001B01',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4601',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40145': [
                    {
                        'CRN': '40145',
                        'campus': 'FH',
                        'course': 'MATH F001B03',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Nghiem',
                        'room': '4605',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '1'
                    },
                    {
                        'CRN': '40145',
                        'campus': 'FH',
                        'course': 'MATH F001B03',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Nghiem',
                        'room': '4605',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '1'
                    }
                ],
                '40370': [
                    {
                        'CRN': '40370',
                        'campus': 'FC',
                        'course': 'MATH F001B05',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Florero Salinas',
                        'room': 'SV220',
                        'seats': '19',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:30 PM-08:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40495': [
                    {
                        'CRN': '40495',
                        'campus': 'FH',
                        'course': 'MATH F001B02',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Nghiem',
                        'room': '5601',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    },
                    {
                        'CRN': '40495',
                        'campus': 'FH',
                        'course': 'MATH F001B02',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Nghiem',
                        'room': '5601',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ],
                '42054': [
                    {
                        'CRN': '42054',
                        'campus': 'FH',
                        'course': 'MATH F001B04W',
                        'days': 'TBA',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Williams',
                        'room': 'ONLINE',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ]
            },
            '1C': {
                '40147': [
                    {
                        'CRN': '40147',
                        'campus': 'FH',
                        'course': 'MATH F001C01',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '4602',
                        'seats': '24',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40147',
                        'campus': 'FH',
                        'course': 'MATH F001C01',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Anderson',
                        'room': '4602',
                        'seats': '24',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40148': [
                    {
                        'CRN': '40148',
                        'campus': 'FH',
                        'course': 'MATH F001C02',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4605',
                        'seats': '8',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40148',
                        'campus': 'FH',
                        'course': 'MATH F001C02',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4605',
                        'seats': '8',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40149': [
                    {
                        'CRN': '40149',
                        'campus': 'FH',
                        'course': 'MATH F001C03',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4602',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40149',
                        'campus': 'FH',
                        'course': 'MATH F001C03',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4602',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40516': [
                    {
                        'CRN': '40516',
                        'campus': 'FH',
                        'course': 'MATH F001C04',
                        'days': 'TThF',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '5601',
                        'seats': '7',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '12:00 PM-01:25 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40517': [
                    {
                        'CRN': '40517',
                        'campus': 'FH',
                        'course': 'MATH F001C05',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Nosratieh',
                        'room': '4602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '7'
                    }
                ]
            },
            '1D': {
                '40150': [
                    {
                        'CRN': '40150',
                        'campus': 'FH',
                        'course': 'MATH F001D01',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '4604',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40150',
                        'campus': 'FH',
                        'course': 'MATH F001D01',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '4604',
                        'seats': '25',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40454': [
                    {
                        'CRN': '40454',
                        'campus': 'FH',
                        'course': 'MATH F001D02',
                        'days': 'TTh',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lublin',
                        'room': '5601',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    },
                    {
                        'CRN': '40454',
                        'campus': 'FH',
                        'course': 'MATH F001D02',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Lublin',
                        'room': '5601',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ],
                '40950': [
                    {
                        'CRN': '40950',
                        'campus': 'FH',
                        'course': 'MATH F001D03',
                        'days': 'MW',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Reese',
                        'room': '4603',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    },
                    {
                        'CRN': '40950',
                        'campus': 'FH',
                        'course': 'MATH F001D03',
                        'days': 'F',
                        'desc': 'CALCULUS',
                        'end': '06/29/2018',
                        'instructor': 'Reese',
                        'room': '4603',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ]
            },
            '22': {
                '40158': [
                    {
                        'CRN': '40158',
                        'campus': 'FH',
                        'course': 'MATH F022.01',
                        'days': 'MW',
                        'desc': 'DISCRETE MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Morriss',
                        'room': '4502',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40455': [
                    {
                        'CRN': '40455',
                        'campus': 'FH',
                        'course': 'MATH F022.02',
                        'days': 'MW',
                        'desc': 'DISCRETE MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Witschorik',
                        'room': '5601',
                        'seats': '4',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '220': {
                '40167': [
                    {
                        'CRN': '40167',
                        'campus': 'FH',
                        'course': 'MATH F220.02',
                        'days': 'F',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4221',
                        'seats': '14',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40167',
                        'campus': 'FH',
                        'course': 'MATH F220.02',
                        'days': 'TTh',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4221',
                        'seats': '14',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40382': [
                    {
                        'CRN': '40382',
                        'campus': 'FH',
                        'course': 'MATH F220.01',
                        'days': 'F',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4602',
                        'seats': '19',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40382',
                        'campus': 'FH',
                        'course': 'MATH F220.01',
                        'days': 'MW',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Litrus',
                        'room': '4602',
                        'seats': '19',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40724': [
                    {
                        'CRN': '40724',
                        'campus': 'FH',
                        'course': 'MATH F220.04',
                        'days': 'MW',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Low',
                        'room': '5609',
                        'seats': '15',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40935': [
                    {
                        'CRN': '40935',
                        'campus': 'FH',
                        'course': 'MATH F220.05',
                        'days': 'TTh',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Lieberman',
                        'room': '4605',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42058': [
                    {
                        'CRN': '42058',
                        'campus': 'FH',
                        'course': 'MATH F220.03Y',
                        'days': 'MW',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Perino',
                        'room': '5610',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '42058',
                        'campus': 'FH',
                        'course': 'MATH F220.03Y',
                        'days': 'TBA',
                        'desc': 'ELEMENTARY ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Perino',
                        'room': 'ONLINE',
                        'seats': '12',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': 'TBA',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '230': {
                '40170': [
                    {
                        'CRN': '40170',
                        'campus': 'FH',
                        'course': 'MATH F230.01',
                        'days': 'MTWThF',
                        'desc': 'PREP FOR ALGEBRA: LINEAR EQ/PR',
                        'end': '06/29/2018',
                        'instructor': 'Lam',
                        'room': '5602',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  6.00',
                        'wait_cap': '15',
                        'wait_seats': '15'
                    },
                    {
                        'CRN': '40170',
                        'campus': 'FH',
                        'course': 'MATH F230.01',
                        'days': 'MTWThF',
                        'desc': 'PREP FOR ALGEBRA: LINEAR EQ/PR',
                        'end': '06/29/2018',
                        'instructor': 'Lam',
                        'room': '5602',
                        'seats': '31',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:50 AM-11:50 AM',
                        'units': '  6.00',
                        'wait_cap': '15',
                        'wait_seats': '15'
                    }
                ],
                '41221': [
                    {
                        'CRN': '41221',
                        'campus': 'FH',
                        'course': 'MATH F230.05',
                        'days': 'MTWTh',
                        'desc': 'PREP FOR ALGEBRA: LINEAR EQ/PR',
                        'end': '06/29/2018',
                        'instructor': 'Reed',
                        'room': '5613',
                        'seats': '7',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-06:50 PM',
                        'units': '  6.00',
                        'wait_cap': '5',
                        'wait_seats': '5'
                    },
                    {
                        'CRN': '41221',
                        'campus': 'FH',
                        'course': 'MATH F230.05',
                        'days': 'MTWTh',
                        'desc': 'PREP FOR ALGEBRA: LINEAR EQ/PR',
                        'end': '06/29/2018',
                        'instructor': 'Reed',
                        'room': '5613',
                        'seats': '7',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '07:00 PM-08:15 PM',
                        'units': '  6.00',
                        'wait_cap': '5',
                        'wait_seats': '5'
                    }
                ]
            },
            '230J': {
                '40350': [
                    {
                        'CRN': '40350',
                        'campus': 'FH',
                        'course': 'MATH F230J01',
                        'days': 'TThF',
                        'desc': 'PREPARING FOR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Sukumar',
                        'room': '5607',
                        'seats': '23',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  3.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '42232': [
                    {
                        'CRN': '42232',
                        'campus': 'FH',
                        'course': 'MATH F230J02',
                        'days': 'TTh',
                        'desc': 'PREPARING FOR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Reed',
                        'room': '5612',
                        'seats': '1',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-07:15 PM',
                        'units': '  3.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '235': {
                '40172': [
                    {
                        'CRN': '40172',
                        'campus': 'FH',
                        'course': 'MATH F235.01',
                        'days': 'MTWThF',
                        'desc': 'PREPARING ALGEBRA:REAL NUMBERS',
                        'end': '06/29/2018',
                        'instructor': 'Lam',
                        'room': '5602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  6.00',
                        'wait_cap': '15',
                        'wait_seats': '15'
                    },
                    {
                        'CRN': '40172',
                        'campus': 'FH',
                        'course': 'MATH F235.01',
                        'days': 'MTWThF',
                        'desc': 'PREPARING ALGEBRA:REAL NUMBERS',
                        'end': '06/29/2018',
                        'instructor': 'Lam',
                        'room': '5602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:50 AM-11:50 AM',
                        'units': '  6.00',
                        'wait_cap': '15',
                        'wait_seats': '15'
                    }
                ],
                '41220': [
                    {
                        'CRN': '41220',
                        'campus': 'FH',
                        'course': 'MATH F235.05',
                        'days': 'MTWTh',
                        'desc': 'PREPARING ALGEBRA:REAL NUMBERS',
                        'end': '06/29/2018',
                        'instructor': 'Reed',
                        'room': '5613',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-06:50 PM',
                        'units': '  6.00',
                        'wait_cap': '5',
                        'wait_seats': '5'
                    },
                    {
                        'CRN': '41220',
                        'campus': 'FH',
                        'course': 'MATH F235.05',
                        'days': 'MTWTh',
                        'desc': 'PREPARING ALGEBRA:REAL NUMBERS',
                        'end': '06/29/2018',
                        'instructor': 'Reed',
                        'room': '5613',
                        'seats': '2',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '07:00 PM-08:15 PM',
                        'units': '  6.00',
                        'wait_cap': '5',
                        'wait_seats': '5'
                    }
                ]
            },
            '2A': {
                '40151': [
                    {
                        'CRN': '40151',
                        'campus': 'FH',
                        'course': 'MATH F002A01',
                        'days': 'MW',
                        'desc': 'DIFFERENTIAL EQUATIONS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '4601',
                        'seats': '21',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40151',
                        'campus': 'FH',
                        'course': 'MATH F002A01',
                        'days': 'F',
                        'desc': 'DIFFERENTIAL EQUATIONS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '4601',
                        'seats': '21',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40433': [
                    {
                        'CRN': '40433',
                        'campus': 'FH',
                        'course': 'MATH F002A02',
                        'days': 'TTh',
                        'desc': 'DIFFERENTIAL EQUATIONS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '5610',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40433',
                        'campus': 'FH',
                        'course': 'MATH F002A02',
                        'days': 'F',
                        'desc': 'DIFFERENTIAL EQUATIONS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '5610',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40518': [
                    {
                        'CRN': '40518',
                        'campus': 'FH',
                        'course': 'MATH F002A03',
                        'days': 'MW',
                        'desc': 'DIFFERENTIAL EQUATIONS',
                        'end': '06/29/2018',
                        'instructor': 'Park Lee',
                        'room': '4603',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '2B': {
                '40152': [
                    {
                        'CRN': '40152',
                        'campus': 'FH',
                        'course': 'MATH F002B02',
                        'days': 'MW',
                        'desc': 'LINEAR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '5614',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '7'
                    },
                    {
                        'CRN': '40152',
                        'campus': 'FH',
                        'course': 'MATH F002B02',
                        'days': 'F',
                        'desc': 'LINEAR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '5614',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '7'
                    }
                ],
                '40372': [
                    {
                        'CRN': '40372',
                        'campus': 'FH',
                        'course': 'MATH F002B01',
                        'days': 'MW',
                        'desc': 'LINEAR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4604',
                        'seats': '8',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40372',
                        'campus': 'FH',
                        'course': 'MATH F002B01',
                        'days': 'F',
                        'desc': 'LINEAR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Lee',
                        'room': '4604',
                        'seats': '8',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40954': [
                    {
                        'CRN': '40954',
                        'campus': 'FH',
                        'course': 'MATH F002B03',
                        'days': 'MW',
                        'desc': 'LINEAR ALGEBRA',
                        'end': '06/29/2018',
                        'instructor': 'Papay',
                        'room': '5502',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '8'
                    }
                ]
            },
            '48A': {
                '40337': [
                    {
                        'CRN': '40337',
                        'campus': 'FH',
                        'course': 'MATH F048A01',
                        'days': 'MW',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Uilecan',
                        'room': '4605',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40337',
                        'campus': 'FH',
                        'course': 'MATH F048A01',
                        'days': 'F',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Uilecan',
                        'room': '4605',
                        'seats': '26',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40338': [
                    {
                        'CRN': '40338',
                        'campus': 'FH',
                        'course': 'MATH F048A03',
                        'days': 'MW',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Uilecan',
                        'room': '4221',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40338',
                        'campus': 'FH',
                        'course': 'MATH F048A03',
                        'days': 'F',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Uilecan',
                        'room': '4221',
                        'seats': '28',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40339': [
                    {
                        'CRN': '40339',
                        'campus': 'FH',
                        'course': 'MATH F048A04',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Zwack',
                        'room': '4301',
                        'seats': '5',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40339',
                        'campus': 'FH',
                        'course': 'MATH F048A04',
                        'days': 'F',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Zwack',
                        'room': '4301',
                        'seats': '5',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40340': [
                    {
                        'CRN': '40340',
                        'campus': 'FH',
                        'course': 'MATH F048A05',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Zwack',
                        'room': '4603',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '9'
                    }
                ],
                '40579': [
                    {
                        'CRN': '40579',
                        'campus': 'FH',
                        'course': 'MATH F048A06',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS I',
                        'end': '06/29/2018',
                        'instructor': 'Ni',
                        'room': '4605',
                        'seats': '17',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '48B': {
                '40341': [
                    {
                        'CRN': '40341',
                        'campus': 'FH',
                        'course': 'MATH F048B01',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4603',
                        'seats': '20',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40341',
                        'campus': 'FH',
                        'course': 'MATH F048B01',
                        'days': 'F',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '4603',
                        'seats': '20',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '09:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40342': [
                    {
                        'CRN': '40342',
                        'campus': 'FH',
                        'course': 'MATH F048B02',
                        'days': 'MW',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Zwack',
                        'room': '4603',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '3'
                    },
                    {
                        'CRN': '40342',
                        'campus': 'FH',
                        'course': 'MATH F048B02',
                        'days': 'F',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Zwack',
                        'room': '4603',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '3'
                    }
                ],
                '40343': [
                    {
                        'CRN': '40343',
                        'campus': 'FH',
                        'course': 'MATH F048B03',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Francisco',
                        'room': '4310',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40343',
                        'campus': 'FH',
                        'course': 'MATH F048B03',
                        'days': 'F',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Francisco',
                        'room': '4310',
                        'seats': '10',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40379': [
                    {
                        'CRN': '40379',
                        'campus': 'FH',
                        'course': 'MATH F048B04',
                        'days': 'TThF',
                        'desc': 'PRECALCULUS II',
                        'end': '06/29/2018',
                        'instructor': 'Nghiem',
                        'room': '4601',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '12:00 PM-01:25 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ]
            },
            '48C': {
                '40344': [
                    {
                        'CRN': '40344',
                        'campus': 'FH',
                        'course': 'MATH F048CS01',
                        'days': 'F',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '5601',
                        'seats': '14',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-08:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40344',
                        'campus': 'FH',
                        'course': 'MATH F048CS01',
                        'days': 'MW',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Cembellin',
                        'room': '5601',
                        'seats': '14',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '08:00 AM-09:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40345': [
                    {
                        'CRN': '40345',
                        'campus': 'FH',
                        'course': 'MATH F048C02',
                        'days': 'MW',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Francisco',
                        'room': '4602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    },
                    {
                        'CRN': '40345',
                        'campus': 'FH',
                        'course': 'MATH F048C02',
                        'days': 'F',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Francisco',
                        'room': '4602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': '10:00 AM-10:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '0'
                    }
                ],
                '40380': [
                    {
                        'CRN': '40380',
                        'campus': 'FH',
                        'course': 'MATH F048C03',
                        'days': 'TTh',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Tomutiu',
                        'room': '4302',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '10:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    },
                    {
                        'CRN': '40380',
                        'campus': 'FH',
                        'course': 'MATH F048C03',
                        'days': 'F',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Tomutiu',
                        'room': '4302',
                        'seats': '22',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '11:00 AM-11:50 AM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40381': [
                    {
                        'CRN': '40381',
                        'campus': 'FH',
                        'course': 'MATH F048C04',
                        'days': 'MW',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Ni',
                        'room': '4604',
                        'seats': '11',
                        'start': '04/09/2018',
                        'status': 'Open',
                        'time': '01:30 PM-03:45 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '10'
                    }
                ],
                '40575': [
                    {
                        'CRN': '40575',
                        'campus': 'FH',
                        'course': 'MATH F048C05',
                        'days': 'MW',
                        'desc': 'PRECALCULUS III',
                        'end': '06/29/2018',
                        'instructor': 'Low',
                        'room': '4602',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Waitlist',
                        'time': '06:00 PM-08:15 PM',
                        'units': '  5.00',
                        'wait_cap': '10',
                        'wait_seats': '8'
                    }
                ]
            },
            '70R': {
                '40758': [
                    {
                        'CRN': '40758',
                        'campus': 'FH',
                        'course': 'MATH F070R01',
                        'days': 'TBA',
                        'desc': 'INDEPENDENT STUDY MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  1.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '71R': {
                '40759': [
                    {
                        'CRN': '40759',
                        'campus': 'FH',
                        'course': 'MATH F071R01',
                        'days': 'TBA',
                        'desc': 'INDEPENDENT STUDY MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  2.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ],
                '41575': [
                    {
                        'CRN': '41575',
                        'campus': 'FH',
                        'course': 'MATH F071R02',
                        'days': 'TBA',
                        'desc': 'INDEPENDENT STUDY MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  2.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '72R': {
                '40760': [
                    {
                        'CRN': '40760',
                        'campus': 'FH',
                        'course': 'MATH F072R01',
                        'days': 'TBA',
                        'desc': 'INDEPENDENT STUDY MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  3.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            },
            '73R': {
                '40761': [
                    {
                        'CRN': '40761',
                        'campus': 'FH',
                        'course': 'MATH F073R01',
                        'days': 'TBA',
                        'desc': 'INDEPENDENT STUDY MATHEMATICS',
                        'end': '06/29/2018',
                        'instructor': 'Staff',
                        'room': 'TBA',
                        'seats': '0',
                        'start': '04/09/2018',
                        'status': 'Full',
                        'time': 'TBA',
                        'units': '  4.00',
                        'wait_cap': '0',
                        'wait_seats': '0'
                    }
                ]
            }
        }
    ]
]
