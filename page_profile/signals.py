from django.db.models.signals import post_save, pre_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Profile, Book
from django.contrib.auth.models import User

# Post save Pre save

@receiver(post_save, sender=Book)    
def post_save_book(sender, instance, created, *args, **kwargs):
    if created:
        print("Kitob yaratildi. Book id: ", instance.id)
    else:
        print("Kitob yangilandi. Book id: ", instance.id)


@receiver(pre_save, sender=Book)    
def pre_save_book(sender, instance, *args, **kwargs):
    print("Kitob yaratilmoqda. Book id: ", instance.id)

@receiver(pre_save, sender=Book)    
def slugify_title_book(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

# Post delete Pre delete

@receiver(pre_delete, sender=Book)    
def pre_delete_book(sender, instance, *args, **kwargs):
    print("Kitob ochirilmoqda. Book id: ", instance.id)

@receiver(post_delete, sender=Book)    
def post_delete_book(sender, instance, *args, **kwargs):
    print("Kitob ochirildi. Book id: ", instance.id)

# M2M changed

@receiver(m2m_changed, sender=Book.author.through)
def m2m_changed_book(sender, instance, action, *args, **kwargs):
    if action == 'post_remove':
        for i in kwargs['pk_set']:
            profile = Profile.objects.get(id=i)
            print(f"({instance.title}) kitobining avtorlaridan {profile.user.username} chiqarib olindi!")
            print(" ")
    
    elif action == 'post_add':
        for i in kwargs['pk_set']:
            profile = Profile.objects.get(id=i)
            print(f"({instance.title}) kitobining avtorlariga {profile.user.username} qoshildi!")
            print(" ")
