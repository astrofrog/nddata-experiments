# Experiments with Converting NDData Types


The objective of this experiment is to provide a protocol for converting
between different subclasses of NDData. So a function designed for a specific
class like `Spectrum1D` can also accept any other NDData subclass by providing
a `Spectrum1D.__from_nddata__` method which takes any `NDData` subclass and
returns a `Spectrum1D`. So specifc to `Spectrum1D` it could reorder the array
to have the spectral dimension last.


The decortator provided in this repo then calls this same `__from_nddata__`
method on the input type after the function is called, so the orginal type is
retuned to the user after the function is called.


For an implementation of `__from_nddata__` see
[this](https://github.com/Cadair/sunpy/commit/247f90a4540caf393170a0d217a128336fd407b6)
commit in SunPy.
