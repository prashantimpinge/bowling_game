import re
import sys


def total_score(input):
    """
    @type input: str
    @param input: String representing the throws of a single bowling game (split
                  into frames). Eg. '12-34-5/-0/-X-X-X-X-X-X-XX'
    @rtype: int
    @return: Total calculated score.
    """
    if not input:
        return 0
    return score(regex_parse(input))


def regex_parse(input):

    f_list = list(re.sub(r'[^\d/X]', '', input))
    
    return [10 - int(f_list[idx - 1]) if val is '/' else 10 if val is 'X' else
            int(val) for idx, val in enumerate(f_list)]


def score(throws, frame=1, total=0):

    if frame > 10 or not throws:
        return total
    elif throws[0] == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = sum(throws[1:3])
        elif len(throws) > 1:
            bonus = throws[1]
        return score(throws[1:], frame + 1, total + 10 + bonus)
    elif sum(throws[0:2]) == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = throws[2]
        return score(throws[2:], frame + 1, total + 10 + bonus)
    else:
        total += sum(throws[0:2])
        return score(throws[2:], frame + 1, total)


def run_tests():
    tests = [(300, 'X-X-X-X-X-X-X-X-X-X-XX'),
             (90, '45-54-36-27-09-63-81-18-90-72'),
             (150, '5/-5/-5/-5/-5/-5/-5/-5/-5/-5/-5'),
             (96, '45-54-36-27-09-63-81-18-90-7/-5'),
             (108, '12-34-0/-0/-X-X-00-18-72-X-0/'),
             (155, '0/-19-28-37-46-55-64-73-82-91-X'),
             (0, '00-00-00-00-00-00-00-00-00-00'),
             (0, ''),
             (15, '01-23-45'),
             (25, '01-23-45-X'),
             (270, 'X-X-X-X-X-X-X-X-X-X'),
             (290, 'X-X-X-X-X-X-X-X-X-X-X'),
             (25, '01-23-45-6/'),
             (145, '5/-5/-5/-5/-5/-5/-5/-5/-5/-5/'),
             (300, 'X-X-X-X-X-X-X-X-X-X-XX-X-X-X-X-X-X'),
             (280, 'X abc  X!X@X#X$X%X^X&X*X*()-0/')]
    for score, input in tests:
        result = "Testing: %s = %d: %s"
        try:
            assert score == total_score(input), 'FAIL'
            print result % (input, score, 'PASS')
        except AssertionError, e:
            print result % (input, score, e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for input in sys.argv[1:]:
            print "Input: %s Total: %d" % (input, total_score(input))
    else:
        run_tests()
