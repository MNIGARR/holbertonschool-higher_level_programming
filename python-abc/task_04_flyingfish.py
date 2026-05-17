#!/usr/bin/python3
"""Module that demonstrates multiple inheritance and MRO."""


class Fish:
    """Fish class."""

    def swim(self):
        """Fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from both Fish and Bird."""

    def swim(self):
        """Flying fish swims."""
        print("The flying fish is swimming!")

    def fly(self):
        """Flying fish flies."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
