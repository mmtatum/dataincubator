#!/usr/bin/env python

import pandas
def avg_1st_last_seconds(group):
    '''
    Calculates the average number of seconds between
    first and last page visited
    '''
    if len(group)<2:
        return None
    return (group.time.max() - group.time.min()).total_seconds()

def avg_num_visits(group, min=1):
    '''
    Calculates the number of visits per user
    given the user visits a minimum number of pages
    '''
    if min < 2:
        return len(group['category'])
    if min > 1:
        if len(group)< min:
            return None
        return len(group['category'])
    
def avg_num_categories(group, min=1):
    '''
    Calculates the number of categories per user
    given the user visits a minimum number of pages
    '''
    if min==0 or min==1:
        return len(set(group['category']))
    if min > 1:
        if len(set(group['category'])) < min:
            return None
        return len(set(group['category']))

def avg_num_category_page(group, page=1):
    if page==0 or page==1:
        return avg_num_categories(group)
    if page > 1:
        if len(group)< page:
            return None
        else:
            return avg_num_categories(group)       
    
def avg_seconds_consecutive_page(group):
    if len(group)<2:
        return None
    return (group.time[1:]\
            -group.time.shift()[1:]).mean().total_seconds()
    
def main(csvfile):

    df=pandas.read_csv(csvfile)
    df.time=df.time.apply\
    (lambda x: pandas.datetime.strptime(x,'%Y-%m-%d %H:%M:%S') )
    grouped_df=df.groupby('user')
    
    print 'Average number of seconds',\
    'between first and last page visited: %f s'\
    %(grouped_df.apply(avg_1st_last_seconds).mean())
    
    print 'Average number of seconds',\
    'between consecutive page visits by a user: %f s'\
    %(grouped_df.apply(avg_seconds_consecutive_page).mean())
    
    print 'Average number of pages visits per user: %f'\
    %(grouped_df.apply(lambda x: avg_num_visits(x,1)).mean())
    
    print 'Average number of pages visits per user given',\
    'they visited more than a single page: %f'\
    %(grouped_df.apply(lambda x: avg_num_visits(x,2)).mean())
    
    print 'Average number of categories visits per user: %f'\
    %(grouped_df.apply(lambda x: avg_num_categories(x,1)).mean())
    
    print 'Average number of categories visited per user',\
    'given they visitied more than a single page: %f '\
    %(grouped_df.apply(lambda x: avg_num_category_page(x,2)).mean())
    
    print 'Average number of categories visits per user given ',\
    'they visited more than one category: %f'\
    %(grouped_df.apply(lambda x: avg_num_categories(x,2)).mean())
    return None 
