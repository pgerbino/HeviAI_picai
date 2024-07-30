See training-steps.md
images https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=23691656
labels https://github.com/rcuocolo/PROSTATEx_masks/

```bash
python training/whole_gland_seg_archive.py
```

Subsequently, we converted the images and annotations to the [`nnU-Net Raw Data Archive`][nnunet_raw_data_format] format using:

```bash
python training/prepare_data.py
```


export nnUNet_raw_data_base="/home/piero/Downloads/uunet"
export nnUNet_preprocessed="/home/piero/Downloads/uunet/nnUNet_preprocessed"
export nnUNet_results="/home/piero/Downloads/uunet/results"
export RESULTS_FOLDER="/home/piero/Downloads/uunet/results"
export CUDA_VISIBLE_DEVICES=1
export nnunet_use_progress_bar=1

nnUNet_plan_and_preprocess -t 2202 --verify_dataset_integrity

nnUNet_train 3d_fullres nnUNetTrainerV2_Loss_FL_and_CE_checkpoints Task2202_prostate_segmentation 0

need to copy files into teh nnunet tree

Here we can see the data and export an onnx representation
.venv/lib/python3.8/site-packages/nnunet/network_architecture/generic_UNet.py:401
