#!/bin/bash
/usr/local/bin/rst_parse --segmentation_model segmentation_model.C32.0 --parsing_model rst_parsing_model.C0.5 $1 > $1.hs2015
cat $1.hs2015
