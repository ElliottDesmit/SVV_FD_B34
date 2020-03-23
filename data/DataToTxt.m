
data = importdata('FTISxprt-20200306_flight2.mat');

T = [data.vane_AOA.data, data.elevator_dte.data, data.column_fe.data,...
    data.lh_engine_FMF.data, data.rh_engine_FMF.data, data.lh_engine_itt.data,...
    data.rh_engine_itt.data ,data.lh_engine_OP.data, data.rh_engine_OP.data,...
    data.column_Se.data, data.lh_engine_fan_N1.data, data.lh_engine_turbine_N2.data,...
    data.rh_engine_fan_N1.data ,data.rh_engine_turbine_N2.data, data.lh_engine_FU.data,...
    data.rh_engine_FU.data, data.delta_a.data, data.delta_e.data, data.delta_r.data,...
    data.Gps_date.data, data.Gps_utcSec.data, data.Ahrs1_Roll.data, data.Ahrs1_Pitch.data,...
    data.Fms1_trueHeading.data, data.Gps_lat.data, data.Gps_long.data,...
    data.Ahrs1_bRollRate.data, data.Ahrs1_bPitchRate.data, data.Ahrs1_bYawRate.data,...
    data.Ahrs1_bLongAcc.data, data.Ahrs1_bLatAcc.data, data.Ahrs1_bNormAcc.data,...
    data.Ahrs1_aHdgAcc.data, data.Ahrs1_xHdgAcc.data, data.Ahrs1_VertAcc.data,...
    data.Dadc1_sat.data, data.Dadc1_tat.data, data.Dadc1_alt.data, data.Dadc1_bcAlt.data,...
    data.Dadc1_bcAltMb.data, data.Dadc1_mach.data, data.Dadc1_cas.data, data.Dadc1_tas.data,...
    data.Dadc1_altRate.data, data.measurement_running.data, data.measurement_n_rdy.data,...
    data.display_graph_state.data, data.display_active_screen.data, data.time.data'];


D = [data.vane_AOA.description, data.elevator_dte.description, data.column_fe.description,...
    data.lh_engine_FMF.description, data.rh_engine_FMF.description, data.lh_engine_itt.description,...
    data.rh_engine_itt.description ,data.lh_engine_OP.description, data.rh_engine_OP.description,...
    data.column_Se.description, data.lh_engine_fan_N1.description, data.lh_engine_turbine_N2.description,...
    data.rh_engine_fan_N1.description ,data.rh_engine_turbine_N2.description, data.lh_engine_FU.description,...
    data.rh_engine_FU.description, data.delta_a.description, data.delta_e.description, data.delta_r.description,...
    data.Gps_date.description, data.Gps_utcSec.description, data.Ahrs1_Roll.description, data.Ahrs1_Pitch.description,...
    data.Fms1_trueHeading.description, data.Gps_lat.description, data.Gps_long.description,...
    data.Ahrs1_bRollRate.description, data.Ahrs1_bPitchRate.description, data.Ahrs1_bYawRate.description,...
    data.Ahrs1_bLongAcc.description, data.Ahrs1_bLatAcc.description, data.Ahrs1_bNormAcc.description,...
    data.Ahrs1_aHdgAcc.description, data.Ahrs1_xHdgAcc.description, data.Ahrs1_VertAcc.description,...
    data.Dadc1_sat.description, data.Dadc1_tat.description, data.Dadc1_alt.description, data.Dadc1_bcAlt.description,...
    data.Dadc1_bcAltMb.description, data.Dadc1_mach.description, data.Dadc1_cas.description, data.Dadc1_tas.description,...
    data.Dadc1_altRate.description, data.measurement_running.description, data.measurement_n_rdy.description,...
    data.display_graph_state.description, data.display_active_screen.description, data.time.description];

U = [data.vane_AOA.units, data.elevator_dte.units, data.column_fe.units,...
    data.lh_engine_FMF.units, data.rh_engine_FMF.units, data.lh_engine_itt.units,...
    data.rh_engine_itt.units ,data.lh_engine_OP.units, data.rh_engine_OP.units,...
    data.column_Se.units, data.lh_engine_fan_N1.units, data.lh_engine_turbine_N2.units,...
    data.rh_engine_fan_N1.units ,data.rh_engine_turbine_N2.units, data.lh_engine_FU.units,...
    data.rh_engine_FU.units, data.delta_a.units, data.delta_e.units, data.delta_r.units,...
    data.Gps_date.units, data.Gps_utcSec.units, data.Ahrs1_Roll.units, data.Ahrs1_Pitch.units,...
    data.Fms1_trueHeading.units, data.Gps_lat.units, data.Gps_long.units,...
    data.Ahrs1_bRollRate.units, data.Ahrs1_bPitchRate.units, data.Ahrs1_bYawRate.units,...
    data.Ahrs1_bLongAcc.units, data.Ahrs1_bLatAcc.units, data.Ahrs1_bNormAcc.units,...
    data.Ahrs1_aHdgAcc.units, data.Ahrs1_xHdgAcc.units, data.Ahrs1_VertAcc.units,...
    data.Dadc1_sat.units, data.Dadc1_tat.units, data.Dadc1_alt.units, data.Dadc1_bcAlt.units,...
    data.Dadc1_bcAltMb.units, data.Dadc1_mach.units, data.Dadc1_cas.units, data.Dadc1_tas.units,...
    data.Dadc1_altRate.units, data.measurement_running.units, data.measurement_n_rdy.units,...
    data.display_graph_state.units, data.display_active_screen.units, data.time.units];

DATA = [string(D); string(U); T];

writematrix(DATA,'data.txt');
