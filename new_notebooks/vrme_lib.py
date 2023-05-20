import ast
import pandas as pd


def print_results(name, atc, ci_lower_bound, ci_upper_bound):
    print(f'{name} ATC: {atc:.4}')
    print(f'{name} CI lower bound: {ci_lower_bound:.4}')
    print(f'{name} CI upper bound: {ci_upper_bound:.4}')
    print(f'{name} CI range: {abs(ci_lower_bound) -abs(ci_upper_bound):.4}')
    
    
def get_numpy (row):
    return ast.literal_eval(row.embedding)


def load_data():
    embedding_path = '../data/raw/df_embeddings.csv'
    submission_path = '../data/raw/df_submission_rating.csv'

    df_embeddings = pd.read_csv(embedding_path).T
    df_embeddings.columns=df_embeddings.iloc[0]
    df_embeddings = df_embeddings.iloc[1: , :]

    df_embeddings['embedding'] = df_embeddings.apply(lambda x: get_numpy(x), axis =1)

    df_submissions = pd.read_csv(submission_path)
    df_submission_labels = df_submissions[['id','title','conf_year','keywords','AVG_rating']]

    df_embeddings_2017 = df_embeddings.merge(df_submission_labels[df_submission_labels['conf_year']==2017], left_on='paper_id',right_on='id')
    df_embeddings_2018 = df_embeddings.merge(df_submission_labels[df_submission_labels['conf_year']==2018], left_on='paper_id',right_on='id')
    assert df_submission_labels[df_submission_labels['conf_year']==2017].shape[0] == df_embeddings_2017.shape[0]
    
    
    return df_embeddings, df_submissions, df_submission_labels, df_embeddings_2017, df_embeddings_2018


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

# ==== Agreement utils ===========================================================================
def print_ttest(other_method_name, ttest):
    print(f'T-Test: {other_method_name} vs VRM-E')
    print(f'statistic: {ttest.statistic:.4}')
    print(f'p-value: {ttest.pvalue}')
    print()