#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request, render_template


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model =joblib.load("regression")
        r_l = model.predict([[rates]])
        model =joblib.load("decision_tree")
        r_t = model.predict([[rates]])
        return(render_template("index.html", result_linear=r_l,result_tree=r_t))
    else:
        return(render_template("index.html", result_linear="WAITING",result_tree="WAITING"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




