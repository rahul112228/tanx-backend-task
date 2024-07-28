#!/bin/bash
echo "Create migration"
python manage.py makemigrations backend
echo "===================================="

echo "Migrate"
python manage.py migrate
echo "================================="

echo "Create superuser if not exists"
echo "
from django.contrib.auth.models import User; 
if not User.objects.filter(username='admin').exists(): 
    User.objects.create_superuser('admin', 'janedoe@gmail.com', 'admin')
" | python manage.py shell
echo "================================="

echo "Start Server"
python manage.py runserver 0.0.0.0:8000
