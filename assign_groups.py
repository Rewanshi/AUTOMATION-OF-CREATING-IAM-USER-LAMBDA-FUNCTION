# import yaml
# import boto3
# from botocore.exceptions import ClientError

# # Initialize a boto3 IAM client
# iam_client = boto3.client('iam')

# # Function to read the YAML file
# def read_yaml(file_path):
#     with open(file_path, 'r') as file:
#         data = yaml.safe_load(file)
#     return data

# # Function to create IAM users
# def create_users(users):
#     print("Creating users...")
#     for user in users:
#         try:
#             response = iam_client.create_user(UserName=user)
#             print(f"User '{user}' created successfully.")
#         except ClientError as e:
#             if e.response['Error']['Code'] == 'EntityAlreadyExists':
#                 print(f"User '{user}' already exists.")
#             else:
#                 print(f"Error creating user '{user}': {e}")

# # Function to create IAM groups and assign users to groups
# def create_groups_and_assign_users(group_assignment):
#     print("\nCreating groups and assigning users...")
#     for group, group_users in group_assignment.items():
#         try:
#             # Create the group
#             iam_client.create_group(GroupName=group)
#             print(f"Group '{group}' created successfully.")
#         except ClientError as e:
#             if e.response['Error']['Code'] == 'EntityAlreadyExists':
#                 print(f"Group '{group}' already exists.")
#             else:
#                 print(f"Error creating group '{group}': {e}")

#         # Assign users to the group
#         for user in group_users:
#             try:
#                 iam_client.add_user_to_group(GroupName=group, UserName=user)
#                 print(f"User '{user}' assigned to group '{group}'.")
#             except ClientError as e:
#                 print(f"Error assigning user '{user}' to group '{group}': {e}")

# # Main function
# def main():
#     # Path to the YAML file
#     yaml_file_path = 'data.yaml'
    
#     # Read the YAML file
#     data = read_yaml(yaml_file_path)
    
#     # Create IAM users
#     create_users(data['Users'])
    
#     # Create IAM groups and assign users to groups
#     create_groups_and_assign_users(data['GroupAssignment'])

# if __name__ == "__main__":
#     main()

import yaml
import boto3

# Initialize a boto3 IAM client
iam_client = boto3.client('iam')

# Function to read the YAML file
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Function to create IAM users
def create_users(users):
    print("Creating users...")
    for user in users:
        try:
            iam_client.create_user(UserName=user)
            print(f"User '{user}' created successfully.")
        except Exception as e:
            print(f"Could not create user '{user}': {e}")

# Function to create IAM groups and assign users to groups
def create_groups_and_assign_users(group_assignment):
    print("\nCreating groups and assigning users...")
    for group, group_users in group_assignment.items():
        try:
            iam_client.create_group(GroupName=group)
            print(f"Group '{group}' created successfully.")
        except Exception as e:
            print(f"Could not create group '{group}': {e}")

        for user in group_users:
            try:
                iam_client.add_user_to_group(GroupName=group, UserName=user)
                print(f"User '{user}' assigned to group '{group}'.")
            except Exception as e:
                print(f"Could not assign user '{user}' to group '{group}': {e}")

# Main function
def main():
    # Path to the YAML file
    yaml_file_path = 'data.yaml'
    
    # Read the YAML file
    data = read_yaml(yaml_file_path)
    
    # Create IAM users
    create_users(data['Users'])
    
    # Create IAM groups and assign users to groups
    create_groups_and_assign_users(data['GroupAssignment'])

if __name__ == "__main__":
    main()


import json
import boto3
import yaml
from pprint import pprint
iam = boto3.client('iam')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    
    bucket_name = 'test-bucket-lambda-tig'
    file_name = 'input.yaml'
    s3_response = s3_client.get_object(bucket=bucket_name, Key=file_name)
    file_data = s3_response['Body'].read().decode('utf')
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    
    users = data['Users']
    groups = data['GroupAssignment']
    
    for nUsers in users:
        response = iam.create_user(UserName=nUsers)

    for groupname, userlist in groups.items():
        response = iam.create_group(GroupName=groupname)
        print(groupname)
        for j in userlist:
            print(j)
            iam.add_user_to_group(GroupName=groupname, UserName=j)
    
    return nUsers, groupname, j










