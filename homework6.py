my_dict={"кошки": 8, "попугаи": 11, "хомяки": 2}
print(my_dict)
print(my_dict.get("кошки"))
print(my_dict.get("собаки"))
my_dict.update({"рыбки" : 30, "черепахи" : 4 })
#del my_dict["хомяки"]
print(my_dict)
a=my_dict.pop("хомяки")
print(my_dict)
print(a)
my_set={3, 7, 11, 13, 7, 3, "cat", (1,2,3,2)}
print(my_set)
my_set.update({2,6,10,6, "dog"})
print(my_set)
print(my_set.discard(13))
print(my_set)