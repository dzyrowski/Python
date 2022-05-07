#Creating a list of services using Python

#1 Create an empty list
aws_services = list()

#P2 opulate the list using append or insert.

aws_services.append('S3')
aws_services.append('Lambda')
aws_services.append('EC2')
aws_services.append('DynamoDB')

#3Print the list and the length of the list. 
print("AWS Services that use Python:", aws_services)
print("Length of list:", (len(aws_services)))

#4. Remove Lambda and DynamoDB from the list by name or by index.
del aws_services[::2]

#5. Print the new list and the new length of the list
print("AWS Services that use Python:", aws_services)
print("Length of list:", (len(aws_services)))
