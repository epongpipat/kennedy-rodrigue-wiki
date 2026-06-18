(pet)=

# pet

## Amyloid Pipeline Description

1. Ensure processed T1w (post-freesurfer processing)
2. Correct for motion
3. Warp PET from native space to T1w space (coregister)
4. Warp DK Atlas from T1w space to PET space
5. Create mask and obtain PET reference values
6. Calculate SUVR image
7. Create cortical ROIs
8. Extract SUVR from cortical ROIs

To run this pipeline, please use `flex_uber` and use the `study-pams/pet/scripts.txt` pipeline
