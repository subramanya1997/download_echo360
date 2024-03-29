#!/bin/bash

PYTHON=python
VENV_NAME=.download_echo360_venv

error_exit(){
    echo "$1" 1>&2
    exit 1
}

error_clean_exit(){
    echo Try again later! Removing the virtual environment dir...
    [ -e $VENV_NAME ] && rm -r $VENV_NAME
    error_exit "$1" 1>&2
}

cd "`dirname \"$0\"`"
if $PYTHON -c 'import sys; sys.exit(1 if sys.hexversion<0x03000000 else 0)'; then
    VENV=venv
else
    error_exit "Python 2 is not supported"
fi

# Check if virtual environment had been created
if [ ! -d "$VENV_NAME" ]; then 
    echo Checking pip is installed
    $PYTHON -m ensurepip --default-pip >/dev/null 2>&1
    $PYTHON -m pip >/dev/null 2>&1
    if [ $? -ne 0 ]; then 
        echo pip is still not installed!...
        echo Try to install it with sudo?
        echo Run: \"sudo $PYTHON -m ensurepip --default-pip\"
        exit 1
    fi
    echo Creating python virtual environment in "$VENV_NAME/"...
    $PYTHON -m $VENV $VENV_NAME || error_exit "Failed to create virtual environment"
    source $VENV_NAME/bin/activate || error_exit "Failed to source virtual environment"
    echo Upgrading pip...
    $PYTHON -m pip install --upgrade pip
    echo Installing all pip dependency inside virtual environment...
    $PYTHON -m pip install --upgrade --force-reinstall -r requirements.txt || error_clean_exit "Something went wrong while installing pip packages"
fi

source $VENV_NAME/bin/activate || error_exit "Failed to source virtual environment (try to delete '$VENV_NAME/' and re-run)"

# run the script
$PYTHON download_echo360.py "$@"