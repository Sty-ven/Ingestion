
#load packages

import pandas as pd

import os

import argparse

#Create SQL connection
from sqlalchemy import create_engine

def main():

    print("start")

    import pandas as pd

    import os

    import argparse

    #Create SQL connection
    from sqlalchemy import create_engine 

    print("start")  

    user = "root"
    password = "root"
    host = "localhost"
    port = "5432"
    db = "covid_db"
    table_name =  "covid_data"
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv"

    csv_name = 'output.csv'
    
    os.system(f"wget {url} -O {csv_name}") 



       
     
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')    


    df = pd.read_csv(csv_name)  


    df.drop(['FIPS', 'Admin2', 'Province_State'], axis=1, inplace=True) 


    df.dropna(inplace=True) 

    df['Last_Update'] = pd.to_datetime(df['Last_Update'])   


    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')

    


if __name__ == '__main__ ':
    main()
    
#     parser = argparse.ArgumentParser(description='Ingest CSV data to postgres') 

   

#     parser.add_argument('--user', help='user name for postgres')
#     parser.add_argument('--password', help='password for postgres')
#     parser.add_argument('--host', help='host for postgres')
#     parser.add_argument('--port', help='port number for postgres')
#     parser.add_argument('--db', help='databse name for postgres')
#     parser.add_argument('--table_name', help='name of the table where we will write the results to')
#     parser.add_argument('--url', help='url of the csv file')  



#     args = parser.parse_args()

#     main(args)



    





