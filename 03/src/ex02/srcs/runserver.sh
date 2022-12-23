#!/bin/bash

cd /home/msalena/Desktop/src
redis-server &
python3 -m http.server &