import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import pathlib as pl


# find the files that have "psykometri" in their name
def get_files():
    cwd = pl.Path.cwd()
    file_path_list = []
    for file in cwd.glob('**/*psykometri*'):
        file_path_list.append(file)
    return file_path_list

def read_excel_data(file_path):
    if file_path.is_file():
        return pd.read_excel(file_path)

def combine_data(file_path_list=get_files()):
    df_list = []
    for file_path in file_path_list:
        df_list.append(read_excel_data(file_path))
    return pd.concat(df_list)

def fix_data(df):

    # we want to remove rows with NaN in any of the columns
    df = df.dropna()

    # we want to reduce every value in the table by 1, except the date
    df.iloc[:,1:] = df.iloc[:,1:].apply(lambda x: x-1)
    df['Date'] = df['Date'].apply(lambda x: re.sub(r'\d\d:\d\d:\d\d', '', str(x)))

    return df

#%%: Vector functions to calculate Pm score

def normalise_vector(vector):
    return vector/np.linalg.norm(vector)

def Pm_score(vector):
    ideal_vector = np.array([4,4,4,0,0,0])
    weights = np.array([1.5,1,1,1,1,1.5])
    vector = vector*weights; ideal_vector = ideal_vector*weights
    # find the perfect score for the vector
    perfect_score = np.dot(ideal_vector, ideal_vector)
    # change the sign on the last the values in the vector
    vector[-3:] = -vector[-3:]  
    return 100*np.dot(vector, ideal_vector)/perfect_score

#%% Combine the functions to calculate Pm score for all rows in the dataframe

def calculate_Pm_score(df):
    # create a new column with the Pm score
    # ignore the first "date" column
    df['Pm_score'] = df.iloc[:,1:].apply(Pm_score, axis=1)
    return df

def calculate_statistic_vector(df):
    pass

def calculate_Pm_score_distribution(df):
    # we want to calculate the distribution of the Pm score
    # to get a new dataframe of just dates and pm scores

    statistics = {"mean": df["Pm_score"].mean(),
                  "std": df["Pm_score"].std()}
    
    df["Deviation"] = df["Pm_score"].apply(lambda x: x-statistics["mean"])
    # we want to find the standard deviation for the data
    
    return df, statistics



# %% visualise the data

def plot_Pm_score(df):
    # group the data by date
    # drop the hour from the date
    df = df.groupby('Date').mean()
    plt.plot(df['Pm_score'])
    plt.xlabel('Date')
    plt.ylabel('Pm score')
    plt.grid()
    plt.title('Pm score over time')
    plt.show()



def main():
    F = combine_data()
    F = fix_data(F)
    F = calculate_Pm_score(F)
    plot_Pm_score(F)
    print(calculate_Pm_score_distribution(F))
main()
