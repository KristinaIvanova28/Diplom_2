class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    
    @property
    def register(self):
        return f"{self.BASE_URL}/auth/register"
    
    @property
    def login(self):
        return f"{self.BASE_URL}/auth/login"
    
    @property
    def user(self):
        return f"{self.BASE_URL}/auth/user"
    
    @property
    def orders(self):
        return f"{self.BASE_URL}/orders"
    
    @property
    def ingredients(self):
        return f"{self.BASE_URL}/ingredients"