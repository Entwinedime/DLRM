#!/usr/bin/env bash

SCRIPT_DIR=$(realpath $(dirname $0))

cd $SCRIPT_DIR
docker build \
    -t $(id -un)/oneflow-dev \
    .
cd - > /dev/null