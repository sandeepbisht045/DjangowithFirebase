from django.shortcuts import render,redirect
import pyrebase,time

# setting up firebase database to establish connection
config={"apiKey": "AIzaSyAWjpw4KAAOmQTPfVAYetM0PLm02cPTWCE"
        ,"authDomain": "krishworks-104a4.firebaseapp.com","projectId": "krishworks-104a4","storageBucket": "krishworks-104a4.appspot.com"
        ,"messagingSenderId": "128730564978","appId": "1:128730564978:web:99eefdd8bed26fb22335eb","measurementId": "G-V0XHCQ2GV6"
        ,"databaseURL": "https://krishworks-104a4-default-rtdb.firebaseio.com"
}
firebase=pyrebase.initialize_app(config)
database=firebase.database()
auth=firebase.auth()
def retrieve_image_link(l_id):
            link_fetch=database.child("images").child(l_id).get().val()
            return link_fetch["image_link"]   
# Create your views here.
def flush(request):
      request.session.flush()
      return render(request,"index.html")

def index(request):
      if not request.session.get("user_id"):
            return render(request,"index.html")
      else:
            return redirect("/profile")

def login(request):
      if not request.session.get("user_id"):
            if request.method=="POST":
                  email=request.POST.get("email")
                  password=request.POST.get("password")
                  print("details",email,password)
                  try:
                        user=auth.sign_in_with_email_and_password(email,password)
                  except:
                        print("error")
                        return render(request,"index.html",{"alert_login":"Invalid Email or Password","email":email})
                  session_id=user["idToken"]
                  request.session["user_id"]=str(session_id)
                  return redirect("/profile")
            else:
                  return redirect("/index")
      else:
            return redirect("/profile")
      
      # signup view
def signup(request):
      if not request.session.get("user_id"):
            if request.method=="POST":
                  username=request.POST.get("username")
                  email=request.POST.get("email")
                  password=request.POST.get("password")
                  try:
                        user=auth.create_user_with_email_and_password(email,password)
                        
                  except:
                        return render(request,"index.html",{"alert_signup":"Email already exists","email1":email,"username":username})
                  local_id=user["localId"]
                  data={"username":username}
                  database.child("names").child(local_id).set(data)
                  database.child("images").child(local_id).set({"image_link":"https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"})
                  session_id=user["idToken"]
                  request.session["user_id"]=str(local_id)
                  # return render(request,"profiles.html",{"email":email,"password":password})
                  return redirect("/profile")
                  
            else:
                  return redirect("/index")
      else:
            return redirect("/profile")      
      
      # view for logout
def logout(request):
      if request.session.get("user_id"):
            request.session.clear()
            return redirect("/index")
      else:
            return redirect("/profile")
 
#  views for profile
def profile(request):
      if request.session.get("user_id"):
      
            if request.method=="POST":
                  dob=request.POST.get("dob")
                  address=request.POST.get("address")
                  
                  l_id=auth.get_account_info(request.session.get("user_id"))["users"][0]["localId"]
                  email=auth.get_account_info(request.session.get("user_id"))["users"][0]["email"] 
                  data={"dob":dob,"address":address}
                  database.child("users").child(l_id).child("details").child("username").set(data)  
                  data_fetch=database.child("users").child(l_id).child("details").child("username").shallow().get().val() 
                  list=[]
                  data_final=[]
                  for i in data_fetch:
                        list.append(i)
                  for i in list:
                        data_filter=database.child("users").child(l_id).child("details").child("username").child(i).get().val() 
                        
                        data_final.append(data_filter)
                  username_fetch=database.child("names").child(l_id).get().val() 
                  link=retrieve_image_link(l_id)  
                  return render(request,"profiles.html",{"data_fetch":data_final,"email":email,"username":username_fetch["username"],"link":link}) 
                                  
            else: 
                  try:
                        l_id=auth.get_account_info(request.session.get("user_id"))["users"][0]["localId"] 
                        email=auth.get_account_info(request.session.get("user_id"))["users"][0]["email"] 
                        data_fetch=database.child("users").child(l_id).child("details").child("username").shallow().get().val() 
                        username_fetch=database.child("names").child(l_id).get().val()
                        link=retrieve_image_link(l_id)  
                        list=[]
                        data_final=[]
                        for i in data_fetch:
                              list.append(i)
                        for i in list:
                              data_filter=database.child("users").child(l_id).child("details").child("username").child(i).get().val()    
                              data_final.append(data_filter)                     
                        return render(request,"profiles.html",{"data_fetch":data_final,"email":email,"username":username_fetch["username"],"link":link})  
                  except:
                        return render(request,"profiles.html",{"data_fetch":data_final,"email":email,"username":username_fetch["username"],"link":link})  
      return redirect("/index")  
                      
            # upload image logic
def upload_image(request):
      if request.session.get("user_id"):
            if request.method=="POST":
                  url=request.POST.get("url")
                  l_id=auth.get_account_info(request.session.get("user_id"))["users"][0]["localId"]
                  image_link={"image_link":url}
                  database.child("images").child(l_id).set(image_link)
                  link_fetch=database.child("images").child(l_id).get().val()
                  link=retrieve_image_link(l_id)
                  return redirect("/profile",{"link":link})
            else:
                  return redirect("/profile")
      else:
            return redirect("/index")

# reset  password logic
def reset_password(request):
      if request.method=="POST":
            email=request.POST.get("email3")
            try:         
                  reset=auth.send_password_reset_email(email)
                  return render(request,"index.html",{"check_email":"check_email"})
            except:
                  return render(request,"index.html",{"alert_for_reset_password":"Email is not registered","email3":email})
      else:
            return redirect("/index")
      

            
            
      

      
      

            
      
            
      
                  
            
      
      
            
            
      


