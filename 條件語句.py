#!/usr/bin/env python
# coding: utf-8

# ### 條件語句

# 條件語句，在Python一般指的是「if」語句
# 
# 用途為「對指定條件判斷真假(True,False)來確定要是否執行語句的指令」

# In[6]:

print("hello world")
A=50
B=30
if A>B:
    print('hello')


# In[7]:


#實際運作：if 接在後方的條件 True False 來決定動作
if True:
    print('hello')
if False:
    print('hello')


# In[10]:


grade = 85

if   grade>=90 :
    print('超級優秀')
elif grade>=80 :
    print('優秀')
elif grade>=70 :
    print('有及格')

print('結束')

# In[11]:


grade = 10
# else，上面的條件語句，執行該行動

if   grade>=90 :
    print('超級優秀')
elif grade>=80 :
    print('優秀')
elif grade>=70 :
    print('有及格')
else:
    print('不及格')


# In[ ]:




