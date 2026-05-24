import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score



df = pd.read_csv("../dataset/datasetbmi.csv")



def bmi_category(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    else:
        return "Obesitas"

df['Category'] = df['Bmi'].apply(bmi_category)



X = df[['Age', 'Height', 'Weight', 'Bmi']]
y = df['Category']



scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)



X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)



classifier = RandomForestClassifier(random_state=42)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy :", accuracy)


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(X_scaled)



joblib.dump(classifier, "../model/classifier.pkl")
joblib.dump(kmeans, "../model/kmeans.pkl")
joblib.dump(scaler, "../model/scaler.pkl")

print("Model berhasil disimpan")