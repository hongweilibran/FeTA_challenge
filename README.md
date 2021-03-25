# FeTA Segmentation Challenge in MICCAI 2021
Example docker containers for the FeTA Segmentation Challenge. 

The example script simply do thresholding of the *anat/[SUBJECT-ID]_T2W.nii.gz* image at 100. The participants could define their logic based on this demo.

## Python example
A detailed description of the Python example is provided here: [WEBSITE-TO-BE-UPDATED]. When this container is run according to the commands below, TEAM-NAME=example:python, YOUR-COMMAND=python&nbsp;/feta_seg/example.py, and TEST-INPUT are the input folders specified here: [WEBSITE-TO-BE-UPDATED].


## Docker commands
Containers submitted to the challenge will be run with the following commands:

```
CONTAINERID=`docker run -dit -v [TEST-INPUT]:/input/anat:ro -v /output feta_challenge/[TEAM-NAME]`
docker exec $CONTAINERID [YOUR-COMMAND]
docker cp $CONTAINERID:/output [RESULT-TEAM]
docker stop $CONTAINERID
docker rm -v $CONTAINERID
```
## Acknowledgement
We thank Hugo J. Kuijf's (UMC Utrecht) original Docker instruction in MICCAI WMH segmentation challenge 2017.
This repository is modified based on his codes.
