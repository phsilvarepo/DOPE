# DOPE

This package contains the necessary scripts for pre processing of the DOPE input data, generated with Isaac Sim

## rename.py
Script to rename files

Parameters:

- **directory_path**: Path to the dataset directory.

Note: Have to change the range, according to the number of images

## pose_transformer
ROS Package to convert the detected object pose from the local camera frame to the global convention (Isaac Sim convention)

Subscribed topics:
- **dope/pose_dex_cube_instanceable** : PoseStamped topic with the object pose in the camera axis
  
published topics:

- **object_pose** : PoseStamped topic with the object pose in the global axis


## Docker Container 
Need to add weight to dope_container/weights folder (Too heavy gor github)

docker build -t dope_ros -f dope_ros.dockerfile .

docker run -it --rm --net=host --gpus all --privileged dope_ros

roslaunch dope dope.launch
