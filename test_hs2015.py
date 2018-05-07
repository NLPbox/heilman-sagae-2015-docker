#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import sh
import sys


EXPECTED_OUTPUT = """{"scored_rst_trees": [{"tree": "(ROOT (satellite:contrast (text 0)) (nucleus:span (text 1)))", "score": -0.9662282971887425}], "edu_tokens": [["Although", "they", "did", "n't", "like", "it", ","], ["they", "accepted", "the", "offer", "."]]}
"""

def test_hs2015():
    """The Heilman and Sagae 2015 parser produces the expected output."""
    parser = sh.Command('./hs2015.sh')
    result = parser('input_short.txt')
    return result.stdout == EXPECTED_OUTPUT, result.stderr.encode('utf-8')

if __name__ == '__main__':
    passed, err = test_hs2015()
    if not passed:
        sys.stderr.write("test_hs2015(): '{}' does not match expected output.\n".format(err))
        sys.exit(1)

