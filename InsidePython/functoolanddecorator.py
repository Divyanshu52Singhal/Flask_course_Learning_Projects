import functools

user = {"username":"divyanshu","access_level":"guest"}
user1 = {"username":"div","access_level":"admin"}

def make_secure(access_level):
    def decorator(func): #func is built in 
        @functools.wraps(func)  # making function decorator
        def secure_function(*args,**kwargs):
            if user1["access_level"]==access_level: #checking global user not passed
                return func(*args,**kwargs)
            else:
                return f"No {access_level} permission for {user['username']}."
        return secure_function
    return decorator #return to function call

@make_secure("admin")   #access_level argument
def get_admin_password():
    return "1234:admin"

@make_secure("user")
def get_dashboard_password():
    return "user ka pass :81"

print(get_admin_password())
print(get_dashboard_password())