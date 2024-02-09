#!/usr/bin/bash

python -m vocabulary_exporter.main \
  -i ../english/$1/vocabulary.yaml \
  -o ../english/$1/export_slides.md
