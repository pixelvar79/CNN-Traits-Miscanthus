import os
from sklearn.model_selection import train_test_split
from tensorflow.keras import callbacks
from model_definition import define_2d_model, define_3d_model
from plotting import evaluate_and_plot
import numpy as np

# Constants
EPOCHS = 20
SIZE = 32
MODE = 'min'
METRIC_VAR = 'val_loss'
PATIENCE = 40
RANDOM_STATE = 456
output_dir = '../output'
output_dir_plots = '../output/plots'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
dfs = []

def train_and_evaluate_model(all_sliced_data, slice_infos, datasets, model_type='2d'):
    if model_type == '2d':
        for key, data in datasets.items():
            y_var = data['y']
            matching_keys = [k for k in all_sliced_data.keys() if k.startswith(key)]
            
            for slice_key in matching_keys:
                value = all_sliced_data[slice_key]
                for i in range(value.shape[-1]):
                    x_var = value[..., i]
                    slice_info = slice_infos[slice_key][i]
                    
                    x_train, x_test, y_train, y_test = train_test_split(x_var, y_var, train_size=0.8, random_state=RANDOM_STATE)
                    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size=0.7)
                    
                    model = define_2d_model(x_train[0].shape)
                    model_name = f'{slice_key}_slice_{slice_info}_2d'
                    es = callbacks.EarlyStopping(monitor=METRIC_VAR, verbose=1, mode=MODE, min_delta=0.01, patience=PATIENCE)
                    mc = callbacks.ModelCheckpoint(os.path.join(output_dir, f'{model_name}.h5'), monitor=METRIC_VAR, mode=MODE, save_best_only=True, verbose=1)
                    
                    history = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=SIZE, validation_data=(x_val, y_val), verbose=2, callbacks=[mc, es])
                    print(f'Model for {slice_key} slice {slice_info} trained with target {key}.')
                    evaluate_and_plot(model, history, x_test, y_test, model_name, model_type, output_dir_plots)
                    
    elif model_type == '3d':
        for key, data in datasets.items():
            y_var = data['y']
            matching_keys = [k for k in all_sliced_data.keys() if k.startswith(key)]
            
            for slice_key in matching_keys:
                value = all_sliced_data[slice_key]
                x_var = np.reshape(value, (value.shape[0], value.shape[1], value.shape[2], -1))
                x_var = np.expand_dims(x_var, axis=-1)
                
                x_train, x_test, y_train, y_test = train_test_split(x_var, y_var, train_size=0.8, random_state=RANDOM_STATE)
                x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size=0.7)
                
                input_shape = x_train[0].shape
                
                model = define_3d_model(input_shape)
                model_name = f'{slice_key}_3d'
                es = callbacks.EarlyStopping(monitor=METRIC_VAR, verbose=1, mode=MODE, min_delta=0.01, patience=PATIENCE)
                mc = callbacks.ModelCheckpoint(os.path.join(output_dir, f'{model_name}.h5'), monitor=METRIC_VAR, mode=MODE, save_best_only=True, verbose=1)
                
                history = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=SIZE, validation_data=(x_val, y_val), verbose=2, callbacks=[mc, es])
                print(f'Model for {slice_key} trained in 3D mode with target {key}.')
                evaluate_and_plot(model, history, x_test, y_test, model_name, model_type)
