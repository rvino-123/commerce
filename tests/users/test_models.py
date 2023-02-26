import pytest


# Test the User Model Methods
def test_user_str(base_user):
    """
    Tests the custom user model string representation.
    """
    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    """
    Tests that the user model's get_short_name method returns the user's short name.
    """
    short_name = f"{base_user.username}"
    assert base_user.__short_name__() == short_name


def test_user_full_name(base_user):
    """
    Tests that the user model's get_short_name method returns the user's short name.
    """
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name() == full_name


def test_base_user_email_is_normalized(base_user):
    """
    Tests that a new base user's email is normalized.
    """
    email = "base@example.com"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """
    Tests that a new super user's email is normalized.
    """
    email = "super@example.com"
    assert super_user.email == email.lower()


# User Factory Tests
def test_super_user_is_not_staff(user_factory):
    """
    Test that an error is raised when an admin user has is_staff set to false
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"


def test_superuser_is_superuser(user_factory):
    """
    Test that an error is raised when an admin user has is_superuser set to false
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_superuser=True"


def test_create_user_with_no_email(user_factory):
    """
    Tests that a base user cannot be created without an email.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_with_no_username(user_factory):
    """
    Tests that a base user cannot be created without an email.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "Base User Account: A username is required"


def test_create_user_with_first_name(user_factory):
    """
    Tests that a base user cannot be created without an email.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Base User Account: A first name is required"


def test_create_user_with_last_name(user_factory):
    """
    Tests that a superuser cannot be created without an email.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Base User Account: A last name is required"


def test_create_superuser_with_no_password(user_factory):
    """
    Test creating a superuser without a password raises an error.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superusers must have a password"


def test_user_email_incorrrect(user_factory):
    """
    Tests that a user must have a valid email address.
    """
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realestate.com")
    assert str(err.value) == "You must provide a valid email address"
