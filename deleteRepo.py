import json
import sys
import requests

param1 = sys.argv[1]
param2 = sys.argv[2]
def add():
  result = param1 + param2
  return result
def deleteRepository():
  get_URL = 'https://dev.azure.com/'+Organization_Name+'/'+Project_Name+'/_apis/git/repositories/'+Repository_Name+'?api-version=5.1'
  get_ID_request = requests.get(url = get_URL , auth = (User_Name,Personal_Token))
  data = get_ID_request.json()
  Repository_ID = data["id"]
  delete_URL = "https://dev.azure.com/"+Organization_Name+"/"+Project_Name+"/_apis/git/repositories/"+Repository_ID+"?api-version=5.1"
  delete_repo_request = requests.delete(url = delete_URL, auth =  (User_Name,Personal_Token))

try:
  a = add()
  print(a)
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
