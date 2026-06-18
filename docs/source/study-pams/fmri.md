(fmri-pams)=

# fMRI processing

## fMRI Pipeline Description

1. Ensure processed T1w (post-freesurfer processing)
2. Ensure functional data (including local) are copied over
3. Ensure you use `module load python/3.9.1` or the latest version

To run this pipeline, please use `flex_uber` and use the `study-pams/mri/func/task-circles_bold/preprocessing/scripts.txt` pipeline.

Then, use `flex_uber` and use the `study-pams/mri/func/task-circles_bold/first-level/scripts.txt` pipeline
