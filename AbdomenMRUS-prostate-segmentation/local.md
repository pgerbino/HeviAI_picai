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

Reduce all processing to bare min to analyse how the network works
alot of it is hard coded
look at just one case
amend (../../../../../Downloads/uunet/mha2nnunet_settings/Task2202_prostate_segmentation.json)
for epoch run https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/.venv/lib/python3.8/site-packages/nnunet/training/network_training/nnUNetTrainerV2.py#L48
for iterations https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/.venv/lib/python3.8/site-packages/nnunet/training/network_training/network_trainer.py#L100
for output validation https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/.venv/lib/python3.8/site-packages/nnunet/training/network_training/nnUNetTrainer.py#L604

run https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/training/whole_gland_seg_archive.py#L274 tp create mha settings
run https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/training/prepare_data.py#L85 after to create the required nnunet archive

whats going on here 
https://vscode.dev/github/pgerbino/HeviAI_picai/blob/main/AbdomenMRUS-prostate-segmentation/.venv/lib/python3.8/site-packages/nnunet/training/network_training/nnUNetTrainer.py#L516