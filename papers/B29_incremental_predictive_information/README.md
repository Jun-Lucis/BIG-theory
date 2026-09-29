# BIG-B29 — Incremental Predictive Information Beyond Instantaneous Geometry

B29 tested whether retained history contributed prospective predictive information beyond instantaneous geometry in a response-readout setting.

## Terminal status

B29 closed **before B29.1 held-out evaluation**.

B29-P0 established a 36-case response-blind grid and a frozen 27-training / 9-held-out split. B29-P0R repaired only the separate calibration set and froze the numerical and gain/readability thresholds.

B29-T1 then evaluated the 27 training cases under the inherited gates. Only **18/27** were valid:

- relative-write (25^circ): all valid;
- relative-write (55^circ): all valid;
- relative-write (85^circ): all invalid under the frozen response-readability gate.

Terminal training status:

`T1_valid=False`

No held-out prediction set was frozen, no held-out post-response was evaluated, and B29.1 was never opened.

## Interpretation

This is **not** a predictive-performance failure of M0, M1, or M2. Those models were never validly trained under the frozen domain and no prospective held-out evaluation occurred.

The correct retained interpretation is:

> the frozen B29 training domain was not uniformly response-readable under the inherited response readout.

The concentration of unreadability in the (85^circ) relative-write stratum was hypothesis-generating only and motivated the later angular-response programme. It does not establish (85^circ) or (90^circ) as a physical constant.

See also: [B27–B36 later-phase status](../../docs/research_status_update_B27_B36.md).
