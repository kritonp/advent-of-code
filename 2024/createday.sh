#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

DIR_NAME=$1

if [ ! -d "$DIR_NAME" ]; then
    mkdir "$DIR_NAME"
else
    echo "Directory '$DIR_NAME' already exists."
fi

FILES=("main.py" "test.txt" "input.txt")

for FILE in "${FILES[@]}"; do
    FILE_PATH="$DIR_NAME/$FILE"
    touch "$FILE_PATH"

done