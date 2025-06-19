from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from users.models import User
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser(
                'adminka',
                'admin@example.com',
                'adminka')
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Админ создан'))
        else:
            self.stdout.write(self.style.SUCCESS('Админ уже есть'))