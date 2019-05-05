import views
from flask.ext.via.routers import default, Include

routes = [
    default.Functional('/', views.home),
    default.Functional('/top_played', views.top_played),
    default.Functional('/callback/q', views.callback)
]
