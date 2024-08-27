import os
import matplotlib.pyplot as plt

def plot_loss(history, model_name, output_folder):
    plt.figure()
    plt.plot(history.history['loss'], label='Training loss')
    plt.plot(history.history['val_loss'], label='Validation loss')
    plt.title(f'Training and validation loss: {model_name}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Save the figure to the output folder
    output_path = os.path.join(output_folder, f'loss_{model_name}.png')
    plt.savefig(output_path)
    plt.close()  # Close the figure to free memory

    print(f"Saved loss plot: {output_path}")

def plot_predictions(y_test, y_pred, model_name, output_folder):
    plt.figure()
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title(f'Actual vs Predicted for {model_name}')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the figure to the output folder
    output_path = os.path.join(output_folder, f'predictions_{model_name}.png')
    plt.savefig(output_path)
    plt.close()  # Close the figure to free memory

    print(f"Saved predictions plot: {output_path}")

def evaluate_and_plot(model, history, x_test, y_test, model_name, model_type, output_folder):
    plot_loss(history, model_name, output_folder)
    
    y_pred = model.predict(x_test)
    plot_predictions(y_test, y_pred, model_name, output_folder)
    
    loss, mae = model.evaluate(x_test, y_test, verbose=0)
    print(f"Model {model_name} with {model_type} input - Loss: {loss}, MAE: {mae}")

