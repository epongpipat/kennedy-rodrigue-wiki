(mri)=

# mri

## T1w

### T1w Pipeline Description

1. Freesurfer processing

   1. Freesurfer's `recon-all`
   2. QC and, if necessary, add control points and run specific `recon-all` function

2. Post-freesurfer processing

   1. Convert T1w and segmentations from .mgz to .nii
   2. Create individual ROIs from DK Atlas (aparc+aseg), Destrieux Atlas (aparc.a2009s+aseg), and white matter parcellation (wmparc)
   3. Reorient T1w to MNI152
   4. Warp T1w from fsnative to T1w
   5. Extract brain (ANT's `antsBrainExtraction`, FSL's `bet`, and `hd-bet`; combine masks with freesurfer's DK Atlas to create final brain mask)
   6. Warp T1w from native to MNI152
   7. Segment tissue (fsl's `fast`)
