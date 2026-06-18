(study-pams-conversion)=

# Conversion

Load the following modules:

> ```bash
> module use ${root_dir}/server/modulefiles
> module load bashHelperKennedyRodrigue
> module load containers/r/4.2.1-quarto
> module load study-pams/convert_mri/latest
> ```

For more details or updates, check the [github page.](https://github.com/epongpipat/convert-mri_study-pams)

(data-entry)=

## Data Entry

1. Enter BP measurements to the Cognitive Data Sheet, and file subject's receipts into the receipt bin.

   ```bash
   ${root_dir}/study-pams/Demographic_and_Task_Data/Cognitive_Data_MCI.xlsx
   ```

2. Copy physiological measures to the server and rename the files using the following template:

   ```bash
   ${root_dir}/study-pams/sourcedata/physio/KENROD_PAMS_20230101_0001_1/sub-0001_ses-01.puls
   ${root_dir}/study-pams/sourcedata/physio/KENROD_PAMS_20230101_0001_1/sub-0001_ses-01.resp
   ```

3. Copy the exam card to the server using the following template:

   ```bash
   ${root_dir}/study-pams/sourcedata/exam_cards/KENROD_PAMS_20230101_0001_1.pdf
   ```

(study-pams-convert)=

## Convert

1. After receiving the {{BHIC}} Data Transfer email, run the following script to unzip data:

   ```bash
   dcm_unzip.sh --data_ref abcdefgh-12345678 --sub 0001 --ses 1 --date 20230101
   ```

2. After the files have been unzipped, convert the DICOM images to NIFTI with the following script:

   ```bash
   dcm2niix_wrapper.sh --sub 0001 --ses 1 --date 20230101
   ```

(qc-parameters)=

## QC Parameters

1. QC the data and check for any images that have bad quality or were cut off.

   - Create a `scanner_reconstruction` directory for the reconstructed files (acq. 11,13,15,18,19 for ref.).
   - Create a `bad` directory within the subject directory for bad scans if necessary.

2. After QC, run the QC uber script:

   ```bash
   qc_uber.sh --sub 0001 --ses 1 --date 20230101
   ```

3. Combine the QC logs together with the following script:

   ```bash
   qc_combine_all_sub.sh
   ```

4. Then run the following script locally (via RStudio)

   ```bash
   qc_render.sh --study pams --overwrite 1
   ```
