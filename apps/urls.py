from apps.users.urls import urlpatterns as users_urls
from apps.authentication.urls import urlpatterns as auth_urls
from apps.chat.urls import urlpatterns as chat_urls
from apps.profiles.urls import urlpatterns as profile_urls
from apps.recommendations.urls import urlpatterns as recommendations_urls



urlpatterns = users_urls + auth_urls + chat_urls + profile_urls + recommendations_urls
