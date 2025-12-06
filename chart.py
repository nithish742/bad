import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------
# 1. Generate synthetic data
# ------------------------------
np.random.seed(42)

data = pd.DataFrame({
    "Channel": np.repeat(["Email", "Chat", "Phone", "Social Media"], 200),
    "Response_Time_Minutes": np.concatenate([
        np.random.normal(45, 10, 200),   # Email
        np.random.normal(5, 2, 200),     # Chat
        np.random.normal(20, 5, 200),    # Phone
        np.random.normal(60, 15, 200)    # Social Media
    ])
})

# ------------------------------
# 2. Apply Seaborn styling
# ------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ------------------------------
# 3. Create violinplot
# ------------------------------
plt.figure(figsize=(8, 8))   # 8x8 inches at 64 dpi = 512x512 px

sns.violinplot(
    data=data,
    x="Channel",
    y="Response_Time_Minutes",
    palette="Set2"
)

plt.title("Customer Support Response Time Distribution")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (Minutes)")

# ------------------------------
# 4. Save as 512 × 512
# ------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
