from member.models.token import Token

def auth_token(func):
    def wrapper(self, info, **kwargs):
        print(info)
        try:
            token = kwargs.get('token')
            print(token)
            token_obj = Token.objects.get(key=token)
            kwargs = token_obj.user
        except Exception as e:
            raise ValueError(e)
        
        return func(self, info, token_obj.user, **kwargs)
    return wrapper