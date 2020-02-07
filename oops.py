class UserProfile(object):
    """
    manage profile of user.

    """
    def __init__(self, name, balance):
             self.name = name
             self.balance = balance

obj = UserProfile("vinay",2500)
print("balance of {0} is {1}".format(obj.name,obj.balance))

