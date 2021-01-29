#!/bin/sh
pip install . -r tests/requirements.txt
pytest -vv .
