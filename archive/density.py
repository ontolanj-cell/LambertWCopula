from .derivatives import psi_prime

def density(u,v,theta):

    return (

        1

        +

        theta

        *psi_prime(u)

        *psi_prime(v)

    )