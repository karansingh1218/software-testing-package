from flask import Flask, request,abort
import json
import numpy as np
import pandas as pd
app = Flask(__name__)
df = pd.DataFrame({'col1': ['abc', 'def', 'tre'],
                   'col2': ['foo', 'bar', 'stuff']})

@app.route('/')
def result():
    return "BOB"

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    d = {'email': ['admin@example.com']}
    useremailDataframe = pd.DataFrame(data = d)
    
    if request.method == 'POST':
        foo = request.form['userEmail']
        print(foo)
        string = str(foo)
        c = {'email': [string]}
        postResponseDataFrame = pd.DataFrame(c)
        df3 = useremailDataframe.append(postResponseDataFrame, ignore_index=True)
        
        return df3.to_html(header="true", table_id="table")

    return useremailDataframe.to_html(header="true", table_id="table")


