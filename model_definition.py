import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, GlobalAveragePooling2D, Dense, Conv3D, MaxPooling3D, GlobalAveragePooling3D


# Constants
LR = 0.001
DC = 0.0001

# def define_2d_model(input_shape):
#     model = Sequential()
#     model.add(Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=input_shape))
#     model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D(pool_size=(3, 3)))
#     model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
#     model.add(Dropout(0.50))
#     model.add(GlobalAveragePooling2D())
#     model.add(Dense(1, activation='linear'))
#     model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=LR, decay=DC), metrics=['mae'])
#     return model

# def define_3d_model(input_shape):
#     model = Sequential()
#     model.add(Conv3D(64, (3, 3, input_shape[2]), padding='same', activation='relu', input_shape=input_shape))
#     model.add(Conv3D(64, (3, 3, input_shape[2]), padding='same', activation='relu'))
#     model.add(MaxPooling3D(pool_size=(2, 2, 2)))
#     model.add(Conv3D(32, (3, 3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling3D(pool_size=(2, 2, 2)))
#     model.add(Dropout(0.50))
#     model.add(GlobalAveragePooling3D())
#     model.add(Dense(1, activation='linear'))
#     model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=LR, decay=DC), metrics=['mae'])
#     return model


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, GlobalAveragePooling2D, Dense
from tensorflow.keras.layers import Conv3D, MaxPooling3D, GlobalAveragePooling3D
from tensorflow.keras.optimizers import Adam

# Constants
LR = 0.001
DC = 0.0001
OPT = Adam(learning_rate=LR, decay=DC)

def define_2d_model(trait, sample_shape):
    model = Sequential()
    
    if trait == 'flowering time':
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=sample_shape))
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3)))
        model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
        model.add(Dropout(0.50))
        model.add(GlobalAveragePooling2D())
        model.add(Dense(1, activation='linear'))
    elif trait in ['culm length', 'biomass']:
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=sample_shape))
        model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
        model.add(GlobalAveragePooling2D())
        model.add(Dense(1, activation='linear'))
    
    model.summary()
    model.compile(loss='mean_squared_error', optimizer=OPT, metrics=['mae'])
    
    return model

def define_3d_model(trait, sample_shape):
    model = Sequential()
    
    if trait == 'flowering time':
        model.add(Conv3D(64, (3, 3, sample_shape[2]), padding='same', activation='relu', input_shape=sample_shape))
        model.add(Conv3D(64, (3, 3, sample_shape[2]), padding='same', activation='relu'))
        model.add(MaxPooling3D(pool_size=(2, 2, 1)))
        model.add(Conv3D(32, (3, 3, sample_shape[2]), padding='same', activation='relu'))
        model.add(MaxPooling3D(pool_size=(2, 2, sample_shape[2])))
        model.add(Dropout(0.50))
        model.add(GlobalAveragePooling3D())
        model.add(Dense(1, activation='linear'))
    elif trait in ['culm length', 'biomass']:
        model.add(Conv3D(64, (3, 3, sample_shape[2]), padding='same', activation='relu', input_shape=sample_shape))
        model.add(Conv3D(64, (3, 3, sample_shape[2]), padding='same', activation='relu'))
        model.add(MaxPooling3D(pool_size=(2, 2, 1)))
        model.add(Conv3D(32, (3, 3, sample_shape[2]), padding='same', activation='relu'))
        model.add(MaxPooling3D(pool_size=(2, 2, 1)))
        model.add(Conv3D(32, (3, 3, sample_shape[2]), padding='same', activation='relu'))
        model.add(Dropout(0.50))
        model.add(GlobalAveragePooling3D())
        model.add(Dense(1, activation='linear'))
    
    model.summary()
    model.compile(loss='mean_squared_error', optimizer=OPT, metrics=['mae'])
    
    return model