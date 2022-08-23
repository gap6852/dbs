#!/usr/bin/env python
# coding: utf-8


# In[2]:


from flask import Flask,request,render_template


# In[3]:


import joblib


# In[4]:


app = Flask(__name__)


# In[5]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        print(rates)
        return(render_template("index.html", result1 = r1, result2 = r2))
    else:
        return(render_template("index.html", result1 = "waiting", result2 = "waiting"))
    


# In[ ]:


if __name__ == "__main__":
    app.run()


# WSGI --> API which connects the frontend and backend for Python Language only
