def get_coulomb(charge1, charge2, distance):
    k = 8.99e9
    force = k * abs(charge1) * abs(charge2) / (distance**2)
    return force
