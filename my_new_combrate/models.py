from django.db import models

class Person(models.Model):
    """
    Model representing a person.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the person.
        """
        return self.name

class Biography(models.Model):
    """
    Model representing a biography associated with a person.
    """
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='biography')
    content = models.TextField()

    def __str__(self):
        """
        Return a string representation of the biography.
        """
        return f"Biography of {self.person.name}"

class PoliticalBeliefs(models.Model):
    """
    Model representing political beliefs associated with a person.
    """
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='political_beliefs')
    content = models.TextField()

    def __str__(self):
        """
        Return a string representation of the political beliefs.
        """
        return f"Political beliefs of {self.person.name}"

class CommunityInvolvement(models.Model):
    """
    Model representing community involvement associated with a person.
    """
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='community_involvement')
    content = models.TextField()

    def __str__(self):
        """
        Return a string representation of the community involvement.
        """
        return f"Community involvement of {self.person.name}"

class RegistrationLink(models.Model):
    """
    Model representing a registration link.
    """
    link_text = models.CharField(max_length=200)
    url = models.URLField()
    button_text = models.CharField(max_length=50, default="Register Now")

    def __str__(self):
        """
        Return a string representation of the registration link.
        """
        return self.link_text

class LoginButton(models.Model):
    """
    Model representing a login button.
    """
    button_text = models.CharField(max_length=50, default="Log In")
    url = models.URLField()

    def __str__(self):
        """
        Return a string representation of the login button.
        """
        return self.button_text

class MyNewCombrateRegistrationLink(models.Model):
    """
    Model representing a registration link for MyNewCombrate.
    """
    url = models.CharField(max_length=255)
