from .psi import psi

def copula(u,v,theta):

    return (

        u*v

        +

        theta

        *psi(u)

        *psi(v)

    )