# import pyrebase

# config = {
#   "apiKey": "apiKey",
#   "authDomain": "https://vaccinate-a2930-default-rtdb.firebaseapp.com",
#   "storageBucket": "https://vaccinate-a2930-default-rtdb.appspot.com",
#   "serviceAccount": "path/to/serviceAccountCredentials.json",
#   "databaseURL": "https://vaccinate-a2930-default-rtdb.firebaseio.com/"
# }
# firebase = pyrebase.initialize_app(config)

# print(firebase)

from firebase import firebase

db = firebase.FirebaseApplication("https://vaccinate-a2930-default-rtdb.firebaseio.com/", None)

names = db.get('', None).values()

print(names)
for name in names:
  for address in name:
    print(address)
