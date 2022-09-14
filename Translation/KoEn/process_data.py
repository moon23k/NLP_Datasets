import json
import pandas as pd


d_names = ['1_구어체(1).xlsx', '1_구어체(2).xlsx', '2_대화체.xlsx'
           '3_문어체_뉴스(1)_200226.xlsx', '3_문어체_뉴스(2).xlsx', 
           '3_문어체_뉴스(3).xlsx', '3_문어체_뉴스(4).xlsx']


def read_data(data_name):
    df = pd.read_excel(f'd_name')
    return [{'src': src, 'trg': trg} for src, trg in zip(df.iloc[:, -2].values.tolist(), df.iloc[:, -1].values.tolist())]


def main():
    return


if __name__ == '__main__':
    main()