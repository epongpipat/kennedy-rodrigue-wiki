.. _mri:

mri
====

T1w
----

T1w Pipeline Description

#. Freesurfer processing

   #. Freesurfer's ``recon-all``
  
   #. QC and, if necessary, add control points and run specific ``recon-all`` function

#. Post-freesurfer processing

   #. Convert T1w and segmentations from .mgz to .nii

   #. Create individual ROIs from DK Atlas (aparc+aseg), Destrieux Atlas (aparc.a2009s+aseg), and white matter parcellation (wmparc)

   #. Reorient T1w to MNI152

   #. Warp T1w from fsnative to T1w

   #. Extract brain (ANT's ``antsBrainExtraction``, FSL's ``bet``, and ``hd-bet``; combine masks with freesurfer's DK Atlas to create final brain mask)

   #. Warp T1w from native to MNI152

   #. Segment tissue (fsl's ``fast``)
