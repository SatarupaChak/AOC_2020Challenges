# !/usr/bin/env python3

# parse input
with open('rulematcher.txt', 'r') as f:
    input_lines = f.read().splitlines()

split = input_lines.index('')
rule_strings = input_lines[:split]
strings = input_lines[split + 1:]

# Convert rules to a dict. keys are rule numbers, values are either:
# - a list of lists of rule numbers. The inner lists are the options (separated by '|' in the original), each is a list of rule numbers to match consecutively.
# or
# - a string, to be matched exactly.

# e.g. if you have these rules:
# 0: 1 | 1 2
# 1: "a"
# 2: "b"
# you would get this dict:
# {0: [[1], [1, 2]], 1: "a", 2: "b"}

rules = {}
for rule_string in rule_strings:
    rule_string = rule_string.split(': ')
    n = int(rule_string[0])
    rule_string = rule_string[1]
    if rule_string.startswith('"'):
        rules[n] = rule_string.strip('"')
    else:
        rules[n] = [[int(rule_string.strip()) for rule_string in rule_string.strip().split(' ')] for rule_string in
                    rule_string.split('|')]


# Parser creators. Each returns a function which takes a string and returns a set of "matches".
# A "match" is the rest of the string after a successful match of the rule.
# A rule may match the same input in multiple ways resulting in different length matches; in this case it will return a set with more than one element.
# If the parser does not match the input at all, it returns the empty set.

# For example, this parser matches either "a" or "ab" at the start of its input:
# parser = alt(literal("a"), concat(literal("a"), literal("b")))
# parser("abab")
# > {"bab", "ab"}
# parser("baba")
# > {}

def literal(string):
    def match(input):
        if input.startswith(string):
            return {input[len(string):]}
        else:
            return set()

    return match


def concat(lhs, rhs):
    def match(input):
        all_matches = set()
        lhs_matches = lhs(input)
        for rest in lhs_matches:
            all_matches.update(rhs(rest))
        return all_matches

    return match


def alt(lhs, rhs):
    def match(input):
        return lhs(input) | rhs(input)

    return match


# For part 1 we can just directly translate each rule into a parser.
def get_parser_p1(n):
    rule = rules[n]
    if isinstance(rule, str):
        return literal(rule)
    elif isinstance(rule, list):
        def make_concat(parts):
            parser = get_parser_p1(parts[0])
            for part in parts[1:]:
                parser = concat(parser, get_parser_p1(part))
            return parser

        parser = make_concat(rule[0])
        for alt_rule in rule[1:]:
            parser = alt(parser, make_concat(alt_rule))

        return parser
    else:
        raise Exception(f'bad rule {n}: {rule}')


# We want to know how many of the inputs can be matched by rule 0 _in their entirety_
# that means that the set of matches should include the empty string, indicating that the whole input matched.
# so, count the number of lines for which the match for rule 0 includes the empty string
parser = get_parser_p1(0)
match_count = 0
for s in input_lines:
    matches = parser(s)
    if '' in matches:
        match_count += 1

print('p1', match_count)

# Part 2
# In part 2 we replace rule 8 with '42 | 42 8' and 11 with '42 31 | 42 11 31'
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

from collections import defaultdict


# Since rules can be recursive, we can't naively translate the rules with a recursive function anymore.
# Instead we memoize the function, putting each new parser rule into a parser table.
def parser_memoize(f):
    parser_table = {}

    def get_parser(n):
        # If we've already translated this rule then return its parser
        if n in parser_table:
            return parser_table[n]

        # Before translating a recursive rule, we need to make sure something's in the parser table so we don't recurse infinitely
        # We put a lambda here which performs a deferred lookup in the parser table, so that a recurisve parser will be able to reference itself
        parser_table[n] = lambda string: parser_table[n](string)
        parser = f(n)
        parser_table[n] = parser

        parser_memotable = {}
        parser_depthtable = defaultdict(lambda: 0)

        # Because parse rules can be recursive, we also need to make sure we don't recurse infinitely when parsing.
        # To do this we use the algorithm from "Parser combinators for ambiguous left-recursive grammars" (Frost, Hafiz, Callaghan 2007)
        # https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.89.2132
        # Basically:
        # - memoize each parser
        # - track how many times the parser has been called on each given input (i.e. the recursion depth for that input)
        # - if that recursion depth depth exceeds the length of the corresponding input plus 1, we will never match and should just return the empty set.
        def parser_wrapper(string):
            if string in parser_memotable:
                return parser_memotable[string]
            if parser_depthtable[string] > len(string) + 1:
                return {}
            parser_depthtable[string] += 1
            parser_memotable[string] = parser(string)
            return parser_memotable[string]

        return parser_wrapper

    return get_parser


# Now redefine our get_parser function using the memoization wrapper
@parser_memoize
def get_parser_part2(n):
    rule = rules[n]
    if isinstance(rule, str):
        return literal(rule)
    elif isinstance(rule, list):
        def make_concat(parts):
            parser = get_parser_part2(parts[0])
            for part in parts[1:]:
                parser = concat(parser, get_parser_part2(part))
            return parser

        parser = make_concat(rule[0])
        for alt_rule in rule[1:]:
            parser = alt(parser, make_concat(alt_rule))

        return parser
    else:
        raise Exception(f'bad rule {n}: {rule}')


parser = get_parser_part2(0)

# count the matches in the same way as part 1
match_count = 0
for s in input_lines:
    matches = parser(s)
    if '' in matches:
        match_count += 1

print('p2', match_count)