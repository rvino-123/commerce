from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, username, first_name, last_name, email, password, **kwargs):
        if not username:
            raise ValueError(_("Missing Username"))

        if not first_name:
            raise ValueError(_("Missing First Name"))

        if not last_name:
            raise ValueError(_("Missing Last Namej"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **kwargs
        )

        user.set_password(password)
        kwargs.setdefault("is_superuser", False)
        kwargs.setdefault("is_staff", False)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **kwargs
    ):
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)

        if kwargs.get("is_superuser") is not True:
            raise ValueError(
                _("Cannot create superuser without setting is_superuser to 'True'")
            )

        if not password:
            raise ValueError(_("Password Missing"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email address is required"))

        user = self.create_user(
            username, first_name, last_name, email, password, **kwargs
        )
        user.save(using=self._db)
        return user
