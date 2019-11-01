a =[2,2,3,2,1,5,5,5,5]
import collections
for item, count in collections.Counter(a).items():
    print(item)
    if count > 1:
        print(item,count)
