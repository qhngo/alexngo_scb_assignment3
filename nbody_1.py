"""
    N-body simulation.
    No.1: Reducing function call overhead
    
    In this file, I will combine all unnecessary functions calls into function advance() 
    and make some changes to avoid recomputation of compute_b(). Since parameters to compute_b()
    are the same, except m1 and m2, ideally, I only need to compute twice. This is where the
    significant improvement can be achieved. Then, I will comment out uncessary functions. Of course,
    I will need to update report_energy() accordingly.
"""
from datetime import datetime

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),

    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),

    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),

    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}

#def compute_deltas(x1, x2, y1, y2, z1, z2):
#    return (x1-x2, y1-y2, z1-z2)

#def compute_b(m, dt, dx, dy, dz):
#    mag = compute_mag(dt, dx, dy, dz)
#    return m * mag

#def compute_mag(dt, dx, dy, dz):
#    return dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))

#def update_vs(v1, v2, dt, dx, dy, dz, m1, m2):
#    v1[0] -= dx * compute_b(m2, dt, dx, dy, dz)
#    v1[1] -= dy * compute_b(m2, dt, dx, dy, dz)
#    v1[2] -= dz * compute_b(m2, dt, dx, dy, dz)
#    v2[0] += dx * compute_b(m1, dt, dx, dy, dz)
#    v2[1] += dy * compute_b(m1, dt, dx, dy, dz)
#    v2[2] += dz * compute_b(m1, dt, dx, dy, dz)

#def update_rs(r, dt, vx, vy, vz):
#    r[0] += dt * vx
#    r[1] += dt * vy
#    r[2] += dt * vz

#original advance()
#def advance(dt):
#    '''
#        advance the system one timestep
#    '''
#    seenit = []
#    for body1 in BODIES.keys():
#        for body2 in BODIES.keys():
#            if (body1 != body2) and not (body2 in seenit):
#                ([x1, y1, z1], v1, m1) = BODIES[body1]
#                ([x2, y2, z2], v2, m2) = BODIES[body2]
#                (dx, dy, dz) = compute_deltas(x1, x2, y1, y2, z1, z2)
#                update_vs(v1, v2, dt, dx, dy, dz, m1, m2)
#                seenit.append(body1)
#
#    for body in BODIES.keys():
#        (r, [vx, vy, vz], m) = BODIES[body]
#        update_rs(r, dt, vx, vy, vz)
  
##new advance(), move nested loop from nbody() to advance() - iter 1
#def advance(loops, iterations, dt):
#    '''
#        advance the system one timestep
#    '''
#    for _ in range(loops):
#        start_time = datetime.now()
#        report_energy()
#        end_time = datetime.now()
#        #print("-- 2.2 report_energy() takes {} ms".format((end_time - start_time).total_seconds()*1000))
#
#        for _ in range(iterations):
#            start_time = datetime.now()
#            seenit = []
#            for body1 in BODIES.keys():
#                for body2 in BODIES.keys():
#                    if (body1 != body2) and not (body2 in seenit):
#                        ([x1, y1, z1], v1, m1) = BODIES[body1]
#                        ([x2, y2, z2], v2, m2) = BODIES[body2]
#                        (dx, dy, dz) = compute_deltas(x1, x2, y1, y2, z1, z2)
#                        update_vs(v1, v2, dt, dx, dy, dz, m1, m2)
#                        seenit.append(body1)
#
#            for body in BODIES.keys():
#                (r, [vx, vy, vz], m) = BODIES[body]
#                update_rs(r, dt, vx, vy, vz)
#            end_time = datetime.now()
#            #print("-- 2.3 advance() in iterations takes {} ms".format((end_time - start_time).total_seconds()*1000))
#        #print("-- 2.4 report_energy()")
#        print(report_energy())
#        #print("---------------------------")

