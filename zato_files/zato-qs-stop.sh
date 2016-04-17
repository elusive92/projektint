#!/bin/bash

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


if [[ "$1" = "--delete-pidfiles" ]]
then
  echo Deleting PID files

  rm -f $BASE_DIR/load-balancer/pidfile
  rm -f $BASE_DIR/load-balancer/zato-lb-agent.pid
  rm -f $BASE_DIR/server1/pidfile
  rm -f $BASE_DIR/server2/pidfile
  rm -f $BASE_DIR/web-admin/pidfile

  echo PID files deleted
fi

ZATO_BIN=zato
STEPS=4
CLUSTER=quickstart-123137

echo Stopping the Zato cluster $CLUSTER

# Start the load balancer first ..
cd $BASE_DIR/load-balancer
$ZATO_BIN stop .
echo [1/$STEPS] Load-balancer stopped

# .. servers ..

cd $BASE_DIR/server1
$ZATO_BIN stop .
echo [2/$STEPS] server1 stopped


cd $BASE_DIR/server2
$ZATO_BIN stop .
echo [3/$STEPS] server2 stopped


cd $BASE_DIR/web-admin
$ZATO_BIN stop .
echo [$STEPS/$STEPS] Web admin stopped

cd $BASE_DIR
echo Zato cluster $CLUSTER stopped
