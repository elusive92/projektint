#!/bin/bash

set -e
export ZATO_CLI_DONT_SHOW_OUTPUT=1

SOURCE="${BASH_SOURCE[0]}"
BASE_DIR="$( dirname "$SOURCE" )"
while [ -h "$SOURCE" ]
do
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$BASE_DIR/$SOURCE"
  BASE_DIR="$( cd -P "$( dirname "$SOURCE"  )" && pwd )"
done
BASE_DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

ZATO_BIN=zato
STEPS=6
CLUSTER=quickstart-123137

echo Starting the Zato cluster $CLUSTER
echo Running sanity checks

$ZATO_BIN check-config $BASE_DIR/server1
$ZATO_BIN check-config $BASE_DIR/server2

echo [1/$STEPS] Redis connection OK
echo [2/$STEPS] SQL ODB connection OK

# Start the load balancer first ..
cd $BASE_DIR/load-balancer
$ZATO_BIN start .
echo [3/$STEPS] Load-balancer started

# .. servers ..

cd $BASE_DIR/server1
$ZATO_BIN start .
echo [4/$STEPS] server1 started


cd $BASE_DIR/server2
$ZATO_BIN start .
echo [5/$STEPS] server2 started


# .. web admin comes as the last one because it may ask Django-related questions.
cd $BASE_DIR/web-admin
$ZATO_BIN start .
echo [$STEPS/$STEPS] Web admin started

cd $BASE_DIR
echo Zato cluster $CLUSTER started
echo Visit https://zato.io/support for more information and support options
exit 0
