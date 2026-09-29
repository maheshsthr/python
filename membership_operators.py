#common and uncommon
list1 = [10,20,30,40]
list2 = [30,40,50,60]

common = [x for x in list1 if x in list2]
uncommon = [x for x in list1+list2 if x not in common]
print(f"Common {common}")
print(f"Uncommon {uncommon}")
