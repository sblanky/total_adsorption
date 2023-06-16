import pygaps as pg
import pygaps.parsing as pgp
import pygaps.graphing as pgg
from pygaps.core.modelisotherm import ModelIsotherm
from pygaps.core.pointisotherm import PointIsotherm

from CoolProp.CoolProp import PropsSI


def density(
    p: float,
    T: float,
    adsorbate: str,
):
    return PropsSI(
        'D',
        'T', T,
        'P|gas', p,
        adsorbate
    )


def total_molar(
    density,
    excess_loading,
    total_pore_volume,
    molar_mass,
):
    excess_mass = excess_loading * molar_mass
    total_mass = excess_mass + (density * total_pore_volume)
    total_molar = total_mass / molar_mass
    return total_molar


def total_adsorption(
    isotherm: "ModelIsotherm|PointIsotherm",
    total_pore_volume: float,
):

    isotherm.convert(
        pressure_unit='Pa',
        material_unit='kg',
        loading_unit='mol'
    )
    isotherm.convert_temperature(unit_to='K')

    adsorbate = isotherm.adsorbate
    molar_mass = isotherm.adsorbate.molar_mass()
    excess_loading = list(isotherm.loading())
    temperature = isotherm.temperature

    total_loading = []
    for n in excess_loading:
        d = density(
            float(isotherm.pressure_at(n)),
            temperature,
            str(adsorbate)
            )
        total = total_molar(
            d, n,
            total_pore_volume, molar_mass,)
        total_loading.append(total)

    total_isotherm = pg.PointIsotherm(
        pressure=isotherm.pressure(),
        loading=total_loading,

        material=isotherm.material,
        adsorbate=str(adsorbate),

        temperature=isotherm.temperature,
        temperature_unit='K',

        pressure_unit='Pa',
        pressure_mode='absolute',
        material_unit='kg',
        material_basis='mass',
        loading_unit='mol',
        loading_basis='molar',
    )
    return total_isotherm


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    isotherm = pgp.isotherm_from_aif('./HTb300-4800.aif')
    total_isotherm = total_adsorption(isotherm, 1.08)
    for iso in [isotherm, total_isotherm]:
        iso.convert(
            pressure_unit='bar',
            loading_unit='mmol',
            material_unit='g',
        )
    total_isotherm.to_csv('result.csv')

    pgg.plot_iso([isotherm, total_isotherm])
    plt.show()
