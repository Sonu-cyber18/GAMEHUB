from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('game/', views.snake_game_view, name='snake-game'),
    path('chess-game/', views.chess_game_view, name='chess-game'),
    path('puzzle-game/', views.puzzle_game, name='puzzle-game'),
    path('pacman-game/', views.pacman_game, name='pacman-game'),
    path('hill-climber/', views.hill_climber_view, name='hill-climber'),
    path('ludo-game/', views.ludo_game_view, name='ludo-game'),
    path('memory-game/', views.memory_game_view, name='memory-game'),
    path('flappy-bird/', views.flappy_bird_game_view, name='flappy-bird'),
    path('stickman-hitman/', views.stickman_hitman_view, name='stickman-hitman'),
    path('endless-runner/', views.endless_runner_view, name='endless-runner'),
    path('itf/', views.itf_view, name='itf'),
    path("python-learning-game/", views.python_learning_game_view, name="python-learning-game"),
]