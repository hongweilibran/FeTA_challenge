# -*- coding: utf-8 -*-
"""
@author: user
"""

import os
import SimpleITK as sitk

inputDir = '/input'
outputDir = '/output'

head_tail = os.path.split(inputDir) # to split the input directory and to obtain the suject name

# Load the image
T2wImage = sitk.ReadImage(os.path.join(inputDir, 'anat', head_tail+'_T2w.nii.gz'))

##
# your logic here. Below we do binary thresholding as a demo
##

# using SimpleITK to do binary thresholding between 100 - 10000
resultImage = sitk.BinaryThreshold(T2wImage, lowerThreshold=100, upperThreshold=10000)

sitk.WriteImage(resultImage, os.path.join(outputDir, 'seg_result.nii.gz'))
