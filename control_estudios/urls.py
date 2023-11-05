from django.urls import path
from control_estudios.views import inicio, inscriptos, cursos, crear_curso

urlpatterns = [
    path("", inicio, name="inicio"),
    path("estudiantes/", inscriptos, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
    path("crear-curso/", crear_curso, name="crear-curso")
]