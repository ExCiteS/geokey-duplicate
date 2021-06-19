from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from ..views import (
    IndexPage, DuplicateProject, DuplicateCategory
    )


class UrlTest(TestCase):

    def test_index_page(self):
        self.assertEqual(reverse('geokey_duplicate:index'), '/admin/duplicate/')

        resolved = resolve('/admin/duplicate/')
        self.assertEqual(resolved.func.func_name, IndexPage.__name__)
