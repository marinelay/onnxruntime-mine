#!/bin/bash
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

export CC=/usr/bin/clang
export CXX=/usr/bin/clang++

# Get directory this script is in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OS=$(uname -s)

if [ "$OS" = "Darwin" ]; then
    DIR_OS="MacOS"
else
    DIR_OS="Linux"
fi

if [[ "$*" == *"--ios"* ]]; then
    DIR_OS="iOS"
elif [[ "$*" == *"--android"* ]]; then
    DIR_OS="Android"
fi

python3 $DIR/tools/ci_build/build.py --build_dir $DIR/build/$DIR_OS "$@"
