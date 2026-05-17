#!/usr/bin/python3
"""Module that defines mixins and Dragon class."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that combines swim and fly abilities."""

    def roar(self):
        """Dragon roar behavior."""
        print("The dragon roars!")
