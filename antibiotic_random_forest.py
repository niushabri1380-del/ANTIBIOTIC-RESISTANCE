# Antibiotic Resistance Prediction — Random Forest
# Author: Niusha Bagheri
# Timeframe: 2024
#
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, precision_recall_curve, confusion_matrix, ConfusionMatrixDisplay

DATA_PATH = "data/antibiotic_resistance_clinical_isolates_2024.csv"
OUT_DIR = "outputs"

df = pd.read_csv(DATA_PATH)
X = df.drop(columns=["Resistant"])
y = df["Resistant"]

cat_cols = ["Species","Sample_Type","Ward"]
num_cols = [c for c in X.columns if c not in cat_cols]

preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ("num", "passthrough", num_cols)
])

model = Pipeline([
    ("prep", preprocess),
    ("clf", RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

model.fit(X_train, y_train)
y_score = model.predict_proba(X_test)[:,1]
y_pred  = model.predict(X_test)

# ROC
fpr, tpr, _ = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label=f"AUC={roc_auc:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate")
plt.title("ROC Curve — Random Forest")
plt.legend()
plt.savefig(f"{OUT_DIR}/roc_rf.png", dpi=200, bbox_inches="tight")
plt.close()

# PR
precision, recall, _ = precision_recall_curve(y_test, y_score)
plt.figure()
plt.plot(recall, precision)
plt.xlabel("Recall"); plt.ylabel("Precision")
plt.title("Precision–Recall — Random Forest")
plt.savefig(f"{OUT_DIR}/pr_rf.png", dpi=200, bbox_inches="tight")
plt.close()

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=["Susceptible","Resistant"])
disp.plot(values_format="d")
plt.title("Confusion Matrix — Random Forest")
plt.savefig(f"{OUT_DIR}/confusion_matrix_rf.png", dpi=200, bbox_inches="tight")
plt.close()

print("Done ✅")
print(f"AUC (ROC): {roc_auc:.3f}")