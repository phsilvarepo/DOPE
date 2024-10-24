# DOPE

This package contains the necessary scripts for pre processing of the DOPE input data, generated with Isaac Sim

## rename.py
Script to rename files

Parameters:

- **directory_path**: Path to the dataset directory.

Note: Have to change the range, according to the number of images

## pose_transfomer
ROS Package to convert the detected object pose from the local camera frame to the global convention (Isaac Sim convention)
