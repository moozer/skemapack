#!/bin/sh

# copies data from the test data directory
SRCDATADIR="testdata"
DSTDATADIR="tempdata"

cp -R $SRCDATADIR/* $DSTDATADIR