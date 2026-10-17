import { readFileSync } from 'node:fs';

// Saved-table algebra only. No PDE integration or full residual uncertainty certification.
function verify(input) {
  const csv = text => text.trim().split(/\r?\n/).map(line => line.split(','));
  const q = csv(input.basis_csv_from_notebook).slice(1).map(row => row.slice(1).map(Number));
  const scale = csv(input.scale_recovery_csv_from_notebook).slice(1).map(row => Number(row[2]));
  const raw = input.path_start.map((x, i) => (input.path_end[i] - x) / scale[i]);
  const vq = Array.from({length: 4}, (_, j) => q.reduce((sum, row, i) => sum + row[j] * raw[i], 0));
  const vqNorm = Math.hypot(...vq), data = input.final_result;
  const table = csv(input.components_csv);
  const rows = table.slice(1).map(row => Object.fromEntries(table[0].map((key, i) => [key, Number(row[i])])));
  const norm = v => Math.hypot(...v);
  const dot = (a, b) => a.reduce((sum, x, i) => sum + x * b[i], 0);
  const checks = [];
  const check = (name, actual, expected, tolerance = 2e-12) => {
    const error = Math.abs(actual - expected);
    checks.push({name, actual, expected, absolute_error: error, tolerance,
      status: Number.isFinite(error) && error <= tolerance ? 'PASS' : 'FAIL'});
  };
  rows.forEach((x, i) => {
    check('DgDt_component_' + (i + 1), (x.g_Tplus - x.g_Tminus) / data.delta_T_total, x.DgDt_direct);
    check('transport_component_' + (i + 1), x.transport_direct / data.epsdot_direct, x.HVP_h2 * vqNorm);
    check('prediction_component_' + (i + 1), x.partial_T_g_fixed_5pt + x.transport_direct, x.prediction);
    check('residual_component_' + (i + 1), x.DgDt_direct - x.prediction, x.residual);
  });
  check('speed', (data.epsilon_plus - data.epsilon_minus) / data.delta_T_total, data.epsdot_direct);
  check('speed_bracket_scale', (data.root_width_minus + data.root_width_plus) / (2 * data.delta_T_total), data.epsdot_bracket_uncertainty_bound);
  check('residual_norm', norm(rows.map(x => x.residual)), data.residual_norm);
  check('relative_residual', norm(rows.map(x => x.residual)) / norm(rows.map(x => x.DgDt_direct)), data.relative_residual);
  check('root_DgDt_scale', vqNorm * norm(data.HVP_h2) * data.epsdot_bracket_uncertainty_bound, data.first_order_root_position_DgDt_uncertainty_bound);
  check('relative_root_scale', data.first_order_root_position_DgDt_uncertainty_bound / norm(data.DgDt_direct), data.relative_root_position_DgDt_uncertainty_bound);
  check('angle', Math.acos(dot(data.prediction, data.DgDt_direct) / (norm(data.prediction) * norm(data.DgDt_direct))) * 180 / Math.PI, data.prediction_observed_angle_deg, 2e-9);
  const a0 = data.HVP_h2.map(x => x * vqNorm), corners = [];
  for (const sm of [-1, 1]) for (const sp of [-1, 1]) {
    const dm = sm * data.root_width_minus / 2, dp = sp * data.root_width_plus / 2;
    const observedShift = a0.map(a => a * (dp - dm) / data.delta_T_total);
    const transportShift = a0.map(a => a * (dp - dm) / data.delta_T_total);
    corners.push({root_minus_shift: dm, root_plus_shift: dp,
      direct_shift_norm: norm(observedShift),
      predicted_transport_shift_norm: norm(transportShift),
      conditional_residual_shift_norm: norm(observedShift.map((x, i) => x - transportShift[i]))});
  }
  return {status: checks.every(x => x.status === 'PASS') ? 'PASS' : 'FAIL',
    scope: 'Independent E12 saved-table algebra only; not the pending whole-source verifier, not a PDE rerun, not residual uncertainty certification',
    comparison_count: checks.length, path_coordinate_direction: vq, path_coordinate_direction_norm: vqNorm,
    checks, conditional_shared_root_corners: corners,
    assumption: 'Endpoint gradient path sensitivities a_minus=a_plus=a0=||v_q|| HVP_h2. This assumption is diagnostic only; endpoint sensitivities were not enclosed.'};
}

const source = process.argv[2] || new URL('../../docs/B21_CP27_INTERIM/E12_Input_Snapshot.json', import.meta.url);
const result = verify(JSON.parse(readFileSync(source, 'utf8')));
process.stdout.write(JSON.stringify(result, null, 2) + '\n');
if (result.status !== 'PASS') process.exitCode = 1;
