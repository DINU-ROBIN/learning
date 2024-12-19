from django.shortcuts import render,redirect,HttpResponse
from createacc.models import create
from django.contrib import messages
from .models import create

# Create your views here.



# def createacc(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         userpassword=request.POST.get("userpassword")
#         crr=create(username=username,userpassword=userpassword)
#         crr.save()
#         return redirect("login")
#     return render(request,"createacc.html")




def createacc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userpassword = request.POST.get("userpassword")

        # Check if username or password is empty
        if not username or not userpassword:
            messages.error(request, "Username and password cannot be empty")
            return render(request, "createacc.html")

        # Check if the username already exists
        if create.objects.filter(username=username).exists():
            messages.error(request, "Username Taken !!!")
            return render(request, "createacc.html")

        # Create and save the new user
        crr = create(username=username, userpassword=userpassword)
        crr.save()
        # messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "createacc.html")



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         userpassword = request.POST.get('userpassword')
#         user = authenticate(request, username=username, userpassword=userpassword)
#         print(f"Username: {username}, userpassword: {userpassword}")
#         if user is not None:
#             login(request, user)
#             return redirect('contentt') 
#         else:
#             # messages.warning(request, 'Invalid username or password')
#             return HttpResponse("invalid")
    
#     return render(request,'login.html')



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         userpassword = request.POST.get('userpassword')
#         print(f"username: {username}, userpassword: {userpassword}")  # Debugging print statement
#         userd = authenticate(request, username=username, userpassword=userpassword)
        
#         if userd is not None:
#             login(request, userd)
#             print("Login successful")  # Debugging print statement
#             return redirect('contentt')  # Ensure 'com' is a valid URL name
#         else:
#             print("Invalid username or password")  # Debugging print statement
#             # messages.warning(request, 'Invalid username or password')
#             return HttpResponse("invalid")
    
#     return render(request, 'login.html')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------this code works but it takes the data of admin file----------------------------------------

# logger = logging.getLogger(__name__)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         userpassword = request.POST.get('userpassword')

#         # Log debugging information
#         logger.debug(f"username: {username}, userpassword: {userpassword}")

#         user = authenticate(request, username=username, password=userpassword)
        
#         if user in create:
#             login(request, user)
#             logger.debug("Login successful")
#             return redirect('contentt')  # Ensure 'content' is a valid URL name
#         else:
#             logger.debug("Invalid username or password")
#             messages.warning(request, 'Invalid username or password')
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
    
#     return render(request, 'login.html')
# ------------------------------------------------------------------------------------------------------^this code works but it takes the data of admin file^--------------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpassword = request.POST.get('userpassword')

       
        print(f"username: {username}, userpassword: {userpassword}")

        try:
            
            user = create.objects.get(username=username)
            
           
            if user.userpassword == userpassword:
               
                print("Login successful")
                return redirect('contentt')  
            else:
               
                print("Invalid username or password")
                messages.warning(request, 'Invalid username or password')
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        except create.DoesNotExist:
          
            print("Invalid username or password")
            messages.warning(request, 'Invalid username or password')
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')








# ----------------------------------------------------------------------------above code is correct -------------------------------------------------------

def forgot(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = create.objects.get(username=username)
            # Redirect to the update password view with the username as a query parameter
            return redirect('updatepassword', username=username)
        except create.DoesNotExist:
            return render(request, 'forgot1.html', {'error': 'Username does not exist'})

    return render(request, "forgot1.html")







def updatepassword(request, username): 
    try:
        user = create.objects.get(username=username)
    except create.DoesNotExist:
        return redirect('forgot')  # Redirect to the forgot page if username is not found

    if request.method == 'POST':
        new_password = request.POST.get('new_password')

        if not new_password:
            # If the new password is empty, render the update form again with an error message
            return render(request, 'forgot.html', {
                'username': username,
                'error': 'Password cannot be empty'
            })

        # Update the user's password
        user.userpassword = new_password
        user.save()

        return redirect('login')  # Redirect to login page or another page after updating the password

    # Render the form for the first GET request
    return render(request, 'forgot.html', {'username': username})












    
    





    