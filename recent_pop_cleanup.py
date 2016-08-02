import glob
import pandas as pd

globule = glob.glob('/Users/IXChris/Desktop/G/cityscapes/data/biggestuscities/cities/*.csv')
def recent_pop_merger(globule):
    frame_names = [thing.split('/')[-1].split('.')[0].split('_')[0] for thing in globule]

    df_list =[]
    columns =['drop_me', 2015, 2014, 2013, 2012, 2011]
    for index, path in enumerate(globule):
        temp_df = pd.read_csv(path)
        temp_df.index.name =('city')
        temp_df['city']= frame_names[index]
        temp_df.set_index('city', inplace=True)
        temp_df = temp_df[1:]
        temp_df.columns = columns
        temp_df.drop('drop_me', axis=1, inplace=True)
        df_list.append(temp_df)

    new = pd.concat(df_list)
    new.reset_index(inplace=True)
    new['city'].iloc[70] = 'san_francisco'
    new['city'].iloc[69] = 'san_diego'
    new['city'].iloc[8] = 'baton_rouge'
    new['city'].iloc[17] = 'chula_vista'
    new['city'].iloc[25] = 'fort_worth'
    new['city'].iloc[41] = 'las_vegas'
    new['city'].iloc[44] = 'los_angeles'
    new['city'].iloc[54] = 'new_york'
    new['city'].iloc[53] = 'new_orleans'
    new['city'].iloc[71] = 'santa_ana'

    new.update(new[new.columns[1:]][new[2015] < 10000] * 1000)
    return new

if __name__ == '__main__':
    globule = glob.glob('/Users/IXChris/Desktop/G/cityscapes/data/biggestuscities/cities/*.csv')
    recent_pop_merger(globule)
