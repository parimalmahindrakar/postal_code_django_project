import os,json
import django
django.setup()
from PostalCodesApp.models import PostalCodes
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PostalCodesProject.settings')

ls = os.listdir("./jsons")
for i in ls:
    name = f"jsons/{i}"
    file = open(name)
    file_dict = json.load(file)
    for i, j in file_dict.items():
        PostalCodes.objects.create(area=i,code=int(j))


# export DJANGO_SETTINGS_MODULE=crudProject.settings
# import django
# django.setup()                 order is compulsory like this
# from crudApp.models import Employee