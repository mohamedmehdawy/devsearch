from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

def getUser(request):
    """
        this function return user insted of session id
        parameters:
            request: request object
        return: user object
    """
    session_key = request.COOKIES.get('sessionid')
    session = Session.objects.get(session_key=session_key)
    user_id = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(id=user_id)
    
    return user