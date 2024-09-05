# image_processing.py

from tifffile import imread
from skimage.transform import resize
import numpy as np
from slices import get_slices_for_trait  # Import the function from slices.py

def load_image(picture):
    img = imread(picture)
    img = resize(img, (80, 80, 96))    
    return img

def apply_slices(x, slices):
    all_slices = []
    slice_info = []
    for slice_list in slices.values():
        for _, info, s in slice_list:
            sliced_part = x[:, :, :, s]
            all_slices.append(sliced_part)
            slice_info.append(info)
    stacked_slices = np.stack(all_slices, axis=-1)
    return stacked_slices, slice_info

def generate_sliced_data(datasets, slices):
    print('generating sliced data...')
    all_sliced_data = {}
    all_slice_infos = {}
    
    for trait, data in datasets.items():
        x = data['x']
        trait_slices = get_slices_for_trait(trait)  # Use the function here
        sliced_data = {}
        slice_infos = {}
        
        for feature_type in ['RGB', 'RGBRENIR', 'CSMRGBRENIR']:
            if feature_type in trait_slices:
                sliced_data[f'{trait}_{feature_type}'], slice_infos[f'{trait}_{feature_type}'] = apply_slices(x, {feature_type: trait_slices[feature_type]})
        
        all_sliced_data.update(sliced_data)
        all_slice_infos.update(slice_infos)
    
    return all_sliced_data, all_slice_infos
