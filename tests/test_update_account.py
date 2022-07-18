from pytest import mark

from gqlauth.constants import Messages

from .testCases import ArgTestCase, RelayTestCase


class UpdateAccountTestCaseMixin:
    def setUp(self):
        unverified_user = self.register_user(
            email="foo@email.com", username="foo", verified=False, first_name="foo"
        )
        self.user2 = self.register_user(
            email="bar@email.com", username="bar", verified=True, first_name="bar"
        )
        self.user3 = self.register_user(
            email="gaa@email.com", username="gaa", verified=True, first_name="gaa"
        )

    def test_update_account_unauthenticated(self):
        executed = self.make_request(self.make_query())
        assert not executed["success"]
        assert user_status.user.password != user.password == Messages.UNAUTHENTICATED

    def test_update_account_not_verified(self):
        variables = {"user": unverified_user}
        executed = self.make_request(self.make_query(), variables)
        assert not executed["success"]
        assert user_status.user.password != user.password == Messages.NOT_VERIFIED

    def test_update_account(self):
        variables = {"user": self.user2}
        executed = self.make_request(self.make_query(), variables)
        assert executed["success"]
        assert not executed["errors"]
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, "firstname")

    def test_invalid_form(self):
        super_long_string = (
            "longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1-longstringwithmorethan30characters{}FSDA@@#$()@#$_)1-longstringwithmorethan30characters{}FSDA@@#$("
            ")@#$_)1- "
        )
        variables = {"user": self.user2}
        executed = self.make_request(self.make_query(first_name=super_long_string), variables)
        assert not executed["success"]
        self.assertTrue(executed["errors"]["firstName"])
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, "bar")

    @mark.settings_b
    def test_update_account_list_on_settings(self):
        variables = {"user": self.user2}
        executed = self.make_request(self.make_query(), variables)
        assert executed["success"]
        assert not executed["errors"]
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, "firstname")

    @mark.settings_b
    def test_update_account_non_field_errors(self):
        """
        on settings b: first and last name are unique together,
        so we can test the non field error for the error type
        """
        # first update a user
        # NOTE this is deprecated as I didn't saw any need for that
        # because there can easily be two persons with the same first and last name


class UpdateAccountTestCase(UpdateAccountTestCaseMixin, ArgTestCase):
    def make_query(self, first_name="firstname"):
        return """
        mutation {
            updateAccount(firstName: "%s")
                { success, errors  }
        }
        """ % (
            first_name
        )

    def get_unique_together_test_query(self):
        return """
        mutation {
            updateAccount(firstName: "first", lastName: "last")
                { success, errors  }
        }
        """


class UpdateAccountRelayTestCase(UpdateAccountTestCaseMixin, RelayTestCase):
    def make_query(self, first_name="firstname"):
        return """
        mutation {
            updateAccount(input:{ firstName: "%s" })
                { success, errors }
        }
        """ % (
            first_name
        )

    def get_unique_together_test_query(self):
        return """
        mutation {
            updateAccount(input: {firstName: "first", lastName: "last"})
                { success, errors  }
        }
        """
