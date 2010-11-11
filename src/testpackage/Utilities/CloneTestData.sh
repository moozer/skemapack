#!/bin/sh

# copies data from the test data directory
SRCDATADIR="testdata"
DSTDATADIR="tempdata"

cd $SRCDATADIR
cp -R . ../$DSTDATADIR