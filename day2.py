# 2) Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples


my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(my_list[0])  
print(my_list[2])  
print(my_list[-1])  
print(my_list[1:4])  



my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1])  
print(my_tuple[3])  
print(my_tuple[-1])  
print(my_tuple[:3])  



my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer",
    "hobby": "Reading"
}
print(my_dict["name"])  
print(my_dict["city"])
print(my_dict.get("job"))  
for key, value in my_dict.items():
    print(f"{key}: {value}")
