#!/usr/bin/env python
# coding: utf-8

# In[1]:


I_P = "https://localhost/?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=1&STYLES=default&FORMAT=image/png&TRANSPARENT=TRUE&CRS=CRS:84&BBOX=11.45586126,48.77322986,11.45686126,48.77422986&WIDTH=1024&HEIGHT=1024"
O_P = "https://ois.had.in.here.com/api/rest/v1/wms/getMap/bbox/11.45586126,48.77322986,11.45686126,48.77422986/width/1024/height/1024/format/png?imageryType=VEXCEL&apiKey=Qy0lC4IEXzdJY6zxUdMk2aWZO2qnmyVvOLQP50lRaEM"


# In[2]:


Input_String = input("Enter the input format: ")


# In[3]:


Desired_String = "https://ois.had.in.here.com/api/rest/v1/wms/getMap/bbox/11.45586126,48.77322986,11.45686126,48.77422986/width/1024/height/1024/format/png?imageryType=VEXCEL&apiKey=Qy0lC4IEXzdJY6zxUdMk2aWZO2qnmyVvOLQP50lRaEM"


# In[4]:


Input_Logic_String = Input_String.split('X=')
Input_Logic_String=Input_Logic_String[1].split('&')
Num_Part = Input_Logic_String[0]
Width_Part = Input_Logic_String[1].split('=')
Width_Part = Width_Part[1]
Height_Part = Input_Logic_String[2].split('=')
Height_Part = Height_Part[1]
print(Num_Part)
print(Width_Part)
print(Height_Part)


# In[5]:


Desired_Logic_String = Desired_String.split('x/')
Output_String_1 = Desired_Logic_String[0] + 'x/'
Output_String_1


# In[6]:


Output_String_2 = Num_Part + '/width/' + Width_Part + '/height/' + Height_Part
Output_String_2


# In[7]:


Output_String_3 = Desired_Logic_String[1].split('/f')
Output_String_3 = '/f'+ Output_String_3[1]
Output_String_3


# In[8]:


Final_Output_String = Output_String_1 + Output_String_2 + Output_String_3
Final_Output_String


# In[9]:


print(Final_Output_String)


# In[ ]:




