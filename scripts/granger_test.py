import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import grangercausalitytests
import warnings
import seaborn as sns
warnings.filterwarnings('ignore')

sns.set_theme(font_scale=0.8, style='white')
#read df_slope_POLITICIAN.csv
df_slope_POLITICIAN = pd.read_csv('df_slope_POLITICIAN.csv')

##############################################################################################
# Granger Causality Test - Predicting the confusion matrix for variables of the slope graphs #
##############################################################################################

def confusion_matrix_GT(n):
    maxlag = n
    test   = 'ssr_chi2test'

    def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False):    
        """Check Granger Causality of all possible combinations of the Time series.
        The rows are the response variable, columns are predictors. The values in the table 
        are the P-Values. P-Values lesser than the significance level (0.05), implies 
        the Null Hypothesis that the coefficients of the corresponding past values is 
        zero, that is, the X does not cause Y can be rejected.

        data      : pandas dataframe containing the time series variables
        variables : list containing names of the time series variables.
        """
        df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
        for c in df.columns:
            for r in df.index:
                test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
                p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
                if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
                min_p_value = np.min(p_values)
                df.loc[r, c] = min_p_value
        df.columns = [var + '_x' for var in variables]
        df.index = [var + '_y' for var in variables]
        return df
    #select all columns except the date
    grangers_causation_matrix(df_slope_POLITICIAN, variables = df_slope_POLITICIAN.columns[1:])
    #matplot the granger test
    #figsize
    plt.figure(figsize=(7, 6))

    ax = sns.heatmap(grangers_causation_matrix(df_slope_POLITICIAN, variables=df_slope_POLITICIAN.columns[1:]),
                     annot=True, cmap='BuGn', fmt='.3f', annot_kws={'size': 10})

    ax.set_xticklabels(df_slope_POLITICIAN.columns[1:], rotation=15, ha='center')
    ax.set_yticklabels(df_slope_POLITICIAN.columns[1:], rotation=15, ha='right')

    plt.tick_params(axis='both', which='major', labelsize=9, labelbottom=True, bottom=False, top=False, labeltop=False)

    plt.show()

#####################################################################################################################
# Granger Causality Test - Test if armonic_mean_normalized_Bots is granger caused by armonic_mean_Normalized_NoBots #
#####################################################################################################################
def trend_p_value_GT():

    ts_df = pd.DataFrame(columns=['armonic_mean_normalized_Bots','armonic_mean_Normalized_NoBots'], data=df_slope_POLITICIAN[['armonic_mean_normalized_Bots','armonic_mean_Normalized_NoBots']])

    #Granger test
    granger_score = grangercausalitytests(ts_df[['armonic_mean_normalized_Bots','armonic_mean_Normalized_NoBots']], maxlag=9)

    #plot the granger test
    plt.figure(figsize=(7, 6))

    #plot as x axis the lag, and as y axis the values of the granger test, compact bars
    plt.bar(x=[i for i in range(1,10)], height=[granger_score[i+1][0]['ssr_chi2test'][1] for i in range(9)], color='lightblue')

    #set the x axis labels
    plt.xticks([i for i in range(1,10)], [i for i in range(1,10)])

    #set the y axis labels
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], [0, 0.2, 0.4, 0.6, 0.8, 1])

    #set the title
    plt.title('Granger Causality Test', fontsize=14)

    #set the x axis label
    plt.xlabel('Lag', fontsize=12)

    #set the y axis label
    plt.ylabel('P-Value', fontsize=12)

    #set the grid
    plt.grid(axis='y', alpha=0.5)

    #show the plot
    plt.show()

def main():
    n = int(input("Enter the maxlag for Granger Test: "))
    confusion_matrix_GT(n)
    trend_p_value_GT()

if __name__ == '__main__':
    main()