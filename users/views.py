from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics, permissions, status

from .models import CustomUser
from .serializers import CustomUserSerializer

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for the custom user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = permissions.IsAuthenticated


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        # 'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(
                reverse('password_reset:reset-password-confirm')),
            reset_password_token.key),
        'site_name': "Stocka"

    }
    # render email text
    email_html_message = render_to_string(
        'account/email/user_reset_password.html', context)
    email_plaintext_message = render_to_string(
        'account/email/user_reset_password.txt', context)
    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Stocka"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@example.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


@api_view()
def success_view(request):
    return Response("Email account has been activated")
