from django.contrib.auth import get_user_model

from model_mommy import mommy

from pos_app.account.models import Doctor
from pos_app.category.models import Category, SubCategory
from pos_app.factory.models import Factory
from pos_app.payment.models import Payment, PaymentProduct
from pos_app.product.models import Embalase, UnitType, Product


User = get_user_model()


def create_user(username='username', email='email@user.com', password='password') -> User:
    return User.objects.create_user(username, email, password)


def create_category(**kwargs) -> Category:
    """
    :param kwargs: Category's fields
    :return: Category object
    """
    return mommy.make(Category, **kwargs)


def create_doctor(**kwargs) -> Doctor:
    """
    :param kwargs: Doctor's fields
    :return: Doctor object
    """
    return mommy.make(Doctor, **kwargs)


def create_embalase(**kwargs) -> Embalase:
    """
    :param kwargs: Embalase's fields
    :return: Embalase object
    """
    return mommy.make(Embalase, **kwargs)


def create_factory(**kwargs) -> Factory:
    """
    :param kwargs: Factory's fields
    :return: Factory object
    """
    return mommy.make(Factory, **kwargs)


def create_subcategory(**kwargs) -> SubCategory:
    """
    :param kwargs: SubCategory's fields
    :return: SubCategory object
    """
    return mommy.make(SubCategory, **kwargs)


def create_unit_type(**kwargs) -> UnitType:
    """
    :param kwargs: UnitType's fields
    :return: UnitType object
    """
    return mommy.make(UnitType, **kwargs)


def create_product(**kwargs) -> Product:
    """
    :param kwargs: Product's fields
    :return: Product object
    """
    return mommy.make(Product, **kwargs)


def create_payment(**kwargs) -> Payment:
    """
    :param kwargs: Payment's fields
    :return: Payment object
    """
    return mommy.make(Payment, **kwargs)


def create_payment_product(**kwargs) -> PaymentProduct:
    """
    :param kwargs: PaymentProduct's fields
    :return: PaymentProduct object
    """
    return mommy.make(PaymentProduct, **kwargs)
