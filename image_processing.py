from tifffile import imread
from skimage.transform import resize
import numpy as np

def load_image(picture):
    img = imread(picture)
    img = resize(img, (10, 10, 102))    
    return img

def get_slices_for_trait(trait, slices):
    return slices.get(trait, {})

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
    all_sliced_data = {}
    all_slice_infos = {}
    
    for trait, data in datasets.items():
        x = data['x']
        trait_slices = get_slices_for_trait(trait, slices)
        sliced_data = {}
        slice_infos = {}
        
        for feature_type in ['RGB', 'RGBRENIR', 'CSMRGBRENIR']:
            if feature_type in trait_slices:
