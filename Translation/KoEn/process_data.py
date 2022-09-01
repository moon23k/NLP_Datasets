import pandas as pd


d_names = ['1_구어체(1).xlsx', '1_구어체(2).xlsx', '2_대화체.xlsx'
           '3_문어체_뉴스(1)_200226.xlsx', '3_문어체_뉴스(2).xlsx', 
           '3_문어체_뉴스(3).xlsx', '3_문어체_뉴스(4).xlsx']


def main():
    src, trg = [], []
    for d_name in d_names:
        df = pd.read_excel(f'd_name')
        src.append(df.iloc[:, -2].values.tolist())
        trg.append(df.iloc[:, -1].values.tolist())
    
    return

if __name__ == '__main__':
    main()