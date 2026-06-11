# a=[13,10,14,6,1,7,12]

# smalest=a[0]

# for i in a:
#     if i<smalest:
#         smalest=i
# print(smalest)        

# rabbit=1042
# bird=2272
# year=0
# #by 3.8% and birds by 1.2% in a year. 
# while bird>rabbit:
#     rabbit=rabbit+rabbit*0.038
#     bird=bird+bird*0.012
#     year=year+1

# print(f" the number of rabbits will exceed the number of birds later {year} year")

import numpy as np
w=np.array([18, 547, 165, 51, 54, 155, 164, 51, 141, 451])
W_mean=np.mean(w)
W_std=np.std(w)
defect=W_mean+2*W_std

defectParts=w[w>defect] # masking methot
print(f" Parts considered defective {defectParts} ")