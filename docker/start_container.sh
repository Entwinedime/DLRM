#!/bin/bash

SCRIPT_DIR=$(realpath $(dirname $0))

cd $SCRIPT_DIR
docker run -it --rm --gpus all \
    -v $(realpath $SCRIPT_DIR/..):/dlrm \
    -w /dlrm \
    $(id -un)/oneflow-dev
cd - > /dev/null