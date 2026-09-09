# The Coma Cluster Distance Audit

An independent astrophysics data-analysis project investigating how the choice of redshift-independent distance indicator affects a cluster-scale estimate of the Hubble constant for the Coma Cluster.

## Research question

**How does the choice of redshift-independent distance indicator affect a cluster-scale estimate of the Hubble constant for the Coma Cluster?**

## Main finding

Using the median of ten listed Coma Cluster distance records as a descriptive summary gives an implied cluster-scale value of approximately **69.2 km/s/Mpc**, while the individual implied values span approximately **50.0–93.6 km/s/Mpc**.

This is **not presented as a precision measurement of H₀**. The records use heterogeneous distance indicators, some share references, and the published distances are not necessarily homogenized onto a common calibration zero point.

## Project structure

- [`version-1/`](version-1/) — earlier analysis stage, preserved for methodological history.
- [`version-2/`](version-2/) — refined and reproducible analysis.
  - [`data/`](version-2/data/) — cleaned Coma distance records.
  - [`analysis/`](version-2/analysis/) — Python analysis.
  - [`figures/`](version-2/figures/) — analysis figures in SVG format for direct browser viewing.
  - [`results/`](version-2/results/) — summary statistics.
  - [`references/`](version-2/references/) — source references.
  - [`report/`](version-2/report/) — report information and reproducibility notes.
- [`TESTING-HUBBLE-LAW. BY VEDANT.pdf`](TESTING-HUBBLE-LAW.%20BY%20VEDANT.pdf) — separate Hubble-law galaxy analysis project.

## Reproducibility

The Version 2 calculation uses the NED Coma fiducial velocity of approximately 7194 km/s and computes each implied value as:

`H₀ = v / D`

Where a published distance-modulus uncertainty is available, it is propagated to distance and then to the implied H₀ uncertainty. Missing uncertainties are left unreported rather than invented.

## Scientific scope

This is a focused case study, not a claim to have measured the universal Hubble constant or resolved the Hubble tension. Its purpose is to examine how measurement method, calibration history, dependence, and uncertainty affect an astronomical inference.

## Author

**Vedant Kushwaha**  
Integrated B.Sc.–M.Sc. Applied Statistics  
Delhi Technological University  
2026
