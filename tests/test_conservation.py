import numpy as np
def test_energy_conservation(conservation_data):
    total_energy, momentum = conservation_data
    total_energy = np.array(total_energy)
    reference=total_energy[0]
    energy_deviation = np.max(np.abs(total_energy-reference))/np.abs(reference)
    assert energy_deviation < 1e-2
def test_momentum_conservation(conservation_data):
    total_energy, momentum = conservation_data
    momentum = np.array(momentum)    
    momentum_deviation = np.max(np.linalg.norm(momentum, axis=1))
    assert momentum_deviation < 1e-6