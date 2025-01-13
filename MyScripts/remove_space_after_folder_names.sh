#!/bin/bash

# find all directory names that end with space:
while find "$(pwd)" -type d |grep  -q ' $'
do
    # select one and store its name in DIR variable
    DIR=$(find "$(pwd)" -type d | grep ' $'|head -1)

    # remove the last character (which is space) from that
    # name and save it to NEW_DIR variable
    NEW_DIR=${DIR%?}

    # rename the directory
    mv "$DIR" "$NEW_DIR"
done
