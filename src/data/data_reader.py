import pandas as pd


def read_AAPL(directory):
    path = directory + 'AAPL.csv'
    return _read_csv(path)


def read_games(directory):
    path = directory + 'games_dataset.csv'
    return _read_csv(path)


def read_marketing_campaign(directory):
    path = directory + 'marketing_campaign.csv'
    return _read_csv(path, sep='\t')

def read_engineer_salaries(directory):
    path = directory + 'engineer_salaries.csv'
    return _read_csv(path)

def _read_csv(path, sep=','):
    df = pd.read_csv(path, sep=sep)
    return df

if __name__ == '__main__':
    import os
    print(read_AAPL(os.getcwd() + '/../../bin/').head())
    print(read_games(os.getcwd() + '/../../bin/')[['Game Name', 'Genre', 'Platform', 'Release Year', 'User Rating']].head())
    print(read_marketing_campaign(os.getcwd() + '/../../bin/').columns)
