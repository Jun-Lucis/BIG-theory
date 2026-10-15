def ket(theta):
    return np.array([np.cos(theta), np.sin(theta)], dtype=float)

def projector(theta):
    v=ket(theta)
    return np.outer(v,v)

def density_from_distribution(theta_grid, weights):
    weights=np.maximum(np.asarray(weights,dtype=float),0.0)
    if np.sum(weights)<=1e-15:
        weights=np.ones_like(weights)
    weights=weights/np.sum(weights)
    rho=np.zeros((2,2),dtype=float)
    for th,w in zip(theta_grid,weights):
        rho += w*projector(th)
    rho=0.5*(rho+rho.T)
    tr=np.trace(rho)
    return rho/tr if abs(tr)>1e-15 else np.eye(2)/2

def purity(rho):
    return float(np.trace(rho@rho))

def eig_entropy(rho, eps=1e-12):
    vals=np.linalg.eigvalsh(rho)
    vals=np.maximum(vals,eps)
    vals=vals/np.sum(vals)
    return float(-np.sum(vals*np.log(vals)))

def measurement_prob(rho, alpha):
    return float(np.trace(rho@projector(alpha)))

def periodic_distance_pi(theta, center):
    return 0.5*np.angle(np.exp(2j*(theta-center)))

def gaussian_projective_cloud(theta_grid, center, width_rad):
    if width_rad<=1e-12:
        idx=np.argmin(np.abs(periodic_distance_pi(theta_grid,center)))
        w=np.zeros_like(theta_grid); w[idx]=1.0
        return w
    d=periodic_distance_pi(theta_grid,center)
    w=np.exp(-0.5*(d/width_rad)**2)
    return w/np.sum(w)

def K_BIG(delta,kappa=3.7410978332842775,c=0.0033597884949152297):
    z=kappa*(np.cos(2*delta)-c)
    z=np.clip(z,-60,60)
    return 1/(1+np.exp(-z))

def rmse(a,b):
    return float(np.sqrt(np.mean((np.asarray(a)-np.asarray(b))**2)))

def max_abs_error(a,b):
    return float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
