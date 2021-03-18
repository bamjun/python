#정규화 normalization
a = [12, 23, 31, 32, 32, 42, 43, 65, 76, 93, 96]
a = sorted(a,reverse = True)
for x in a:
    (x-min(a))/(max(a)-min(a))

#표준화 standardization
(x-mean(a))/std(a)
