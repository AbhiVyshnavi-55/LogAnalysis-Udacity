#!/usr/bin/env python
import psycopg2
#first top 3 articles execution
def View_Articles():
    new=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    old=new.cursor()
    query1= ''' SELECT title, views FROM loganalysis_articles INNER JOIN articles ON
    articles.slug = loganalysis_articles.slug ORDER BY views desc LIMIT 3; '''
    old.execute(query1)
    op=old.fetchall()
    print(" \n  A.What are the most popular three articles of all time ? \n")
    count=1
    for result in op:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"===>{1} views'.format(result[0], result[1]))
#top 4 authors
def View_Authors():
    
    new=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    old=new.cursor()
    query2= '''
    SELECT logauthors_name.name AS author,
    sum(loganalysis_articles.views) AS views FROM loganalysis_articles INNER JOIN logauthors_name
    ON logauthors_name.slug=loganalysis_articles.slug
    GROUP BY logauthors_name.name ORDER BY views desc limit 4;
    '''
    old.execute(query2)
    op=old.fetchall()
    print("\n  B.Who are the most popular article authors of all time ? \n")
    count=1
    for result in op:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"Authors' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"====>{1} views'.format(result[0], result[1]))
#lead errors
def View_Analysis():
    new=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    old=new.cursor()
    query3= '''
    SELECT logerror_fail.date ,(logerror_fail.count*100.00 / loganalysis_total.count) AS
    percentage FROM logerror_fail INNER JOIN loganalysis_total
    ON logerror_fail.date = loganalysis_total.date
    AND (logerror_fail.count*100.00 / loganalysis_total.count) >1
    ORDER BY (logerror_fail.count*100.00 /loganalysis_total.count) desc;
    '''
    old.execute(query3)
    op=old.fetchall()
    print(" \n  C.Days on which more than 1% of requests lead to errors ? ")
    for result in op:
        print('\n  On ' + str(result[0]) +'   -->   ' + '%.1f' % result[1] +'% errors\n')
View_Articles()
View_Authors()
View_Analysis()

