import ast


def print_results(name, atc, ci_lower_bound, ci_upper_bound):
    print(f'{name} ATC: {atc:.4}')
    print(f'{name} CI lower bound: {ci_lower_bound:.4}')
    print(f'{name} CI upper bound: {ci_upper_bound:.4}')
    print(f'{name} CI range: {abs(ci_lower_bound) -abs(ci_upper_bound):.4}')
    
    
    
    
    
def get_numpy (row):
    return ast.literal_eval(row.embedding)



# ==== SPSM utils ================================================================================

def mean_predictions(dummy, y_pred):
    """
    Helpful for error diagnosing. Returns the mean of the predcted values
    Args:
        - dummy : we need this arg so that this function looks the same as
        sklearn error metrics that take inputs y_true, y_pred
        - y_pred : np.array
    """
    return np.mean(y_pred)

def calibration_rmse(y_true, y_pred): 
    """
    Calculates calibration root mean squared error (RMSE). 
    Calibration is the extent to which a model's probabilistic predictions match their 
    corresponding empirical frequencies. 
    See Nguyen and O'Connor 2015's introduction and definitions 
    https://www.emnlp2015.org/proceedings/EMNLP/pdf/EMNLP182.pdf
    """
    prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=10, strategy='uniform')
    rms = mean_squared_error(prob_true, prob_pred, squared=False) #False returns RMSE vs MSE 
    return rms

def mean_truth(y_true, dummy):
    """
    Helpful for error diagnosing. Returns the mean of the true values
    Args:
        - y_true : np.array
        - dummy : we need this arg so that this function looks the same as
        sklearn error metrics that take inputs y_true, y_pred
    """
    return np.mean(y_true)

def strip_char(row):
    word_list = ast.literal_eval(row.keywords)
    s = ''
    for word in word_list:
        s += " " + word.replace(' ','_').replace('-','_').lower()
    return s
