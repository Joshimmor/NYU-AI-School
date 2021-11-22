import numpy as np
import matplotlib.pyplot  as plt

x1 = np.random.randint(0,500,size=(500))
x2 = []
for i in x1:
  x2.append(i+5)
x = []
i = 0
while i < len(x1):
  x.append(x1[i])
  x.append(x2[i])
  i+=1
plt.hist(x)
plt.title("Random Number Gen")
plt.show()

def data_mean(x):
  sum = 0
  for i in x:
    sum += i
  mean = sum/len(x)  
  return mean
def data_variance(x):
  sample_mean = data_mean(x)
  sample_diff = 0
  for i in x:
    diff = i - sample_mean 
    diff *= diff
    sample_diff += diff
  var = sample_diff/(len(x)-1 )  
  return var
print(data_mean(x1)) 
print(data_mean(x2))
print(data_mean(x))
# The mean for x1 and x2 is five because both data sets are essentially the same but added five. 
#The sample_mean for x should be 2.5 more than x1 and 2.5 less than x2 because it uses both samples to create an average
print(data_variance(x1)) 
print(data_variance(x2))
print(data_variance(x))