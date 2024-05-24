oxygen = 0
water_l = -285.8
water_g = -241.8
cdioxide = -393.5
C_water = 4.184
LCV = 0


def Calorific_Value(given, n_given, n_O, n_CO2, n_H2O):  # in kJ/mol
    HCV = ((n_CO2 * cdioxide) + (n_H2O * water_l)) - ((n_given * given) + (n_O * oxygen))
    global LCV
    LCV = ((n_CO2 * cdioxide) + (n_H2O * water_g)) - ((n_given * given) + (n_O * oxygen))

    print(f"HCV: {HCV} kJ/mol")
    print(f"LCV: {LCV} kJ/mol")
    print("\n")


def Heat_of_Combustion(T_o, T_f, m_H2O, given_mass_i, given_mass_f, given_gmol):  # in degrees C and grams
    if T_f == 0:
        T = T_o
    else:
        T = T_f - T_o
    fuel_consumed = given_mass_i - given_mass_f
    n = fuel_consumed / given_gmol
    q_water = m_H2O * C_water * T
    q_fuel = -q_water
    heat_of_combustion = q_fuel / n

    print(f"Moles of Fuel Consumed: {n} mol")
    print(f"q Water: {q_water} kJ")
    print(f"q Fuel: {q_fuel} kJ")
    print(f"Heat of Combustion: {heat_of_combustion} kJ/mol")
    print("\n")


def SE(heat_rxn, gmol):
    se = heat_rxn * 1000 / (1 * pow(10, 6)) / gmol * 1000
    return se  # MJ/mol


def ED(SE, density):
    ed = SE * density
    return ed


def Specific_Energy_Density(heat_rxn, gmol, density):
    se = SE(heat_rxn, gmol)
    ed = ED(se, density)

    print(f"Specific Energy: {se} MJ/kg")
    print(f"Energy Density: {ed} MJ/m^3")
    print("\n")


print("""
[1] Calorific Value
[2] Heat of Combustion
[3] Specific Energy / Density
""")

while True:
    choice = int(input("choose: "))
    if choice == 1:
        given = float(input("Hydrocarbon: "))
        n_given = float(input("No. of mol: "))
        n_O = int(input("No. of mol for Oxygen: "))
        n_CO2 = int(input("No. of mol for C.Dioxide: "))
        n_H2O = int(input("No. of mol for Water: "))
        Calorific_Value(given, n_given, n_O, n_CO2, n_H2O)
    elif choice == 2:
        T_o = float(input("Initial Temp (C): "))
        T_f = float(input("Final Temp (C): "))
        m_H2O = float(input("Mass of Water (g): "))
        given_mass_i = float(input("Initial Mass of Hydrocarbon (g):"))
        given_mass_f = float(input("Final Mass of Hydrocarbon (g): "))
        given_gmol = float(input("Molar Mass of Hydrocarbon (g/mol): "))
        Heat_of_Combustion(T_o, T_f, m_H2O, given_mass_i, given_mass_f, given_gmol)
    elif choice == 3:
        heat_rxn = float(input("Heat of Combustion: "))
        if heat_rxn == 0:
            if LCV == 0:
                raise "LCV = 0"
            else:
                heat_rxn = LCV
        gmol = float(input("Molar Mass (g/mol): "))
        density = float(input("Density (kg/m^3): "))
        Specific_Energy_Density(heat_rxn, gmol, density)
