import os
from test.testlib import *
from git import *

class TestActor(object):
    def test_from_string_should_separate_name_and_email(self):
        a = Actor.from_string("Michael Trier <mtrier@example.com>")
        assert_equal("Michael Trier", a.name)
        assert_equal("mtrier@example.com", a.email)

    def test_from_string_should_handle_just_name(self):
        a = Actor.from_string("Michael Trier")
        assert_equal("Michael Trier", a.name)
        assert_equal(None, a.email)

    def test_should_display_representation(self):
        a = Actor.from_string("Michael Trier <mtrier@example.com>")
        assert_equal('<GitPython.Actor "Michael Trier <mtrier@example.com>">', repr(a))

    def test_str_should_alias_name(self):
        a = Actor.from_string("Michael Trier <mtrier@example.com>")
        assert_equal(a.name, str(a))