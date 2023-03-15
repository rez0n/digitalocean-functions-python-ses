#!/bin/bash

set -e

virtualenv --python python3.9 --without-pip virtualenv
pip install -r requirements.txt --target virtualenv/lib/python3.9/site-packages
