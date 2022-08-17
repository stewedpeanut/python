#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
total=0
for i in range(n+1):
    if i == n:
        print(i)
    else:
        print(i,end='+')
    total+=i
print(f"={total}")


# In[ ]:


judge=int(input())
lst=input()
lst=lst.split()
ans=[]
for i in lst:
    i=int(i)
    if i>judge:
        ans.append(i)

print(ans)


# In[2]:


lst=input()
lst=lst.split()
ans=0
for i in lst:
    i=int(i)
    if i%2==0:
        ans+=i

print(ans)


# In[4]:


#第四題不知道怎麼改
parent=input()
kid=input()
parent=parent.split()
kid=kid.split()
count=0
for i in range(len(parent)-len(kid)+1):
      if parent[i:i+len(kid)]== kid:
        count+=1
print(count)


# In[ ]:




