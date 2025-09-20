list_of_cloud = ["aws","azure","gcp","alibaba"]
print(list_of_cloud)

# Append the new cloud in list.

list_of_cloud.append("ibm".upper())
print(list_of_cloud)

# Inster the cloud on specific place.

list_of_cloud.insert(3, "salesforce" .upper())
print(list_of_cloud)

# Check the lenth of list.

list_length = len(list_of_cloud)
print(list_length)

# For loop
for cloud in list_of_cloud:
    print(cloud)

for i in range(1,11):
    print(i)
