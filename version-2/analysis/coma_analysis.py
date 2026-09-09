import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

VELOCITY_KMS = 7194
VELOCITY_ERROR_KMS = 19

df = pd.read_csv("../data/coma_distance_records.csv")
df["implied_H0"] = VELOCITY_KMS / df["distance_mpc"]

mask = df["mu_error"].notna()
df.loc[mask, "distance_sigma_mpc"] = (
    df.loc[mask, "distance_mpc"] * np.log(10) / 5 * df.loc[mask, "mu_error"]
)
df.loc[mask, "H0_sigma"] = (
    df.loc[mask, "implied_H0"] *
    np.sqrt((VELOCITY_ERROR_KMS/VELOCITY_KMS)**2 +
            (df.loc[mask, "distance_sigma_mpc"]/df.loc[mask, "distance_mpc"])**2)
)

print(df[["method","distance_mpc","implied_H0","H0_sigma"]])
print("Mean:", df.implied_H0.mean())
print("Median:", df.implied_H0.median())
print("SD of distance:", df.distance_mpc.std())
print("CV (%):", 100*df.distance_mpc.std()/df.distance_mpc.mean())

plt.scatter(df.distance_mpc, df.implied_H0)
plt.xlabel("Distance (Mpc)")
plt.ylabel("Implied H0 (km/s/Mpc)")
plt.title("Coma Cluster: Distance versus Implied H0")
plt.tight_layout()
plt.savefig("../figures/distance_vs_implied_H0.png", dpi=180)
plt.show()
