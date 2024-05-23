from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Biography(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='biography')
    content = models.TextField()

    def __str__(self):
        return f"Biography of {self.person.name}"

class PoliticalBeliefs(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='political_beliefs')
    content = models.TextField()

    def __str__(self):
        return f"Political beliefs of {self.person.name}"

class CommunityInvolvement(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='community_involvement')
    content = models.TextField()

    def __str__(self):
        return f"Community involvement of {self.person.name}"
    
class RegistrationLink(models.Model):
    link_text = models.CharField(max_length=200)
    url = models.URLField()
    button_text = models.CharField(max_length=50, default="Register Now")

    def __str__(self):
        return self.link_text

class LoginButton(models.Model):
    button_text = models.CharField(max_length=50, default="Log In")
    url = models.URLField()

    def __str__(self):
        return self.button_text
 
class MyNewCombrateRegistrationLink(models.Model):
    url = models.CharField(max_length=255)
    


