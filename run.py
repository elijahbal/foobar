"""This script will actually run the factory.

The strategy is quite simple:

    - We now that the mean time to make a `bar` is 1.25 sec,
    because the time is uniformely distributed between 0.5
    and 2 seconds.
    - We now that the exact time to make a foo is 1.00 sec 
    but since the `foo` object is lost
    at each failed attempt, 40% of the foo objects will
    be destroyed.
    - A `foobar` object _costs_ takes an average 
    time of 2 / 0.6 secs to be made, because of the success 


Then, the actual output rate is 
    - `foo` objects: 0.6 objects / sec
    - `bar` objects: 0.8 objects / sec
    - `foobar` objects: 0.3 objects / sec

We can dedicate one half of the robot pool to make
`foo` objects and one half of the robot pool to make `bar`
objects.

When the quantity of foo and bars goes above a certain
threshold, we can dedicate all the pool to make
`foobar`s, then sell them, then buy robots, append them to 
the pool, then redistribute the workforce between `foo`
and `bar` producers, and repeat again.

"""


from .factory import FooBarFactory

my_factory = FooBarFactory()

my_factory.run()
