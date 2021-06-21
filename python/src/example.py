# -*- coding: utf-8 -*-
"""
@author: user
"""

import os
import glob
import SimpleITK as sitk

inputDir = '/input'
outputDir = '/output'

T2wImagePath = glob.glob(os.path.join(inputDir, ‘anat’, ‘sub-*_T2w.nii.gz’))[0] 
sub = os.path.split(T2wImagePath)[1].split(‘_’)[0] # to split the input directory and to obtain the suject name 

# Load the image
T2wImage = sitk.ReadImage(T2wImagePath)

##
# your logic here. Below we do binary thresholding as a demo
##

# using SimpleITK to do binary thresholding between 100 - 10000
resultImage = sitk.BinaryThreshold(T2wImage, lowerThreshold=100, upperThreshold=10000)
# save the segmentation mask
sitk.WriteImage(resultImage, os.path.join(outputDir, sub + '_seg_result.nii.gz'))
