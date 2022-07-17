def fields(xlen):
    return( 
    [

    ['', '>',  0],
      ['old_keep_dims1', '>',  0],
        ['box_dims1', '>',  0],
          ['box_ident', 'string', 10],
          ['id_byte', 'byte',  0],
          ['now_time', 'integer',  0],
          ['keep_date', 'string', 20],
          ['keep_time', 'string', 20],
          ['top_label', 'string', 100],
          ['project_for', 'string', 50],
          ['reference_string', 'string', 100],
          ['this_was_control_template', 'boolean',  0],
          ['rail_info', '>',  0],
            ['flared_ends_ri', 'integer',  0],
            ['spare_int1', 'integer',  0],
            ['knuckle_code_ri', 'integer',  0],
            ['knuckle_radius_ri', 'extended',  0],
            ['spare_float2', 'extended',  0],
            ['spare_bool1', 'boolean',  0],
            ['spare_bool2', 'boolean',  0],
            ['isolated_crossing_sw', 'boolean',  0],
            ['k_diagonal_side_check_rail_sw', 'boolean',  0],
            ['k_main_side_check_rail_sw', 'boolean',  0],
            ['switch_drive_sw', 'boolean',  0],
            ['track_centre_lines_sw', 'boolean',  0],
            ['turnout_road_stock_rail_sw', 'boolean',  0],
            ['turnout_road_check_rail_sw', 'boolean',  0],
            ['turnout_road_crossing_rail_sw', 'boolean',  0],
            ['crossing_vee_sw', 'boolean',  0],
            ['main_road_crossing_rail_sw', 'boolean',  0],
            ['main_road_check_rail_sw', 'boolean',  0],
            ['main_road_stock_rail_sw', 'boolean',  0],
            ['alignment_byte_1', 'byte',  0],
            ['alignment_byte_2', 'byte',  0],
          ['rail_info', '<',  0],
          ['auto_restore_on_startup', 'boolean',  0],
          ['ask_restore_on_startup', 'boolean',  0],
          ['pre077_bgnd_flag', 'boolean',  0],
          ['alignment_byte_3', 'byte',  0],
          ['templot_version', 'integer',  0],
          ['file_format_code', 'integer',  0],
          ['gauge_index', 'integer',  0],
          ['gauge_exact', 'boolean',  0],
          ['gauge_custom', 'boolean',  0],
          ['proto_info', '>',  0],
            ['name_str_pi', 'string', 15],
            ['spare_str_pi', 'string', 75],
            ['scale_pi', 'extended',  0],
            ['gauge_pi', 'extended',  0],
            ['fw_pi', 'extended',  0],
            ['fwe_pi', 'extended',  0],
            ['xing_fl_pi', 'extended',  0],
            ['railtop_pi', 'extended',  0],
            ['trtscent_pi', 'extended',  0],
            ['trmscent_pi', 'extended',  0],
            ['retcent_pi', 'extended',  0],
            ['min_radius_pi', 'extended',  0],
            ['old_winglongs_pi', 'extended',  0],
            ['old_winglongl_pi', 'extended',  0],
            ['old_cklongs_pi', 'extended',  0],
            ['old_cklongm_pi', 'extended',  0],
            ['old_cklongl_pi', 'extended',  0],
            ['old_cklongxl_pi', 'extended',  0],
            ['tbwide_pi', 'extended',  0],
            ['slwide_pi', 'extended',  0],
            ['xtimbsp_pi', 'extended',  0],
            ['ftimbspmax_pi', 'extended',  0],
            ['tb_pi', 'extended',  0],
            ['mainside_ends_pi', 'boolean',  0],
            ['jt_slwide_pi', 'float',  0],
            ['alignment_byte_1', 'byte',  0],
            ['random_end_pi', 'extended',  0],
            ['timber_thick_pi', 'extended',  0],
            ['random_angle_pi', 'extended',  0],
            ['ck_ms_working1_pi', 'extended',  0],
            ['ck_ms_working2_pi', 'extended',  0],
            ['ck_ms_working3_pi', 'extended',  0],
            ['ck_ts_working_mod_pi', 'extended',  0],
            ['ck_ms_ext1_pi', 'extended',  0],
            ['ck_ms_ext2_pi', 'extended',  0],
            ['ck_ts_ext_mod_pi', 'extended',  0],
            ['wing_ms_reach1_pi', 'extended',  0],
            ['wing_ms_reach2_pi', 'extended',  0],
            ['wing_ts_reach_mod_pi', 'extended',  0],
            ['railbottom_pi', 'extended',  0],
            ['rail_height_pi', 'extended',  0],
            ['seat_thick_pi', 'extended',  0],
            ['old_tb_pi', 'extended',  0],
            ['rail_inclination_pi', 'extended',  0],
            ['foot_height_pi', 'extended',  0],
            ['chair_outlen_pi', 'extended',  0],
            ['chair_inlen_pi', 'extended',  0],
            ['chair_width_pi', 'extended',  0],
            ['chair_corner_pi', 'extended',  0],
            ['spare_byte1', 'byte',  0],
            ['spare_byte2', 'byte',  0],
            ['spare_byte3', 'byte',  0],
            ['spare_byte4', 'byte',  0],
            ['spare_byte5', 'byte',  0],
            ['alignment_byte_2', 'byte',  0],
          ['proto_info', '<',  0],
          ['railtop_inches', 'extended',  0],
          ['railbottom_inches', 'extended',  0],
          ['alignment_byte_4', 'byte',  0],
          ['alignment_byte_5', 'byte',  0],
          ['version_as_loaded', 'integer',  0],
          ['bgnd_code_077', 'integer',  0],
          ['print_mapping_colour', 'integer',  0],
          ['pad_marker_colour', 'integer',  0],
          ['use_print_mapping_colour', 'boolean',  0],
          ['use_pad_marker_colour', 'boolean',  0],
          ['spare_bool1', 'boolean',  0],
          ['spare_bool2', 'boolean',  0],
          ['spare_int2', 'integer',  0],
          ['grid_units_code', 'integer',  0],
          ['x_grid_spacing', 'extended',  0],
          ['y_grid_spacing', 'extended',  0],
          ['total_length_of_timbering', 'extended',  0],
          ['id_number', 'integer',  0],
          ['id_number_str', 'string', 7],
          ['spare_boolean1', 'boolean',  0],
          ['spare_boolean2', 'boolean',  0],
          ['transform_info', '>',  0],
            ['datum_y', 'extended',  0],
            ['x_go_limit', 'extended',  0],
            ['x_stop_limit', 'extended',  0],
            ['transforms_apply', 'boolean',  0],
            ['alignment_byte_1', 'byte',  0],
            ['x1_shift', 'extended',  0],
            ['y1_shift', 'extended',  0],
            ['k_shift', 'extended',  0],
            ['x2_shift', 'extended',  0],
            ['y2_shift', 'extended',  0],
            ['peg_pos', '>',  0],
              ['x', 'extended',  0],
              ['y', 'extended',  0],
            ['peg_pos', '<',  0],
            ['alignment_byte_2', 'byte',  0],
            ['alignment_byte_3', 'byte',  0],
            ['peg_point_code', 'integer',  0],
            ['peg_point_rail', 'integer',  0],
            ['mirror_on_x', 'boolean',  0],
            ['mirror_on_y', 'boolean',  0],
            ['alignment_byte_4', 'byte',  0],
            ['alignment_byte_5', 'byte',  0],
            ['spare_int1', 'integer',  0],
            ['spare_int2', 'integer',  0],
            ['spare_flag1', 'boolean',  0],
            ['spare_flag2', 'boolean',  0],
            ['spare_flag3', 'boolean',  0],
            ['spare_flag4', 'boolean',  0],
            ['notch_info', '>',  0],
              ['notch_x', 'extended',  0],
              ['notch_y', 'extended',  0],
              ['notch_k', 'extended',  0],
            ['notch_info', '<',  0],
            ['spare_str', 'string', 10],
            ['alignment_byte_6', 'byte',  0],
            ['alignment_byte_7', 'byte',  0],
            ['alignment_byte_8', 'byte',  0],
          ['transform_info', '<',  0],
          ['platform_trackbed_info', '>',  0],
            ['adjacent_edges_keep', 'boolean',  0],
            ['draw_ms_trackbed_edge_keep', 'boolean',  0],
            ['draw_ts_trackbed_edge_keep', 'boolean',  0],
            ['spare_bool1', 'boolean',  0],
            ['OUT_OF_USE_trackbed_width_ins_keep', 'extended',  0],
            ['draw_ts_platform_keep', 'boolean',  0],
            ['draw_ts_platform_start_edge_keep', 'boolean',  0],
            ['draw_ts_platform_end_edge_keep', 'boolean',  0],
            ['draw_ts_platform_rear_edge_keep', 'boolean',  0],
            ['platform_ts_front_edge_ins_keep', 'extended',  0],
            ['platform_ts_start_width_ins_keep', 'extended',  0],
            ['platform_ts_end_width_ins_keep', 'extended',  0],
            ['platform_ts_start_mm_keep', 'extended',  0],
            ['platform_ts_length_mm_keep', 'extended',  0],
            ['draw_ms_platform_keep', 'boolean',  0],
            ['draw_ms_platform_start_edge_keep', 'boolean',  0],
            ['draw_ms_platform_end_edge_keep', 'boolean',  0],
            ['draw_ms_platform_rear_edge_keep', 'boolean',  0],
            ['platform_ms_front_edge_ins_keep', 'extended',  0],
            ['platform_ms_start_width_ins_keep', 'extended',  0],
            ['platform_ms_end_width_ins_keep', 'extended',  0],
            ['platform_ms_start_mm_keep', 'extended',  0],
            ['platform_ms_length_mm_keep', 'extended',  0],
            ['OUT_OF_USE_cess_width_ins_keep', 'extended',  0],
            ['OUT_OF_USE_draw_trackbed_cess_edge_keep', 'boolean',  0],
            ['platform_ms_start_skew_mm_keep', 'extended',  0],
            ['platform_ms_end_skew_mm_keep', 'extended',  0],
            ['platform_ts_start_skew_mm_keep', 'extended',  0],
            ['platform_ts_end_skew_mm_keep', 'extended',  0],
            ['spare_bool2', 'boolean',  0],
            ['spare_bool3', 'boolean',  0],
            ['spare_bool4', 'boolean',  0],
            ['spare_bool5', 'boolean',  0],
            ['spare_bool6', 'boolean',  0],
            ['spare_bool7', 'boolean',  0],
            ['spare_bool8', 'boolean',  0],
            ['trackbed_ms_width_ins_keep', 'float',  0],
            ['trackbed_ts_width_ins_keep', 'float',  0],
            ['cess_ms_width_ins_keep', 'float',  0],
            ['cess_ts_width_ins_keep', 'float',  0],
            ['draw_ms_trackbed_cess_edge_keep', 'boolean',  0],
            ['draw_ts_trackbed_cess_edge_keep', 'boolean',  0],
            ['spare1', 'boolean',  0],
            ['spare2', 'boolean',  0],
            ['trackbed_ms_start_mm_keep', 'extended',  0],
            ['trackbed_ms_length_mm_keep', 'extended',  0],
            ['trackbed_ts_start_mm_keep', 'extended',  0],
            ['trackbed_ts_length_mm_keep', 'extended',  0],
          ['platform_trackbed_info', '<',  0],
          ['align_info', '>',  0],
            ['curving_flag', 'boolean',  0],
            ['trans_flag', 'boolean',  0],
            ['fixed_rad', 'extended',  0],
            ['trans_rad1', 'extended',  0],
            ['trans_rad2', 'extended',  0],
            ['trans_length', 'extended',  0],
            ['trans_start', 'extended',  0],
            ['rad_offset', 'extended',  0],
            ['alignment_byte_1', 'byte',  0],
            ['alignment_byte_2', 'byte',  0],
            ['tanh_kmax', 'double',  0],
            ['slewing_flag', 'boolean',  0],
            ['cl_only_flag', 'boolean',  0],
            ['slew_type', 'byte',  0],
            ['dummy_template_flag', 'boolean',  0],
            ['slew_start', 'extended',  0],
            ['slew_length', 'extended',  0],
            ['slew_amount', 'extended',  0],
            ['cl_options_code_int', 'integer',  0],
            ['cl_options_custom_offset_ext', 'extended',  0],
            ['reminder_flag', 'boolean',  0],
            ['reminder_colour', 'integer',  0],
            ['reminder_str', 'string', 200],
            ['spare_float1', 'extended',  0],
            ['spare_float2', 'extended',  0],
            ['spare_float3', 'extended',  0],
            ['spare_int', 'integer',  0],
          ['align_info', '<',  0],
          ['rail_type', 'integer',  0],
          ['fb_kludge_template_code', 'integer',  0],
          ['box_save_done', 'boolean',  0],
          ['uninclined_rails', 'boolean',  0],
          ['disable_f7_snap', 'boolean',  0],
          ['spare_bool4', 'boolean',  0],
          ['mod_text_x', 'extended',  0],
          ['mod_text_y', 'extended',  0],
          ['flatbottom_width', 'extended',  0],
          ['check_diffs', '>',  0],
            ['end_diff_mw', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_mw', '<',  0],
            ['end_diff_me', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_me', '<',  0],
            ['end_diff_mr', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_mr', '<',  0],
            ['end_diff_tw', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_tw', '<',  0],
            ['end_diff_te', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_te', '<',  0],
            ['end_diff_tr', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_tr', '<',  0],
            ['end_diff_mk', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_mk', '<',  0],
            ['end_diff_dk', '>',  0],
              ['len_diff', 'extended',  0],
              ['flr_diff', 'extended',  0],
              ['gap_diff', 'extended',  0],
              ['type_diff', 'byte',  0],
            ['end_diff_dk', '<',  0],
          ['check_diffs', '<',  0],
          ['retain_diffs_on_make_flag', 'boolean',  0],
          ['retain_diffs_on_mint_flag', 'boolean',  0],
          ['retain_entry_straight_on_make_flag', 'boolean',  0],
          ['retain_entry_straight_on_mint_flag', 'boolean',  0],
          ['retain_shoves_on_make_flag', 'boolean',  0],
          ['retain_shoves_on_mint_flag', 'boolean',  0],
          ['turnout_info1', '>',  0],
            ['plain_track_flag', 'boolean',  0],
            ['rolled_in_sleepered_flag', 'boolean',  0],
            ['front_timbers_flag', 'boolean',  0],
            ['approach_rails_only_flag', 'boolean',  0],
            ['hand', 'integer',  0],
            ['timbering_flag', 'boolean',  0],
            ['switch_timbers_flag', 'boolean',  0],
            ['closure_timbers_flag', 'boolean',  0],
            ['xing_timbers_flag', 'boolean',  0],
            ['exit_timbering', 'integer',  0],
            ['turnout_road_code', 'integer',  0],
            ['turnout_length', 'extended',  0],
            ['origin_to_toe', 'extended',  0],
            ['step_size', 'extended',  0],
            ['turnout_road_is_adjustable', 'boolean',  0],
            ['turnout_road_is_minimum', 'boolean',  0],
          ['turnout_info1', '<',  0],
        ['box_dims1', '<',  0],
      ['old_keep_dims1', '<',  0],
      ['old_keep_shoves', '>',  0],
        # ['shoves', '------> array[0-shovedim_c_048] of Told_shove 0
        ['shoves', 'h', 30*68],
      ['old_keep_shoves', '<',  0],
      ['old_keep_dims2', '>',  0],
        ['turnout_info2', '>',  0],
          ['switch_info', '>',  0],
            ['old_size', 'integer',  0],
            ['sw_name_str', 'string', 100],
            ['alignment_byte_1', 'byte',  0],
            ['alignment_byte_2', 'byte',  0],
            ['alignment_byte_3', 'byte',  0],
            ['sw_pattern', 'integer',  0],
            ['planing', 'extended',  0],
            ['planing_angle', 'extended',  0],
            ['switch_radius_inchormax', 'extended',  0],
            ['switch_rail', 'extended',  0],
            ['stock_rail', 'extended',  0],
            ['heel_lead_inches', 'extended',  0],
            ['heel_offset_inches', 'extended',  0],
            ['switch_front_inches', 'extended',  0],
            ['planing_radius', 'extended',  0],
            ['sleeper_j1', 'extended',  0],
            ['sleeper_j2', 'extended',  0],
            # ['timber_centres', '------> array[0-swtimbco_c] of x 0
            ['timber_centres', 'h', 43*xlen],
            ['group_code', 'integer',  0],
            ['size_code', 'integer',  0],
            ['joggle_depth', 'extended',  0],
            ['joggle_length', 'extended',  0],
            ['group_count', 'integer',  0],
            ['joggled_stock_rail', 'boolean',  0],
            ['alignment_byte_4', 'byte',  0],
            ['alignment_byte_5', 'byte',  0],
            ['alignment_byte_6', 'byte',  0],
            ['spare_int2', 'integer',  0],
            ['spare_int1', 'integer',  0],
            ['valid_data', 'boolean',  0],
            ['front_timbered', 'boolean',  0],
            ['num_bridge_chairs_main_rail', 'byte',  0],
            ['num_bridge_chairs_turnout_rail', 'byte',  0],
            ['fb_tip_offset', 'extended',  0],
            ['sleeper_j3', 'extended',  0],
            ['sleeper_j4', 'extended',  0],
            ['sleeper_j5', 'extended',  0],
            ['spare_float4', 'extended',  0],
            ['spare_float3', 'extended',  0],
            ['spare_float2', 'extended',  0],
            ['spare_float1', 'extended',  0],
            ['spare_str', 'string', 200],
            ['num_slide_chairs', 'byte',  0],
            ['num_block_slide_chairs', 'byte',  0],
            ['num_block_heel_chairs', 'byte',  0],
          ['switch_info', '<',  0],
          ['crossing_info', '>',  0],
            ['pattern', 'integer',  0],
            ['sl_mode', 'integer',  0],
            ['retcent_mode', 'integer',  0],
            ['k3n_unit_angle', 'extended',  0],
            ['fixed_st', 'extended',  0],
            ['spare_int3', 'integer',  0],
            ['hd_timbers_code', 'integer',  0],
            ['hd_vchecks_code', 'integer',  0],
            ['k_check_length_1', 'extended',  0],
            ['k_check_length_2', 'extended',  0],
            ['k_check_mod_ms', 'extended',  0],
            ['k_check_mod_ds', 'extended',  0],
            ['k_check_flare', 'extended',  0],
            ['curviform_timbering_keep', 'boolean',  0],
            ['alignment_byte_2', 'byte',  0],
            ['main_road_code', 'integer',  0],
            ['tandem_timber_code', 'integer',  0],
            ['blunt_nose_width', 'extended',  0],
            ['blunt_nose_to_timb', 'extended',  0],
            ['vee_joint_half_spacing', 'extended',  0],
            ['wing_joint_spacing', 'extended',  0],
            ['wing_timber_spacing', 'extended',  0],
            ['vee_timber_spacing', 'extended',  0],
            ['vee_joint_space_co1', 'byte',  0],
            ['vee_joint_space_co2', 'byte',  0],
            ['vee_joint_space_co3', 'byte',  0],
            ['vee_joint_space_co4', 'byte',  0],
            ['vee_joint_space_co5', 'byte',  0],
            ['vee_joint_space_co6', 'byte',  0],
            ['wing_joint_space_co1', 'byte',  0],
            ['wing_joint_space_co2', 'byte',  0],
            ['wing_joint_space_co3', 'byte',  0],
            ['wing_joint_space_co4', 'byte',  0],
            ['wing_joint_space_co5', 'byte',  0],
            ['wing_joint_space_co6', 'byte',  0],
            ['spare_flag1', 'boolean',  0],
            ['spare_flag2', 'boolean',  0],
            ['main_road_endx_infile', 'extended',  0],
            ['hdkn_unit_angle', 'extended',  0],
            ['check_flare_info_081', '>',  0],
              ['check_flare_ext_ms', 'extended',  0],
              ['check_flare_ext_ts', 'extended',  0],
              ['check_flare_work_ms', 'extended',  0],
              ['check_flare_work_ts', 'extended',  0],
              ['wing_flare_ms', 'extended',  0],
              ['wing_flare_ts', 'extended',  0],
              ['check_flare_k_ms', 'extended',  0],
              ['check_flare_k_ds', 'extended',  0],
              ['check_fwe_ext_ms', 'extended',  0],
              ['check_fwe_ext_ts', 'extended',  0],
              ['check_fwe_work_ms', 'extended',  0],
              ['check_fwe_work_ts', 'extended',  0],
              ['wing_fwe_ms', 'extended',  0],
              ['wing_fwe_ts', 'extended',  0],
              ['check_fwe_k_ms', 'extended',  0],
              ['check_fwe_k_ds', 'extended',  0],
            ['check_flare_info_081', '<',  0],
            ['k_custom_wing_long_keep', 'extended',  0],
            ['k_custom_point_long_keep', 'extended',  0],
            ['use_k_custom_wing_rails_keep', 'boolean',  0],
            ['use_k_custom_point_rails_keep', 'boolean',  0],
            ['spare_str', 'string', 10],
            ['alignment_byte_3', 'byte',  0],
          ['crossing_info', '<',  0],
          ['plain_track_info', '>',  0],
            ['pt_custom', 'boolean',  0],
            ['alignment_byte_1', 'byte',  0],
            ['alignment_byte_2', 'byte',  0],
            ['alignment_byte_3', 'byte',  0],
            ['list_index', 'integer',  0],
            ['rail_length', 'extended',  0],
            ['alignment_byte_4', 'byte',  0],
            ['alignment_byte_5', 'byte',  0],
            ['sleepers_per_length', 'integer',  0],
            # ['sleeper_centres', '------> array[0-psleep_c] of x 0
            ['sleeper_centres', 'h', 52*xlen],
            ['rail_joints_code', 'integer',  0],
            ['user_peg_rail', 'integer',  0],
            ['pt_spare_flag1', 'boolean',  0],
            ['pt_spare_flag2', 'boolean',  0],
            ['pt_spare_flag3', 'boolean',  0],
            ['user_peg_data_valid', 'boolean',  0],
            ['user_pegx', 'extended',  0],
            ['user_pegy', 'extended',  0],
            ['user_pegk', 'extended',  0],
            ['pt_spacing_name_str', 'string', 200],
            ['alignment_byte_6', 'byte',  0],
            ['pt_tb_rolling_percent', 'extended',  0],
            ['gaunt_sleeper_mod_inches', 'extended',  0],
            ['pt_spare_ext3', 'extended',  0],
            ['pt_spare_ext2', 'extended',  0],
            ['pt_spare_ext1', 'extended',  0],
            ['alignment_byte_7', 'byte',  0],
            ['alignment_byte_8', 'byte',  0],
          ['plain_track_info', '<',  0],
          ['diamond_auto_code', 'integer',  0],
          ['bonus_timber_count', 'integer',  0],
          ['equalizing_fixed_flag', 'boolean',  0],
          ['no_timbering_flag', 'boolean',  0],
          ['angled_on_flag', 'boolean',  0],
          ['chairing_flag', 'boolean',  0],
          ['start_draw_x', 'extended',  0],
          ['timber_length_inc', 'extended',  0],
          ['omit_switch_front_joints', 'boolean',  0],
          ['omit_switch_rail_joints', 'boolean',  0],
          ['omit_stock_rail_joints', 'boolean',  0],
          ['omit_wing_rail_joints', 'boolean',  0],
          ['omit_vee_rail_joints', 'boolean',  0],
          ['omit_k_crossing_stock_rail_joints', 'boolean',  0],
          ['spare_flag14', 'boolean',  0],
          ['spare_flag13', 'boolean',  0],
          ['spare_flag12', 'boolean',  0],
          ['diamond_switch_timbering_flag', 'boolean',  0],
          ['gaunt_flag', 'boolean',  0],
          ['diamond_proto_timbering_flag', 'boolean',  0],
          ['semi_diamond_flag', 'boolean',  0],
          ['diamond_fixed_flag', 'boolean',  0],
          ['hdk_check_rail_info', '>',  0],
            ['k_check_ms_1', 'extended',  0],
            ['k_check_ms_2', 'extended',  0],
            ['k_check_ds_1', 'extended',  0],
            ['k_check_ds_2', 'extended',  0],
          ['hdk_check_rail_info', '<',  0],
          ['vee_check_rail_info', '>',  0],
            ['v_check_ms_working1', 'extended',  0],
            ['v_check_ms_working2', 'extended',  0],
            ['v_check_ms_working3', 'extended',  0],
            ['v_check_ts_working1', 'extended',  0],
            ['v_check_ts_working2', 'extended',  0],
            ['v_check_ts_working3', 'extended',  0],
            ['v_check_ms_ext1', 'extended',  0],
            ['v_check_ms_ext2', 'extended',  0],
            ['v_check_ts_ext1', 'extended',  0],
            ['v_check_ts_ext2', 'extended',  0],
            ['v_wing_ms_reach1', 'extended',  0],
            ['v_wing_ms_reach2', 'extended',  0],
            ['v_wing_ts_reach1', 'extended',  0],
            ['v_wing_ts_reach2', 'extended',  0],
          ['vee_check_rail_info', '<',  0],
          ['turnout_road_endx_infile', 'extended',  0],
          ['template_type_str', 'string', 6],
          ['smallest_radius_stored', 'extended',  0],
          ['dpx_stored', 'extended',  0],
          ['ipx_stored', 'extended',  0],
          ['fpx_stored', 'extended',  0],
          ['gaunt_offset_inches', 'extended',  0],
          ['dxf_connector_0', 'boolean',  0],
          ['dxf_connector_t', 'boolean',  0],
          ['dxf_connector_9', 'boolean',  0],
        ['turnout_info2', '<',  0],
      ['old_keep_dims2', '<',  0],
    ['', '<',  0],

    ])