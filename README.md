# Predicting Drug Perturbations from Cellular Morphology

## Overview
This project explores whether single-cell morphology can be used to predict drug treatments (`Metadata_pert_iname`) using a subset of the JUMP Cell Painting dataset [1]. We segment microscopy images, extract handcrafted features, apply dimensionality reduction, and train a Random Forest classifier to evaluate treatment-specific morphological signals.

## Abstract
High-content imaging enables large-scale analysis of cellular responses to perturbations, offering potential
for drug classification based on cell morphology. In this study, we evaluate whether single-cell morphological
features can be used to predict drug treatments using a subset of a dataset. We segmented 2,867 grayscale
microscopy images using Cellpose, generating over 450,000 individual cell masks. For each cell, we extracted 11
features, capturing size, shape, and intensity descriptors, to name a few. These features were used to train a
Random Forest classifier with and without dimensionality reduction via Principal Component Analysis (PCA).
We evaluated model performance across different input types and sampling strategies, including experiments with
and without the control treatment (DMSO). Accuracy remained low overall, with class imbalance contributing
to overprediction of DMSO despite downsampling. Feature importance analysis highlighted intensity variation
and solidity as modestly informative, and UMAP visualizations revealed weak clustering for treatments. These
findings suggest that while morphological features do reflect some treatment-specific signals, classification is
limited. Our results emphasize the challenge of phenotype-based drug prediction at the single-cell level, while
also demonstrating the capability of interpretable pipelines for large-scale morphological profiling.


---
# CellMorph.ipynb
The file is too large to view on GitHub. Please download it to follow this outline.

## 1. Image–Label Mapping

The metadata CSV includes key columns:
- `FileName_OrigRNA`: matches image filenames
- `Metadata_pert_iname`: drug name (prediction target)
- `Metadata_target`: biological target (optional grouping/interpretation)
- `Metadata_cell_line`: cell line used (e.g., A549)
- `Metadata_experiment_type`: experiment type (e.g., "Compound")
- `Metadata_pubchem_cid`: PubChem compound ID

These allow us to:
- Assign groundtruth labels to cell images
- Analyze results by drug, target, or cell line

---

## 2. Data Preprocessing

### 2.1 Implementing Cellpose Algorithm
Adapted from "Cellpose Prediction for 2D v0.5"
- Used Cellpose to download and load the images
  
### 2.2 Segmentation
- Used Cellpose to segment cells in 2867 `.tiff` images
- Saved corresponding masks

### 2.3 Concatenation
- Matched each cell’s features to the drug treatment label of its parent image

---

## 3. Feature Extraction

### 3.1 Morphological Feature Extraction
- Applied a custom feature extraction function using `skimage.measure.regionprops` to each labeled cell region
- Extracted features for each segmented cell, including:
  - Area, eccentricity, perimeter, solidity, mean intensity, orientation, etc.
#### 3.1.1 Using your own dataset?
- Extract the features and treatments from your dataset
#### 3.1.2 Loading provided dataset
- Otherwise, use the data provided here
#### 3.1.4 Cell count mask
- To reduce runtime, we look at the top 20 treatments with the most segmented cell counts

### 3.2 Dimensionality Reduction
- Applied PCA to reduce the 11-dimensional feature space to n principal components
- Helps with:
  - Noise reduction
  - Visualization (ie. UMAP)
  - Speeding up training
#### 3.2.1 Scree plot
- Find the number of principal components that explain 95% of the variance
#### 3.2.2 Elbow method
- Find the optimal number of clusters by finding the point where adding more clusters yields diminishing returns in explained variance
---

## 4. Train a Classifier

### 4.1 Random Forest
- Used for its robustness and interpretability
- Stratified by treatment 80/20 train/test split

#### 4.1.1 All features/treatments
- Ran into RAM issues both with and without PCA

#### 4.1.2 Top 20 features/treatments
- Only searched for the best number of estimators for without PCA and without DMSO
  - Best practice should serach for the best number of estimators for each experiment
- Ran experiments with with and witout PCA
- Ran experiments both with and without DMSO, the control treatment
---

## 5. Evaluate and Visualize
- Accuracy
- Confusion matrix to show common misclassifications
- Random Forest bar plots of feature importances 
- UMAP of PCA-reduced features to visualize morphological clustering
  - Silhouette score

---
## References
1. Chandrasekaran, S. N., Cimini, B. A., Goodale, A., Miller, L., Kost-Alimova, M., Jamali, N., Doench, J. G., et al. (2024). *Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations*. **Nature Methods**, 21(6), 1114–1121. https://doi.org/10.1038/s41592-024-02241-6
2. Image-based Profiling with Cell Painting. 2024. Google Colaboratory notebook. Retrieved March 27, 2025, from https://colab.research.google.com/drive/1SDwTBwiS8qQO3kG4LDqNWxAn-TcUFzJ-#scrollTo=hG3LSmJmLylT
