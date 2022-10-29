#!/usr/bin/env bash

#poetry export --without-hashes -o requirements.txt

pyinstaller run.py \
    --name smallapp \
    --onefile \
    -w \
    --clean \
    --noupx \
    -i "smallapp\assets\icons\appicons\smallapp.icns" \
    --add-data smallapp/assets:smallapp/assets
