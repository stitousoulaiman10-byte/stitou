#!/bin/bash
# runs validation for each spec sequentially
for s in "$@"; do ../../.venv-research/bin/python -W ignore validate.py specs/$s.json /tmp/claude-0/-home-user-stitou/7146fc9a-e7d4-5b6b-82be-574729346c6d/scratchpad/val_$s.json > /tmp/claude-0/-home-user-stitou/7146fc9a-e7d4-5b6b-82be-574729346c6d/scratchpad/val_$s.log 2>>/tmp/claude-0/-home-user-stitou/7146fc9a-e7d4-5b6b-82be-574729346c6d/scratchpad/val_err.log; done
