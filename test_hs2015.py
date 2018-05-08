#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import json
import os
import sh
import sys

PARSER_PATH = '/opt/discourse-parsing'
PARSER_EXECUTABLE = 'hs2015.sh'
INPUT_FILEPATH = 'input_short.txt'
EXPECTED_OUTPUT = """{"scored_rst_trees": [{"tree": "(ROOT (satellite:contrast (text 0)) (nucleus:span (text 1)))", "score": -0.9662282971887425}], "edu_tokens": [["Although", "they", "did", "n't", "like", "it", ","], ["they", "accepted", "the", "offer", "."]]}
"""

def test_hs2015():
    """The Heilman and Sagae 2015 parser produces the expected output."""
    parser = sh.Command(os.path.join(PARSER_PATH, PARSER_EXECUTABLE))
    result = parser(INPUT_FILEPATH)
    result_str = result.stdout.decode('utf-8')

    json_expected = json.loads(EXPECTED_OUTPUT)
    json_produced = json.loads(result_str)
    return json_expected == json_produced, (result_str, result.stderr.decode('utf-8'))


if __name__ == '__main__':
    passed, (result, err) = test_hs2015()
    if not passed:
        sys.stderr.write("test_hs2015(): '{}'\ndoes not match expected output.\n{}\n".format(result, err))
        sys.exit(1)

