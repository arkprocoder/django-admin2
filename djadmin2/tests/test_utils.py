from django.test import TestCase
from django.utils import six

from .. import utils
from ..views import IndexView
from .models import UtilsTestModel


class UtilsTest(TestCase):

    def setUp(self):
        self.instance = UtilsTestModel()

    def test_as_model_class(self):
        self.assertEqual(
            UtilsTestModel._meta,
            utils.model_options(UtilsTestModel)
        )
        UtilsTestModel._meta.verbose_name = "Utils Test Model is singular"
        UtilsTestModel._meta.verbose_name_plural = "Utils Test Model are " +\
            " plural"
        self.assertEqual(
            UtilsTestModel._meta,
            utils.model_options(UtilsTestModel)
        )
        UtilsTestModel._meta.verbose_name = "Utils Test Model"
        UtilsTestModel._meta.verbose_name_plural = "Utils Test Models"

    def test_as_model_instance(self):
        self.assertEqual(
            self.instance._meta,
            utils.model_options(self.instance)
        )
        self.instance._meta.verbose_name = "Utils Test Model is singular"
        self.instance._meta.verbose_name_plural = "Utils Test Model are " +\
            " plural"
        self.assertEqual(
            self.instance._meta,
            utils.model_options(self.instance)
        )
        self.instance._meta.verbose_name = "Utils Test Model"
        self.instance._meta.verbose_name_plural = "Utils Test Models"

    def test_admin2_urlname(self):
        self.assertEqual(
            "admin2:None_None_index",
            utils.admin2_urlname(IndexView, "index")
        )

    def test_model_app_label_as_model_class(self):
        self.assertEqual(
            UtilsTestModel._meta.app_label,
            utils.model_app_label(UtilsTestModel)
        )

    def test_model_app_label_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.app_label,
            utils.model_app_label(UtilsTestModel)
        )

    def test_model_verbose_name_as_model_class(self):
        self.assertEqual(
            UtilsTestModel._meta.verbose_name,
            utils.model_verbose_name(UtilsTestModel)
        )

    def test_model_verbose_name_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.verbose_name,
            utils.model_verbose_name(self.instance)
        )

    def test_model_verbose_name_plural_as_model_class(self):
        self.assertEqual(
            UtilsTestModel._meta.verbose_name_plural,
            utils.model_verbose_name_plural(UtilsTestModel)
        )

    def test_model_verbose_name_plural_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.verbose_name_plural,
            utils.model_verbose_name_plural(self.instance)
        )

    def test_model_field_verbose_name_autogenerated(self):
        self.assertEqual(
            'field1',
            utils.model_field_verbose_name(self.instance, 'field1')
        )

    def test_model_field_verbose_name_overridden(self):
        self.assertEqual(
            'second field',
            utils.model_field_verbose_name(self.instance, 'field2')
        )

    def test_model_method_verbose_name(self):
        self.assertEqual(
            'Published recently?',
            utils.model_method_verbose_name(self.instance, 'was_published_recently')
        )

    def test_model_method_verbose_name_fallback(self):
        self.assertEqual(
            'simple_method',
            utils.model_method_verbose_name(self.instance, 'simple_method')
        )

    def test_app_label_as_model_class(self):
        self.assertEqual(
            UtilsTestModel._meta.app_label,
            utils.model_app_label(UtilsTestModel)
        )

    def test_app_label_as_model_instance(self):
        self.assertEqual(
            self.instance._meta.app_label,
            utils.model_app_label(self.instance)
        )

    def test_get_attr_callable(self):
        class Klass(object):
            def hello(self):
                return "hello"

        self.assertEqual(
            utils.get_attr(Klass(), "hello"),
            "hello"
        )

    def test_get_attr_str(self):
        class Klass(object):
            def __str__(self):
                return "str"

            def __unicode__(self):
                return "unicode"

        if six.PY2:
            self.assertEqual(
                utils.get_attr(Klass(), "__str__"),
                "unicode"
            )
        else:
            self.assertEqual(
                utils.get_attr(Klass(), "__str__"),
                "str"
            )

    def test_get_attr(self):
        class Klass(object):
            attr = "value"

        self.assertEqual(
            utils.get_attr(Klass(), "attr"),
            "value"
        )
