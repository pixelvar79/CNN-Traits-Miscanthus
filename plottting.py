import matplotlib.pyplot as plt

def plot_loss(history, model_name):
    plt.figure()
    plt.plot(history.history['loss'], label='Training loss')
    plt.plot(history.history['val_loss'], label='Validation loss')
    plt.title(f'Training and validation loss: {model_name}')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def plot_predictions(y_test, y_pred, model_name):
    plt.figure()
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title(f'Actual vs Predicted for {model_name}')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.show()

def evaluate_and_plot(model, history, x_test, y_test, model_name, model_type):
    plot_loss(history, model_name)
    
    y_pred = model.predict(x_test)
    plot_predictions(y_test, y_pred, model_name)
    
    loss, mae = model.evaluate(x_test, y_test, verbose=0)
    print(f"Model {model_name} with {model_type} input - Loss: {loss}, MAE: {mae}")
