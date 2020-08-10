from unittest import TestCase
from pytest import raises
from utils import parse_course_str, get_class_type, ValidationError

# Handpicked test cases for `parse_course_str()`
course_str_data = {
    # De Anza
    'ANTH D001L51Z': ('ANTH', '1L', '51Z', {'Z'}),
    'ARTS D001A62Z': ('ARTS', '1A', '62Z', {'Z'}),
    'ARTS D002F62Z': ('ARTS', '2F', '62Z', {'Z'}),
    'ARTS D002G61Z': ('ARTS', '2G', '61Z', {'Z'}),
    'ARTS D018D01Z': ('ARTS', '18D', '01Z', {'Z'}),
    'ARTS D03TC50Z': ('ARTS', '3TC', '50Z', {'Z'}),
    'ASAM D031.VED': ('ASAM', '31', 'VED', {'V', 'D', 'E'}),
    'ASTR D015L71Z': ('ASTR', '15L', '71Z', {'Z'}),
    'AUTO D060A49Z': ('AUTO', '60A', '49Z', {'Z'}),
    'AUTO D060F55Y': ('AUTO', '60F', '55Y', {'Y'}),
    'AUTO D065P50Z': ('AUTO', '65P', '50Z', {'Z'}),
    'AUTO D065W01': ('AUTO', '65W', '01', set()),
    'BIOL D054G62Z': ('BIOL', '54G', '62Z', {'Z'}),
    'BIOL D054H62Z': ('BIOL', '54H', '62Z', {'Z'}),
    'BIOL D077X65R': ('BIOL', '77X', '65R', {'R'}),
    'BIOL D077Y65R': ('BIOL', '77Y', '65R', {'R'}),
    'C D D010G50Z': ('CD', '10G', '50Z', {'Z'}),
    'C D D010H50Z': ('CD', '10H', '50Z', {'Z'}),
    'C D D012.1SZ': ('CD', '12', '1SZ', {'S', 'Z'}),
    'C D D059G50Z': ('CD', '59G', '50Z', {'Z'}),
    'CHEM D077.67R': ('CHEM', '77', '67R', {'R'}),
    'CHEM D077X65R': ('CHEM', '77X', '65R', {'R'}),
    'CIS D064G62Z': ('CIS', '64G', '62Z', {'Z'}),
    'CIS D21JA01Z': ('CIS', '21JA', '01Z', {'Z'}),
    'COMM D007.01D': ('COMM', '7', '01D', {'D'}),
    'COMM D010.01': ('COMM', '10', '01', set()),
    'DMT D054.61Y': ('DMT', '54', '61Y', {'Y'}),
    'DMT D077G65R': ('DMT', '77G', '65R', {'R'}),
    'DMT D077H65R': ('DMT', '77H', '65R', {'R'}),
    'DMT D077J65R': ('DMT', '77J', '65R', {'R'}),
    'DMT D077Y65R': ('DMT', '77Y', '65R', {'R'}),
    'DMT D087D61Y': ('DMT', '87D', '61Y', {'Y'}),
    'DMT D087J61Y': ('DMT', '87J', '61Y', {'Y'}),
    'DMT D101.01': ('DMT', '101', '01', set()),
    'E S D061L62Z': ('ES', '61L', '62Z', {'Z'}),
    'E S D077X65R': ('ES', '77X', '65R', {'R'}),
    'E S D077Y65R': ('ES', '77Y', '65R', {'R'}),
    'E S D077Z65R': ('ES', '77Z', '65R', {'R'}),
    'EDAC D232T01F': ('EDAC', '232T', '01F', {'F'}),
    'EDAC D232V01F': ('EDAC', '232V', '01F', {'F'}),
    'ESCI D001L01Z': ('ESCI', '1L', '01Z', {'Z'}),
    'ESL D251.2ZL': ('ESL', '251', '2ZL', {'L', 'Z'}),
    'EWRT D001A06Q': ('EWRT', '1A', '06Q', {'Q'}),
    'EWRT D001A1PQ': ('EWRT', '1A', '1PQ', {'P', 'Q'}),
    'EWRT D001A1WQ': ('EWRT', '1A', '1WQ', {'W', 'Q'}),
    'EWRT D001A20Q': ('EWRT', '1A', '20Q', {'Q'}),
    'EWRT D001A41D': ('EWRT', '1A', '41D', {'D'}),
    'EWRT D001AFYQ': ('EWRT', '1A', 'FYQ', {'Y', 'F', 'Q'}),
    'EWRT D001AKED': ('EWRT', '1A', 'KED', {'K', 'E', 'D'}),
    'EWRT D001AR2Q': ('EWRT', '1A', 'R2Q', {'R', 'Q'}),
    'EWRT D001AVQD': ('EWRT', '1A', 'VQD', {'V', 'D', 'Q'}),
    'EWRT D01AH01Z': ('EWRT', '1AH', '01Z', {'Z'}),
    'EWRT D01AS03Z': ('EWRT', '1AS', '03Z', {'Z'}),
    'EWRT D01ASFY1': ('EWRT', '1AS', 'FY1', {'Y', 'F'}),
    'EWRT D01AT01Z': ('EWRT', '1AT', '01Z', {'Z'}),
    'F/TV D072J01Z': ('F/TV', '72J', '01Z', {'Z'}),
    'HTEC D060H02Z': ('HTEC', '60H', '02Z', {'Z'}),
    'HTEC D068.01F': ('HTEC', '68', '01F', {'F'}),
    'HTEC D090G01Y': ('HTEC', '90G', '01Y', {'Y'}),
    'HTEC D101C61Z': ('HTEC', '101C', '61Z', {'Z'}),
    'HTEC D101D02Y': ('HTEC', '101D', '02Y', {'Y'}),
    'HTEC D101K01Z': ('HTEC', '101K', '01Z', {'Z'}),
    'HTEC D101L01': ('HTEC', '101L', '01', set()),
    'HTEC D101M01': ('HTEC', '101M', '01', set()),
    'HUMA D020.1PD': ('HUMA', '20', '1PD', {'D', 'P'}),
    'HUMI D006.1MZ': ('HUMI', '6', '1MZ', {'M', 'Z'}),
    'ICS D017.1EZ': ('ICS', '17', '1EZ', {'E', 'Z'}),
    'ICS D077X65R': ('ICS', '77X', '65R', {'R'}),
    'ICS D078W65R': ('ICS', '78W', '65R', {'R'}),
    'KNES D012G01Z': ('KNES', '12G', '01Z', {'Z'}),
    'KNES D015E02Z': ('KNES', '15E', '02Z', {'Z'}),
    'KNES D019G02Z': ('KNES', '19G', '02Z', {'Z'}),
    'KNES D09AX62Z': ('KNES', '9AX', '62Z', {'Z'}),
    'KNES D15EX01Z': ('KNES', '15EX', '01Z', {'Z'}),
    'LART D250.01Q': ('LART', '250', '01Q', {'Q'}),
    'LART D250.1PQ': ('LART', '250', '1PQ', {'P', 'Q'}),
    'LART D250.1WQ': ('LART', '250', '1WQ', {'W', 'Q'}),
    'LART D250.FYQ': ('LART', '250', 'FYQ', {'Y', 'F', 'Q'}),
    'LART D250.R2Q': ('LART', '250', 'R2Q', {'R', 'Q'}),
    'LART D250.VQD': ('LART', '250', 'VQD', {'V', 'D', 'Q'}),
    'LRNA D077.65R': ('LRNA', '77', '65R', {'R'}),
    'MATH D010.MP2': ('MATH', '10', 'MP2', {'M', 'P'}),
    'MATH D010.Q13': ('MATH', '10', 'Q13', {'Q'}),
    'MUSI D041W01Y': ('MUSI', '41W', '01Y', {'Y'}),
    'NURS D092L02F': ('NURS', '92L', '02F', {'F'}),
    'NURS D092P01Z': ('NURS', '92P', '01Z', {'Z'}),
    'NURS D093L55F': ('NURS', '93L', '55F', {'F'}),
    'NURS D93AL02F': ('NURS', '93AL', '02F', {'F'}),
    'NURS D93PL01Y': ('NURS', '93PL', '01Y', {'Y'}),
    'NUTR D062G02Z': ('NUTR', '62G', '02Z', {'Z'}),
    'P E D032F02Z': ('PE', '32F', '02Z', {'Z'}),
    'P E D32HX01Z': ('PE', '32HX', '01Z', {'Z'}),
    'P E D32IX01Z': ('PE', '32IX', '01Z', {'Z'}),
    'P E D032J01Z': ('PE', '32J', '01Z', {'Z'}),
    'P E D032K01Z': ('PE', '32K', '01Z', {'Z'}),
    'P E D032L50Z': ('PE', '32L', '50Z', {'Z'}),
    'P E D032M01Z': ('PE', '32M', '01Z', {'Z'}),
    'P E D032N01Z': ('PE', '32N', '01Z', {'Z'}),
    'P E D032P01Z': ('PE', '32P', '01Z', {'Z'}),
    'P E D032S01Z': ('PE', '32S', '01Z', {'Z'}),
    'P E D04XX04Z': ('PE', '4XX', '04Z', {'Z'}),
    'PEA D001X61Z': ('PEA', '1X', '61Z', {'Z'}),
    'PEA D006Y01Z': ('PEA', '6Y', '01Z', {'Z'}),
    'PHYS D077.65R': ('PHYS', '77', '65R', {'R'}),
    'POLI D001.4EZ': ('POLI', '1', '4EZ', {'E', 'Z'}),
    'PSYC D010G50Z': ('PSYC', '10G', '50Z', {'Z'}),
    'PSYC D010H50Z': ('PSYC', '10H', '50Z', {'Z'}),
    'SOC D001.2EZ': ('SOC', '1', '2EZ', {'E', 'Z'}),
    'SOC D001.FY2': ('SOC', '1', 'FY2', {'Y', 'F'}),
    'SOSC D083X62Z': ('SOSC', '83X', '62Z', {'Z'}),
    'SPAN D001.1KZ': ('SPAN', '1', '1KZ', {'K', 'Z'}),

    # Foothill
    'ACTG F051A01W': ('ACTG', '51A', '01W', {'W'}),
    'ACTG F052.01W': ('ACTG', '52', '01W', {'W'}),
    'ACTG F070R01' : ('ACTG', '70R', '01', set()),
    'AHS F051.01Y':  ('AHS', '51', '01Y', {'Y'}),
    'ALCB F400A01V': ('ALCB', '400A', '01V', {'V'}),
    'ALCB F407Y02V': ('ALCB', '407Y', '02V', {'V'}),
    'ALCB F408Y10V': ('ALCB', '408Y', '10V', {'V'}),
    'ALCB F413Y01V': ('ALCB', '413Y', '01V', {'V'}),
    'ALCB F413Y11V': ('ALCB', '413Y', '11V', {'V'}),
    'ANTH F001H1HW': ('ANTH', '1H', '1HW', {'H', 'W'}),
    'ANTH F001L01W': ('ANTH', '1L', '01W', {'W'}),
    'ART F002J01W': ('ART', '2J', '01W', {'W'}),
    'ASTR F010L02V': ('ASTR', '10L', '02V', {'V'}),
    'ATHL F004E01V': ('ATHL', '4E', '01V', {'V'}),
    'ATHL F021F01W': ('ATHL', '21F', '01W', {'W'}),
    'BIOL F009L01V': ('BIOL', '9L', '01V', {'V'}),
    'BUSI F022H1HW': ('BUSI', '22H', '1HW', {'H', 'W'}),
    'BUSI F059.2DW': ('BUSI', '59', '2DW', {'W', 'D'}),
    'BUSI F095.01W': ('BUSI', '95', '01W', {'W'}),
    'CHEM F12AL01Z': ('CHEM', '12AL', '01Z', {'Z'}),
    'CHLD F001.01W': ('CHLD', '1', '01W', {'W'}),
    'CHLD F001.5DW': ('CHLD', '1', '5DW', {'W', 'D'}),
    'CHLD F056N01W': ('CHLD', '56N', '01W', {'W'}),
    'CHLD F089.2DW': ('CHLD', '89', '2DW', {'W', 'D'}),
    'CHLD F53NC01Z': ('CHLD', '53NC', '01Z', {'Z'}),
    'CNSL F001.1PZ': ('CNSL', '1', '1PZ', {'P', 'Z'}),
    'CNSL F008H1HV': ('CNSL', '8H', '1HV', {'H', 'V'}),
    'CNSL F056.1UV': ('CNSL', '56', '1UV', {'U', 'V'}),
    'CNSL F275.01W': ('CNSL', '275', '01W', {'W'}),
    'COMM F01AH1HW': ('COMM', '1AH', '1HW', {'H', 'W'}),
    'CRLP F007.30W': ('CRLP', '7', '30W', {'W'}),
    'D H F200L52Y': ('DH', '200L', '52Y', {'Y'}),
    'D H F300A01Y': ('DH', '300A', '01Y', {'Y'}),
    'D H F302.01': ('DH', '302', '01', set()),
    'D H F305A01': ('DH', '305A', '01', set()),
    'ECON F001B9DV': ('ECON', '1B', '9DV', {'D', 'V'}),
    'ECON F009H1HW': ('ECON', '9H', '1HW', {'H', 'W'}),
    'ENGL F001A1UW': ('ENGL', '1A', '1UW', {'W', 'U'}),
    'ENGL F001A2PW': ('ENGL', '1A', '2PW', {'W', 'P'}),
    'ENGL F001A4CW': ('ENGL', '1A', '4CW', {'W', 'C'}),
    'ENGL F001A61D': ('ENGL', '1A', '61D', {'D'}),
    'ENGL F001S1CW': ('ENGL', '1S', '1CW', {'W', 'C'}),
    'ENGL F01AH1HW': ('ENGL', '1AH', '1HW', {'H', 'W'}),
    'ENGL F01BH1HW': ('ENGL', '1BH', '1HW', {'H', 'W'}),
    'ENGL F43AH1HW': ('ENGL', '43AH', '1HW', {'H', 'W'}),
    'ENGR F037L01V': ('ENGR', '37L', '01V', {'V'}),
    'ESLL F201A7CV': ('ESLL', '201A', '7CV', {'C', 'V'}),
    'ESLL F226.1QZ': ('ESLL', '226', '1QZ', {'Z', 'Q'}),
    'GID F033.4DW': ('GID', '33', '4DW', {'W', 'D'}),
    'HIST F017B2DW': ('HIST', '17B', '2DW', {'W', 'D'}),
    'HLTH F021.8DW': ('HLTH', '21', '8DW', {'W', 'D'}),
    'HORT F054J01V': ('HORT', '54J', '01V', {'V'}),
    'HUMN F001H1HZ': ('HUMN', '1H', '1HZ', {'H', 'Z'}),
    'JAPN F013A1QZ': ('JAPN', '13A', '1QZ', {'Z', 'Q'}),
    'LINC F060K01Z': ('LINC', '60K', '01Z', {'Z'}),
    'LINC F081.01D': ('LINC', '81', '01D', {'D'}),
    'MATH F001C9DV': ('MATH', '1C', '9DV', {'D', 'V'}),
    'MATH F048A3CZ': ('MATH', '48A', '3CZ', {'Z', 'C'}),
    'MATH F048AMVP': ('MATH', '48A', 'MVP', {'P', 'M', 'V'}),
    'MATH F048AVMP': ('MATH', '48A', 'VMP', {'P', 'M', 'V'}),
    'MATH F248A3CV': ('MATH', '248A', '3CV', {'C', 'V'}),
    'MDIA F011H1HZ': ('MDIA', '11H', '1HZ', {'H', 'Z'}),
    'MUS F008H1HZ': ('MUS', '8H', '1HZ', {'H', 'Z'}),
    'MUS F02AH1HZ': ('MUS', '2AH', '1HZ', {'H', 'Z'}),
    'NCBS F405.MPV': ('NCBS', '405', 'MPV', {'P', 'M', 'V'}),
    'NCBS F405.MVP': ('NCBS', '405', 'MVP', {'P', 'M', 'V'}),
    'NCBS F405.VMP': ('NCBS', '405', 'VMP', {'P', 'M', 'V'}),
    'NCEL F426.1QZ': ('NCEL', '426', '1QZ', {'Z', 'Q'}),
    'NCEN F401A1UV': ('NCEN', '401A', '1UV', {'U', 'V'}),
    'NCEN F401A2PV': ('NCEN', '401A', '2PV', {'P', 'V'}),
    'NCEN F401A4CV': ('NCEN', '401A', '4CV', {'C', 'V'}),
    'PHOT F008.2UW': ('PHOT', '8', '2UW', {'W', 'U'}),
    'PHOT F008H1HW': ('PHOT', '8H', '1HW', {'H', 'W'}),
    'PHOT F008HHUW': ('PHOT', '8H', 'HUW', {'H', 'W', 'U'}),
    'PHYS F02AM01W': ('PHYS', '2AM', '01W', {'W'}),
    'POLI F002H1HV': ('POLI', '2H', '1HV', {'H', 'V'}),
    'PSYC F030.2DW': ('PSYC', '30', '2DW', {'W', 'D'}),
    'R T F53BL01': ('RT', '53BL', '01', set()),
    'V T F057L04Y': ('VT', '57L', '04Y', {'Y'}),
}

