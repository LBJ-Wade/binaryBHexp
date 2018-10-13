import os

prec_cmd = "python black_hole_scattering.py --q 2 --chiA 0.3 0.7 -0.1 --chiB 0.3 0.6 0.1 --omega_ref 1.8e-2 --wave_time_series --save_file animations/precessing.gif"

prec_rot_cmd = "python black_hole_scattering.py --q 2 --chiA 0.3 0.7 -0.1 --chiB 0.3 0.6 0.1 --omega_ref 1.8e-2 --wave_time_series --auto_rotate_camera --save_file animations/precessing_auto_rotate.gif" 

super_kick_cmd = "python black_hole_scattering.py --q 1.34 --chiA 0.62 -0.27 0.34 --chiB -0.62 0.27 0.34 --wave_time_series --project_on_all_planes --save_file animations/super_kick.gif"

aligned_cmd = "python black_hole_scattering.py --q 2 --chiA 0 0 -0.6 --chiB 0 0 0.8 --omega_ref 1.8e-2 --wave_time_series --project_on_all_planes --save_file animations/aligned.gif" 

os.system(prec_cmd)
for still_time in [-3650, 2280]:
    os.system('%s --still_time %f'%(prec_cmd, still_time))

os.system(prec_rot_cmd)
for still_time in [-3800, -3450, -3100]:
    os.system('%s --still_time %f'%(prec_rot_cmd, still_time))

os.system(super_kick_cmd)
for still_time in [-2600, -100, 15, 2280]:
    os.system('%s --still_time %f'%(super_kick_cmd, still_time))

os.system(aligned_cmd)