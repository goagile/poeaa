from unittest import TestCase


class BaseTestCase(TestCase):

    def assertCasesEqual(self, cases):
        for expected, actual in cases:
            self.assertEqual(expected, actual)

    def assertConditionsAreTrue(self, conditions):
        for expected, equal in conditions:
            self.assertIs(expected, equal)

    def assertMembersInContainer(self, members, container):
        for member in members:
            self.assertIn(member, container)
