import pandas as pd
import numpy as np
from pathlib import Path
from image_processing import load_image

def load_dataset(img_dir, gt_dir, filter_column, target_column, encoding='latin1'):
    csv_file = Path(gt_dir) / 'MSAMSI_GT.csv'
    df = pd.read_csv(csv_file, encoding=encoding)
    
    df = df.head(200)
    df = df[df[filter_column] == 'yes']
    y = df[target_column]
    plotid = df['plot_id']
    
    img_files = [Path(img_dir) / f'plot_{plot_id}.tif' for plot_id in df['plot_id']]
    img_list = [load_image(file) for file in img_files if file.exists()]
    
    if not img_list:
        raise ValueError("No images were loaded. Please check the image loading function.")
    
    x = np.stack(img_list)
    
    min_value = x.min()
    max_value = x.max()
    x = (x - min_value) / (max_value - min_value)
    
    return plotid, x, y

def load_all_datasets(img_dir, gt_dir, dataset_configs):
    datasets = {}
    for config in dataset_configs:
        filter_column = config['filter_column']
        target_column = config['target_column']
        plotid, x, y = load_dataset(img_dir, gt_dir, filter_column, target_column)
        datasets[target_column] = {
            'plotid': plotid,
            'x': x,
            'y': y
        }
    return datasets
