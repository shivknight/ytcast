#!/bin/bash

youtube-dl -x --audio-quality 0 --audio-format "opus" --add-metadata -o 'lambdas/podcasts/%(id)s.%(ext)s' $1 
