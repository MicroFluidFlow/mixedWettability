# mixedWettability

The following README is for the manuscript titled "Capillary trapping in mixed-wet porous medium — implications for sub-surface carbon dioxide sequestration"

The repo contains two folders.
1. simulation,
2. wettabilityDistributionCode

Within the repo 'simulation', there exist 4 subfolders with represent the following cases:
(a) deltaTheta_0 correponds to the Δθ = 0 as discussed in the manuscript. That is, porous medium having uniform wettability of 90 degree.
(b) deltaTheta_60 correponds to the Δθ = 60. That is, porous medium having mixed-wettability with contact angle in the range 60 to 120 degree.
(c) deltaTheta_120 correponds to the Δθ = 120. That is, porous medium having mixed-wettability with contact angle in the range 30 to 150 degree.
(d) deltaTheta_180 correponds to the Δθ = 180. That is, porous medium having mixed-wettability with contact angle in the range 0 to 180 degree.

Within each of the above mentioned deltaTheta_x cases, there exists the following folders:
(i). 0 - a folder that describes the initial and boundary conditions. The setup correponds to commencement of LV flooding.
(ii). constant - folder comprises details regarding the mesh (folder: polyMesh), the solid grains distribution in stl format (folder: triSurface) and properties of the fluids such as density, viscosity and surface tension (file: transportProperties).
(iii). system - folder that comprises of files that control specifics of the simulation (simulation time, output time intervals, time step sizes, tolerance while solving equations etc..)
(iv). a.b_HV - 'a.b' refers to the breakthrough time of LV flooding. The boundary conditions are changed accordingly to commence HV flooding from this time. To commence, HV flooding replace the file 'a.b_HV' with 'a.b'.

Series of commands in order to run the OpenFOAM simulations:
setFields (only for LV flooding),
decomposePar (make sure to update the system/decomposeParDict file related to the number of processors the user wants to use),
mpirun -np z interFoam -parallel (where z indicates the number of processors used for the simulations),
reconstructPar (to build the output files).

Within the repo 'wettabilityDistributionCode', there exists a python file 'ca_randomSet.py' that is used to assign contact angles in a random manner. 
Within the python code, line number 11 indicates the range for the distribution of the contact angle. The file currently has a range between 0-180 that corresponds to the Δθ = 180 case.
Running, the code saves a PDF file with the contact angle distribution (note that the output is rotated 90 degree anti-clockwise to match the setup used in the manuscript).
Also, the python script generates a text file with the following data. This data is copied to the 0/alpha.phase file to setup the mixed-wet distribution in the porous medium.

    r1_1
    {
        type            constantAlphaContactAngle;
        theta0          78;
        limit           gradient;
        value           uniform 0;
    }
    r1_2
    {
        type            constantAlphaContactAngle;
        theta0          133;
        limit           gradient;
        value           uniform 0;
    }
    .
    .
    .
    .
    r15_10
    {
        type            constantAlphaContactAngle;
        theta0          6;
        limit           gradient;
        value           uniform 0;
    }
