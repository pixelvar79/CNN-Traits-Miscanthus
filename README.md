# CNN-Trait-Miscanthus

This is the coding implementation for the research project presented in the foloowing peer-review publication:

Sebastian Varela, Xuying Zheng, Joyce N. Njuguna, Erik J. Sacks, Dylan P. Allen, Jeremy Ruhter and Andrew D. B. Leakey (2022). *Deep Convolutional Neural Networks Exploit High-Spatial- and -Temporal-Resolution Aerial Imagery to Phenotype Key Traits in Miscanthus*. Remote Sensing. [![DOI](https://img.shields.io/badge/DOI-10.3390/rs14215333-blue)](https://doi.org/10.3390/rs14215333) [![PDF](https://img.shields.io/badge/PDF-Download-orange)](papers/remotesensing-14-05333.pdf)


1) check if anaconda is installed locally
```
conda --version

```
  https://docs.conda.io/projects/miniconda/en/latest/
  
  miniconda will be enough for creating venv and dependencies
  
  During the installation, you might be prompted to add Anaconda to the system PATH. If not, and if you encounter issues, you can add it manually:
  
  On Windows, you can check "Add Anaconda to my PATH environment variable" during installation.
  On Linux you may need to add the following line to your shell profile file (e.g., .bashrc or .zshrc):

Build local Conda virtual environment and dependencies
```
  conda create --name miscatraits python=3.9  

  conda activate miscatraits
  
  pip install -r requirements.txt
```
  
  tifffile==2023.2.28
  scikit-image==0.20.0
  numpy==1.24.2
  scikit-learn==1.0.1
  tensorflow==2.10.0
  pandas==1.5.3
  seaborn
  rasterio==1.3.6
  rasterstats==0.18.0

2) Execute whole analysis including, loading, slicing, model training and evaluation, plotting, metrics, Grad-Cam
```
  python main.py 
```
 script structure include main.py which executes: load_all_datasets(), generate_sliced_data(), train_and_evaluate_model()

A brief description of the steps in the implementation: 
          1) load_all_datasets() - load the image chips and corresponding ground-truth data available. Image chips varied in width and length size depending of the trial, temporal dimension is 102 for the whole dataset which includes up to 17 time-points between May-Novemeber. Each time point in the image chip includes 6-bands (1 CSM + 5 MSI bands).
          2) generate_sliced_data() -  takes two dictionaries and slices into RGB, RGBRENIR, CSMRGBRENIR type of features and the specific time-points for each of the target traits (Flowering time, culm length, biomass).
          3) train_and_evaluate_model() - takes previous sliced data by type of features and time range and train and evaluate 2d and 3d CNN modeling, this includes saving of figures, metrics and scatterplots generation.
          4) Grad-CAM generation() -  this takes examples images and ask grad-cam prediction of last layers of CNN to genearate heatmaps of most relevant regions used by the model for prediction. Refer to Grad-CAM technique here: https://arxiv.org/abs/1610.02391  
          
