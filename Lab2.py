
# coding: utf-8

# In[2]:


import requests
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')

arr = []
#1Скачивание 1000 последних объявлений с hh.ru
for i  in range(10):
    res=requests.get('http://api.hh.ru/vacancies/?per_page=100&page='+str(i)+'&text=data+science+OR+data+analytics')
    arr.append(res.json())
    print(res.json())
#print(arr[1])


# In[9]:


vac = []
for i in arr:
    for vacancy in i['items']:
        vac.append(vacancy)
print (vac[1])
print (len(vac))
print (type(vac))


# In[10]:


#проходим по словарю sal_dict  и ищем одинаковые названия
sal_dict = {}


print('\n')
for sal in vac:
    if(sal['salary'] != None):
        if ((sal['salary']['to'] != None) and (sal['salary']['from'] != None)):
            salary = (sal['salary']['to'] + sal['salary']['from'])/2
            sal_dict[sal['name']] = salary
        elif ((sal['salary']['to'] == None) and (sal['salary']['from'] != None)):
            salary = sal['salary']['from']
            sal_dict[sal['name']] = salary
        elif ((sal['salary']['to'] != None) and (sal['salary']['from'] == None)):
            salary = sal['salary']['to']/2
            sal_dict[sal['name']] = salary
            
print(sal_dict)


# In[11]:


arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
for key in sal_dict:
    if ('Data Analyst' in  key):
        arr1.append(sal_dict[key])
    if ('Data Science' in key):
        arr2.append(sal_dict[key])
    if ('Big data' in key):
        arr3.append(sal_dict[key])
    if ('Python' in key):
        arr4.append(sal_dict[key])
    if ('Deep Learning'in key):
        arr5.append(sal_dict[key])
print (arr1)
print (arr2)
print (arr3)
print (arr4)
print (arr5)
arr1.sort()
arr2.sort()
arr3.sort()
arr4.sort()
arr5.sort()
med1=arr1[len(arr1)//2]
med2=arr2[len(arr2)//2]
med3=arr3[len(arr3)//2]
med4=arr4[len(arr4)//2]
med5=arr5[len(arr5)//2]
print (arr2)
print (med3)
print (med4)
print (med5)
print (med1)


# In[12]:


#распределение зп по диапазонам
#до 80к
sum_dict = {}
to80k=0
to120k=0
to150k=0
to200k=0
to300k=0
more300k=0
for key in sal_dict:
    if sal_dict[key]<=80000:
        to80k=to80k+1
    if sal_dict[key]>80000 and salary<=120000:
        to120k=to120k+1
    if sal_dict[key]>120000 and salary<=150000:
        to150k=to150k+1
    if sal_dict[key]>150000 and  salary<=200000:
        to200k=to200k+1
    if sal_dict[key]>200000 and salary<=300000:
        to300k=to300k+1
    if sal_dict[key]>300000:
        more300k=more300k+1
sum_dict['80000']=to80k
sum_dict['120000']=to120k
sum_dict['150000']=to150k
sum_dict['200000']=to200k
sum_dict['300000']=to300k
sum_dict['>300000']=more300k
print(sum_dict)


# In[13]:


#График медиан
bins = range(1000, 300000, 10000)

med = [med1, med2, med3, med4, med5]

plt.title('med salary schedule')
plt.ylabel("value")
plt.xlabel("salary")

hist, bins = np.histogram(med, bins = bins)
print(hist, bins)

plt.hist(med, bins)
plt.show()


# In[14]:


bins = range(0, 80, 10)

ran = [to80k,to120k, to150k, to200k, to300k, more300k]

plt.title('salary schedule')
plt.ylabel("value")
plt.xlabel("people")

hist, bins = np.histogram(ran, bins = bins)
print(hist, bins)

plt.hist(ran, bins)
plt.show()

