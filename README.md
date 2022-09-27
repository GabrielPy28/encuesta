# Instrucciones Backend:

<h2>1. Instalar las Dependencias del Backend</h2>
    <p>• Archivo: <a href="https://github.com/GabrielPy28/encuesta/blob/main/DjangoQuiz/requirements.txt">requirements.txt</a></p>

<h2>2. Hacer las Migraciones</h2>
   
    • python manage.py makemigrations
    • python manage.py migrate
  
<h2>3. Correr el servidor</h2>
    
    • python manage.py createsuperuser
    • python manage.py runserver

<h2>4. Crear una encuesta:</h2>
    • <a href="http://127.0.0.1:8000/admin/quiz/quiz/add/">añadir encuesta</a>
    |
     <a href="http://127.0.0.1:8000/admin/quiz/answer/add/" target="__blank">añadir respuestas</a> 

# Instrucciones Frontend:

<h2>1. Instalar las Dependencias del Frontend</h2>
    <p>• Archivo: <a href="https://github.com/GabrielPy28/encuesta/blob/main/DjangoQuiz/requirements.txt">requirements.txt</a></p>

<h2>2. Correr el servidor (en una terminal a parte)</h2>
    
    • ng serve

<h2>3. Urls de la Pagina:</h2>
  <ol>
    <li><a href="http://localhost:4200/auth/login">iniciar sesión</a></li>
    <li><a href="http://localhost:4200/auth/register">crear cuenta</a></li>
    <li><a href="http://localhost:4200/quizzes/all">ver encuestas</a></li>
  </ol>
