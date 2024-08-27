from data_loader import load_all_datasets
from image_processing import generate_sliced_data
from train_evaluate import train_and_evaluate_model

# Configurations
img_dir = 'path_to_image_directory'
gt_dir = 'path_to_groundtruth_directory'

# Dataset configurations
dataset_configs = [
    {'filter_column': 'data_available_f50', 'target_column': 'f50_head_date'},
    {'filter_column': 'data_available_length', 'target_column': 'culm_length'},
    {'filter_column': 'data_available', 'target_column': 'biomass'}
]

slices = {
    # Define the slices here
}

def main():
    datasets = load_all_datasets(img_dir, gt_dir, dataset_configs)
    all_sliced_data, all_slice_infos = generate_sliced_data(datasets, slices)
    
    # Train and evaluate 2D model
    train_and_evaluate_model(all_sliced_data, all_slice_infos, datasets, model_type='2d')
    
    # Train and evaluate 3D model
    train_and_evaluate_model(all_sliced_data, all_slice_infos, datasets, model_type='3d')

if __name__ == "__main__":
    main()
