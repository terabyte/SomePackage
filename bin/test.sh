#!/bin/bash

rm -rf .ve
python2.7 -m virtualenv --python=python2.7 .ve
source .ve/bin/activate

pip install -r requirements.txt

pylint somepackage
LINT_RESULT=$?

python2.7 -m somepackage.tests.__main__
TEST_RESULT=$?


echo "LINT RESULT: $LINT_RESULT"
echo "TEST RESULT: $TEST_RESULT"
if [[ $LINT_RESULT != "0" ]]; then
    exit $LINT_RESULT
fi
exit $TEST_RESULT



