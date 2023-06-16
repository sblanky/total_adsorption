Simple module for calculating total adsorption from an excess adsorption isotherm.

Not yet installable.

Relies on [pyGAPS](https://github.com/pauliacomi/pyGAPS/) for isotherm import and modelling, as well as [CoolProp](http://www.coolprop.org/coolprop/wrappers/Python/index.html) for density calculations. Files must be in [`.aif` format](https://raw2aif.adsorptioninformationformat.com/) in order to be parsed, with the adsorbate and experimental temperatures defined. Pore volume must also be known (e.g. via nitrogen porosimetry).

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
```
