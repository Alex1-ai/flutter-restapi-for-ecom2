from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(
            name="Alex",
            email="alexanderemmanuel1719@gmail.com",
            is_staff=True,
            is_superuser=True,
            phone='0238559158',
            gender='Male'
        )
        user.set_password('123123')
        user.save()


    
    dependencies= [

    ]

    operations= [
        migrations.RunPython(seed_data),
    ]