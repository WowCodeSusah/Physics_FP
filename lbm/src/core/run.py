# Generic imports
import os
import time

# Custom imports
from lbm.src.app.app      import *
from lbm.src.core.lattice import *
from gifgenerator import gif_generate

########################
# Run lbm simulation
########################
def run(lattice, app):

    # Initialize fields and distributions
    app.initialize(lattice)

    date = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')

    # Timer and loop data
    start_time = time.time()
    it         = 0
    compute    = True

    # Solve
    print('### Solving')
    while (compute):

        # Printings
        app.printings(it)

        # Set inlets
        app.set_inlets(lattice, it)

        # Compute macroscopic fields
        lattice.macro()

        # Output field
        app.outputs(lattice, it)

        # Compute equilibrium state
        lattice.equilibrium()

        # Streaming
        lattice.collision_stream()

        # Boundary conditions
        app.set_bc(lattice)

        # Compute observables (drag, lift, etc)
        app.observables(lattice, it)

        # Check stopping criterion
        compute = app.check_stop(it)

        # Increment iteration
        it += 1

    # Count time
    end_time = time.time()
    print("# Loop time = {:f}".format(end_time - start_time))

    # Perform final operations and outputs
    app.finalize(lattice)

    gif_generate(date)

