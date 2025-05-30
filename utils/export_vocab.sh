#!/usr/bin/bash

python ./vocabulary_exporter/main.py \
  -i ../english/$1/vocabulary.yaml \
  -o ../english/$1/slides_export.md
