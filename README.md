Simple module for calculating total adsorption from an excess adsorption isotherm.

Relies on [pyGAPS](https://github.com/pauliacomi/pyGAPS/) for isotherm import and modelling, as well as [CoolProp](http://www.coolprop.org/coolprop/wrappers/Python/index.html) for density calculations. Isotherms must be in `pyGAPS` class, i.e. `PointIsotherm` or `ModelIsotherm`. Pore volume must also be known (e.g. via nitrogen porosimetry).

Not yet installable; just copy `total_adsorption.py` into your working directory, and follow insructions below.

### Basic use

```py
import pygaps.parsing as pgp # to parse isotherms
from total_adsorption import total_adsorption

# import isotherm
isotherm = pgp.isotherm_from_aif('/path/to/file.aif')
# calculate total adsorption, using the correct pore volume
total_isotherm = total_adsorption(isotherm, 1.00)
```

The total isotherm exists as a pyGAPS point isotherm. Thus it can be exported;

```py
total_isotherm.to_csv('/path/to/csv.csv')
total_isotherm.to_aif('path/to/aif.aif')
```

Or plotted with the convenient pyGAPS graphing module;

```py
import pygaps.graphing as pgg
import matplotlib.pyplt as plt # may be necessary on some systems
pgg.plot_iso([isotherm, total_isotherm])
plt.show()
```
