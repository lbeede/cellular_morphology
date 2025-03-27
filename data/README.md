# How to download our dataset

This repository contains a lightweight Python script to download a subset of the JUMP Cell Painting dataset used for single-cell morphological analysis.

---

1. **Clone the repository**:
```bash
git clone https://github.com/lbeede/cellular_morphology
cd cellular_morphology
```
Now we are in the repository directory.

2. Run download_data.py
```
python download_data.py
```

3. Done!
You now will have all the data from our project in cellular_morphology/data/cellmorph/. The files are as follow
- lmb_downsampled_data/ : folder containing all images and masks (.tiff)
  - Masks/ : folder containing the masks (.tiff)
- segmented/ : folder containing the segementations of the images
- all_features.npy : all the features of the segmented images
- all_treatments.npy : all the treatments of the segmented images
- metadata_BR00116991.csv : the images' corresponding metadata
You can now run the corresponding notebooks!

# References
Chandrasekaran, S. N. et al. (2024). Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations. Nature Methods, 21(6), 1114–1121. https://doi.org/10.1038/s41592-024-02241-6