DEBUG = False

def show(error_info):
    if not DEBUG:
        return
    e = error_info.value
    print(e.message, '-', e.details)


class TestParseCourseString(TestCase):
    def test_parser_works_correctly(self):
        # Loop test cases data for `parse_course_str`
        for raw, expected in course_str_data.items():
            parsed = parse_course_str(raw)
            match = (parsed['dept'], parsed['course'], parsed['section'], parsed['flags'])

            self.assertEqual(
                match,
                expected,
                'Expected and parsed course string data does not match'
            )


    def test_error_on_empty_str(self):
        # Test empty string
        with raises(ValidationError) as error_info:
            parse_course_str('')
        show(error_info)


    def test_error_with_invalid_num_of_parts(self):
        # Test string with less than 2 space-separated parts
        with raises(ValidationError) as error_info:
            parse_course_str('CS ')
        show(error_info)


    def test_error_with_too_short_course_section_part(self):
        # Test string with invalid course + section string (last part)
        # Length is less than 8
        with raises(ValidationError) as error_info:
            parse_course_str('CIS D00F')
        show(error_info)


    def test_error_with_too_long_course_section_part(self):
        # Test string with invalid course + section string (last part - 'D001CXXXX')
        # Length is greater than 8
        with raises(ValidationError) as error_info:
            parse_course_str('CIS D001CXXXX')
        show(error_info)


    def test_error_with_invalid_course_part_format1(self):
        # Test string with invalid course part ('X001C' starts with invalid 'X')
        with raises(ValidationError) as error_info:
            parse_course_str('CS X001C01')
        show(error_info)


    def test_error_with_invalid_course_part_format2(self):
        # Test string with invalid course part ('FXXXX' has an invalid format - no numbers)
        with raises(ValidationError) as error_info:
            parse_course_str('CS FXXXX00')
        show(error_info)

    def test_error_with_invalid_course_part_format3(self):
        # Test string with invalid course part ('F01A-' does not match fully due to trailing '-')
        with raises(ValidationError) as error_info:
            parse_course_str('CS F01A-00')
        show(error_info)


class TestGetClassType(TestCase):
    def test_fallback_case(self):
        for campus in ['fh', 'da']:
            self.assertEqual(get_class_type(campus, set()), 'standard')
            self.assertEqual(get_class_type(campus, {'A'}), 'standard')
            self.assertEqual(get_class_type(campus, {'A', 'B'}), 'standard')


    def test_correct_type_is_returned(self):
        self.assertEqual(get_class_type('fh', {'W'}), 'online')
        self.assertEqual(get_class_type('fh', {'V'}), 'virtual')
        self.assertEqual(get_class_type('fh', {'Z'}), 'hybrid')

        self.assertEqual(get_class_type('da', {'Z'}), 'online')
        self.assertEqual(get_class_type('da', {'Y'}), 'hybrid')


    def test_correct_type_is_returned_with_multiple_flags(self):
        self.assertEqual(get_class_type('fh', {'W', '?'}), 'online')
        self.assertEqual(get_class_type('da', {'L', 'Y', 'A'}), 'hybrid')
