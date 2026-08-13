from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=150)),
                ('valor', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('data_da_despesa', models.IntegerField()),
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
