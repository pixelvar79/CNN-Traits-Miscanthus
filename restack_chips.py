# import os
# import rasterio
# import numpy as np

# # Define input and output directories
# input_dir1 = r'D:/OneDrive - University of Illinois - Urbana/TF/Data/MSI2019_RGB_SEASON/IMAGES_ALL'
# input_dir2 = r'D:/OneDrive - University of Illinois - Urbana/TF/Data/MSI2019_RGB_SEASON/IMAGES_ALL1'
# output_dir = r'D:/OneDrive - University of Illinois - Urbana/TF/Data/MSI2019_RGB_SEASON/IMAGES_MSI_ALL'

# import os
# import rasterio
# import numpy as np
# import cv2


# os.makedirs(output_dir, exist_ok=True)

# def list_tiff_files(directory):
#     return [f for f in os.listdir(directory) if f.endswith('.tif')]

# # List TIFF files in both directories
# files1 = list_tiff_files(input_dir1)
# files2 = list_tiff_files(input_dir2)

# # Create a dictionary to group files by their names
# file_groups = {}
# for file in files1:
#     file_groups[file] = [os.path.join(input_dir1, file)]

# for file in files2:
#     if file in file_groups:
#         file_groups[file].append(os.path.join(input_dir2, file))
#     else:
#         file_groups[file] = [os.path.join(input_dir2, file)]

# # Function to resize image using OpenCV
# def resize_image(image, new_height, new_width):
#     resized_image = np.empty((image.shape[0], new_height, new_width), dtype=image.dtype)
#     for i in range(image.shape[0]):
#         resized_image[i] = cv2.resize(image[i], (new_width, new_height), interpolation=cv2.INTER_LINEAR)
#     return resized_image

# # Stack and save images
# for file_name, file_paths in file_groups.items():
#     if len(file_paths) == 2:  # Ensure there are two files to stack
#         file1, file2 = file_paths
#         print(file1)
#         print(file2)
        
#         with rasterio.open(file1) as src1, rasterio.open(file2) as src2:
#             # Read the images
#             img1 = src1.read()
#             img2 = src2.read()
            
#             # Resize images to 108x107
#             img1_resized = resize_image(img1, 64, 64)
#             img2_resized = resize_image(img2, 64, 64)
            
#             # Stack the images
#             stacked_img = np.concatenate((img1_resized, img2_resized), axis=0)
            
#             # Define the output file path
#             output_file = os.path.join(output_dir, file_name)
            
#             # Save the stacked image
#             with rasterio.open(
#                 output_file,
#                 'w',
#                 driver='GTiff',
#                 height=stacked_img.shape[1],
#                 width=stacked_img.shape[2],
#                 count=stacked_img.shape[0],
#                 dtype=stacked_img.dtype,
#                 crs=src1.crs,
#                 transform=src1.transform,
#             ) as dst:
#                 dst.write(stacked_img)


import os
import rasterio
import numpy as np
import cv2

# Define input and output directories
input_dir = '../data/IMAGERY/MSI/IMAGES_ALL'
output_dir = '../data/IMAGERY/MSI_MODIFIED'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def list_tiff_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.tif')]

# List TIFF files in the input directory
tiff_files = list_tiff_files(input_dir)

# Slices to discard
#discard_slices = [slice(31, 37), slice(43, 49), slice(79, 85)]
discard_slices = [slice(25, 31)]

# Function to resize image using OpenCV
def resize_image(image, new_height, new_width):
    resized_image = np.empty((image.shape[0], new_height, new_width), dtype=image.dtype)
    for i in range(image.shape[0]):
        resized_image[i] = cv2.resize(image[i], (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return resized_image

# Function to discard specified slices from the depth dimension
def discard_slices_from_image(image, discard_slices):
    mask = np.ones(image.shape[0], dtype=bool)
    for s in discard_slices:
        mask[s] = False
    return image[mask]

# Process each TIFF file
for tiff_file in tiff_files:
    input_path = os.path.join(input_dir, tiff_file)
    output_path = os.path.join(output_dir, tiff_file)
    
    with rasterio.open(input_path) as src:
        # Read the image
        image = src.read()
        
        # Resize the image to 108x107
        resized_image = resize_image(image, 108, 107)
        
        # Discard the specified slices
        modified_image = discard_slices_from_image(resized_image, discard_slices)
        
        # Save the modified image
        with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=modified_image.shape[1],
            width=modified_image.shape[2],
            count=modified_image.shape[0],
            dtype=modified_image.dtype,
            crs=src.crs,
            transform=src.transform,
        ) as dst:
            dst.write(modified_image)