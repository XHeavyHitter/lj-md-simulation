class System:
    def __init__(self, n_cell, rho_star, dt, r_c, T_star):
        self.n_cell = n_cell
        self.rho_star = rho_star
        self.dt = dt
        self.r_c = r_c
        self.T_star = T_star
        self.N = 4 * n_cell**3
        self.L_star = (self.N / rho_star)**(1/3)