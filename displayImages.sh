#!/usr/bin/bash
ls -l ../maskSegan.py
python ../maskSegan.py
gimp input_val.png label_val.png result_val.png label_mask.png result_mask.png &
