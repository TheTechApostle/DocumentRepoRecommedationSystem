import datetime
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class SessionIdleTimeout(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            current_time = datetime.datetime.now()
            last_activity = request.session.get('last_activity')

            if last_activity:
                elapsed_time = (current_time - last_activity).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    # Logout the user due to inactivity
                    
                    logout(request)
            request.session['last_activity'] = current_time
