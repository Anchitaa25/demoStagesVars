import json
import sys
import requests
Organization_Name = sys.argv[2]
Project_Name = sys.argv[3]
Repository_Name = sys.argv[1]
User_Name = sys.argv[4]
Personal_Token = sys.argv[5]
param1 = sys.argv[6]
param2 = sys.argv[7]
def add():
  result = param1 + param2
def deleteRepository():
  get_URL = 'https://dev.azure.com/'+Organization_Name+'/'+Project_Name+'/_apis/git/repositories/'+Repository_Name+'?api-version=5.1'
  get_ID_request = requests.get(url = get_URL , auth = (User_Name,Personal_Token))
  data = get_ID_request.json()
  Repository_ID = data["id"]
  delete_URL = "https://dev.azure.com/"+Organization_Name+"/"+Project_Name+"/_apis/git/repositories/"+Repository_ID+"?api-version=5.1"
  delete_repo_request = requests.delete(url = delete_URL, auth =  (User_Name,Personal_Token))

try:
  deleteRepository()
  add()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
