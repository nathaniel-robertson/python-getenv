# Python program to explain os.environ object 
  
# importing os module 
import os
  
# Get the value of
# 'server_hostname' environment variable defined in MyKinsta's Settings -> Environment variables
server_hostname_var = os.environ.get('server_hostname')
  
# Print the value of
# 'server_hostname' environment variable
print("Server Hostname :", server_hostname_var)
