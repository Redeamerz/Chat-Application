import sqlite3
import pandas as pd

datapath = './chat-application.db'

connection = sqlite3.connect(datapath)
c = connection.cursor()
limit = 10000000
last_unix = 0
cur_length = limit
counter = 0
test_done = False

while cur_length == limit:

    df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
    last_unix = df.tail(1)['unix'].values[0]
    cur_length = len(df)
    print("writing to FROM")
    with open('train.from','a', encoding='utf8') as f:
        for content in df['parent'].values:
            f.write(content+'\n')
    
    print("writing to TO")
    with open('train.to','a', encoding='utf8') as f:
        for content in df['comment'].values:
            f.write(str(content)+'\n')

    counter += 1
    print(counter*limit,'rows completed so far')