#new advance(), replace unnecessary calls with the direct computation - iter 2
#comment compute_deltas(), update_vs(), compute_b()， compute_mag() accordingly
def advance(loops, iterations, dt):
    '''
        advance the system one timestep
    '''
    for _ in range(loops):
        start_time = datetime.now()
        report_energy()
        end_time = datetime.now()
        #print("-- 2.2 report_energy() takes {} ms".format((end_time - start_time).total_seconds()*1000))

        for _ in range(iterations):
            start_time = datetime.now()
            seenit = []
            for body1 in BODIES.keys():
                for body2 in BODIES.keys():
                    if (body1 != body2) and not (body2 in seenit):
                        ([x1, y1, z1], v1, m1) = BODIES[body1]
                        ([x2, y2, z2], v2, m2) = BODIES[body2]
                        
                        #(dx, dy, dz) = compute_deltas(x1, x2, y1, y2, z1, z2)
                        dx, dy, dz = x1-x2, y1-y2, z1-z2
                        
                        #update_vs(v1, v2, dt, dx, dy, dz, m1, m2)
                        core_compute_b = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
                        compute_b_m2 = m2 * core_compute_b
                        compute_b_m1 = m1 * core_compute_b
                        v1[0] -= dx * compute_b_m2
                        v1[1] -= dy * compute_b_m2
                        v1[2] -= dz * compute_b_m2
                        v2[0] += dx * compute_b_m1
                        v2[1] += dy * compute_b_m1
                        v2[2] += dz * compute_b_m1
                        
                        seenit.append(body1)

            for body in BODIES.keys():
                (r, [vx, vy, vz], m) = BODIES[body]
                
                #update_rs(r, dt, vx, vy, vz)
                r[0] += dt * vx
                r[1] += dt * vy
                r[2] += dt * vz
                
            end_time = datetime.now()
            #print("-- 2.3 advance() in iterations takes {} ms".format((end_time - start_time).total_seconds()*1000))
        #print("-- 2.4 report_energy()")
        print(report_energy())
        #print("---------------------------")
    
#def compute_energy(m1, m2, dx, dy, dz):
#    return (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)

#original report_energy()
#def report_energy(e=0.0):
#    '''
#        compute the energy and return it so that it can be printed
#    '''
#    seenit = []
#    for body1 in BODIES.keys():
#        for body2 in BODIES.keys():
#            if (body1 != body2) and not (body2 in seenit):
#                ((x1, y1, z1), v1, m1) = BODIES[body1]
#                ((x2, y2, z2), v2, m2) = BODIES[body2]
#                (dx, dy, dz) = compute_deltas(x1, x2, y1, y2, z1, z2)
#                e -= compute_energy(m1, m2, dx, dy, dz)
#                seenit.append(body1)
#
#    for body in BODIES.keys():
#        (r, [vx, vy, vz], m) = BODIES[body]
#        e += m * (vx * vx + vy * vy + vz * vz) / 2.
#
#    return e

#new report_energy() where compute_energy() is replaced
def report_energy(e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    seenit = []
    for body1 in BODIES.keys():
        for body2 in BODIES.keys():
            if (body1 != body2) and not (body2 in seenit):
                ((x1, y1, z1), v1, m1) = BODIES[body1]
                ((x2, y2, z2), v2, m2) = BODIES[body2]
                
                #(dx, dy, dz) = compute_deltas(x1, x2, y1, y2, z1, z2)
                dx, dy, dz = x1-x2, y1-y2, z1-z2
                
                #e -= compute_energy(m1, m2, dx, dy, dz)
                delta_e = (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
                e -= delta_e
                seenit.append(body1)

    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.

    return e

def offset_momentum(ref, px=0.0, py=0.0, pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m

    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
    #start_time = datetime.now()
    offset_momentum(BODIES[reference])
    #end_time = datetime.now()
    #print("-- 2.1 Set up global state takes {} ms".format((end_time - start_time).total_seconds()*1000))

# comment this out as we have placed it in advance()
#    for _ in range(loops):
#        start_time = datetime.now()
#        report_energy()
#        end_time = datetime.now()
#        #print("-- 2.2 report_energy() takes {} ms".format((end_time - start_time).total_seconds()*1000))
#
#        for _ in range(iterations):
#            start_time = datetime.now()
#            advance(0.01)
#            end_time = datetime.now()
#            #print("-- 2.3 advance() in iterations takes {} ms".format((end_time - start_time).total_seconds()*1000))
#        #print("-- 2.4 report_energy()")
#        print(report_energy())
#        #print("---------------------------")

    advance(loops, iterations, 0.01)

if __name__ == '__main__':
    print("1. In Main")
    start_time = datetime.now()
    nbody(100, 'sun', 20000)
    end_time = datetime.now()
    print("1. Execution time (s) = {}".format((end_time - start_time).total_seconds()))