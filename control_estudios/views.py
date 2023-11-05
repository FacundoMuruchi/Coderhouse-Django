from django.shortcuts import render, redirect
from .models import Estudiante, Curso
from .forms import CursoForm
# Create your views here.

def inicio(request):
    return render(request=request, template_name="inicio.html")

def cursos(request):
    http_response = render(
        request=request,
        template_name="cursos.html",
        context={"cursos": Curso.objects.all()}
    )
    return http_response

#def profesores(request):
#    return HttpResponse("Vista profesores")

#def entregables(request):
#    return HttpResponse("Vista entregables")

def inscriptos(request):
    http_response = render(
        request=request,
        template_name="estudiantes.html",
        context={"estudiante": Estudiante.objects.all()}
    )
    return http_response

# FORM USANDO SOLO HTML
def crear_curso_html(request):
    return render(request,"crear-curso.html")

# FORM USANDO HTML Y PYTHON
def crear_curso_html_python(request):
    if request.method == "POST": #GUARDAR DATOS
        data = request.POST #request.POST = DICCIONARIO DONDE SE ALMACENAN LOS DATOS DEL FORMULARIO HTML
        curso = Curso(nombre=data["nombre"], comision=data["comision"]) #CONVERTIR DATOS A UN OBJETO CURSO
        curso.save() #GUARDAR EL OBJETO EN LA BD

        # GUARDAR SIN REDIRECCIONAR
        #return redirect("crear-curso")
    
        # GUARDAR Y REDIRECCIONAR
        return redirect("cursos")
    
    else: #CARGAR FORMULARIO INICIAL
        return render(request,"crear-curso.html")
    
# FORM USANDO SOLO PYTHON(DJANGO)

def crear_curso(request):
    if request.method == "POST": # POST (ENVIA LOS DATOS)
        form = CursoForm(request.POST)# CREAR OBJETO FORM CON LOS DATOS DEL USUARIO

        if form.is_valid():# VERIFICA QUE LOS DATOS CUMPLEN CON LAS CONDICIONES DE LA CLASE(FORMS.PY)
            data = form.cleaned_data # DICCIONARIO
            curso=Curso(nombre=data["nombre"], comision=data["comision"]) # CREAR CURSO EN MEMORIA RAM
            curso.save() # GUARDAR CURSO EN BD

            # REDIRIGIR AL LISTADO DE CURSOS
            return redirect("cursos")
        
    else: # GET (MUESTRA LA SEGUNDA VALIDACION)
        form = CursoForm()

    # RENDERIZA LA PLANTILLA DEL FORMULARIO
    return render(
        request=request,
        template_name="crear-curso.html",
        context={"form": form}
    )