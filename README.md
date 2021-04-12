# Final-Project

## HR Analytics-for-Employee-Promotion-Prediction
A Final Project for Purwadhika Data Scientist Course 

Pada repository ini dilakukan eksplorasi data untuk dapat memperdiksi Promosi karyawan.
Berikut link dataset : [HR_Analytics_Classification | Kaggle](https://www.kaggle.com/bhrt97/hr-analytics-classification)

### Dataset
Didalam dataset ini terdapat 13 kolom yang digunakan sebagai feature dan target.

Feature-feature:

1. **Department** : Data kategorikal yang merepresentasikan deparment karyawan bekerja dengan unique value ; `Sales & Marketing`, `Operations`, `Technology`, `Analytics`,`R&D`, `Procurement`, `Finance`, `HR`, `Legal`. Total dari unique value department = 9.
2. **Region** : Data kategorikal yang merepresentasikan region karyawan bekerja dengan total unique value = 34, `region_1 s/d region_34`
3 **Education** : Data kategorikal yang merepresentasikan education karyawan dengan total unique value = 3, yaitu ; `Bachelor's`, `Master's & above`,`Below Secondary`.
4. **Gender** : Data kategorikal yang merepresentasikan gender karyawan dengan total unique value = 2, yaitu ; `m` untuk Male, `f` untuk Female.
5. **Recruitment Channel** : Data kategorikal yang merepresentasikan proses rekrumen karyawan dengan total unique value = 3, yaitu ; `sourcing`, `referred` dan `other`
6. **No Of Trainings** : Data numerikal yang merepresentasikan seberapa banyak karyawan mengikuti training dengan total unique value = 10, yaitu ; `1 s/d 10`
7. **Age** : Data numerikal yang merepresentasikan usia karyawan dengan total unique value = 41, yaitu ; range antara `21 s/d 60`.
8. **Previous Year Rating** : Data numerikal yang merepresentasikan rating karyawan pada tahun sebelumnya dengan total unique value = 5, yaitu ; range antara `1 s/d 5`
9. **Length of Service** : Data numerikal yang merepresentasikan seberapa lama karyawan bekerja di perusahaan dengan total unique value = 35, yaitu ; range antara `1 s/d 37`
10. **KPI > 80%** : Data kategorikal yang merepresentasikan nilai KPI karyawan diatas 80% bekerja di perusahaan dengan total unique value = 2, yaitu ; `0` untuk dibawah 80%, sedangkan `1` diatas 80%.
11. **Awards Won** : Data kategorikal yang merepresentasikan karyawan telah mendapatkan awards selama bekerja di perusahaan dengan total unique value = 2, yaitu ; `0` untuk karyawan belum pernah menang awards, sedangkan `1` untuk yang mendapatkan award.
12. **Average Training Score** :  Data numerikal yang merepresentasikan nilai rata-rata karyawan ketika mengikuti training di perusahaan dengan total unique value = 61, yaitu ; range antara `44 s/d 99`

Target :

13. **Is Promoted** : Target dari prediksi apakah karyawan mendapatkan nilai 1 yang merepresentasikan di Promosikan atau tidak.

Step yang dilakukan untuk melakukan Prediksi:
1. Exploratory data analysis
2. Preprocessing. Which mainly about handling missing value
3. Model selections. The models used are LogReg, DecisionTree, RandomForest, KNN, AdaBoost, XGBoost, GradBoost.
4. Deployment with flask.


## Model Selection Results

Model terbaik yang ditentukan adalah Logistic Regresi dengan nilai Accurary 76% dan Nilai Recall 80%.


Kemudian dilakukan Hyperparameter tunning

> {'model__C': 0.1, 'model__random_state': 1212, 'model__solver': 'newton-cg'}

Proses tunning mendapatkan best score 82% dengan nilai recall 80%

## Dashboard

Flask was used to create the dashboard.

