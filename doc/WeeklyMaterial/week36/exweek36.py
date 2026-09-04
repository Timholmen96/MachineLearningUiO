import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.utils import resample


rng = np.random.default_rng(2026)
n = 100
x = rng.standard_normal(n)
y = 3 * x**2 + rng.standard_normal(n)  

# degree 6 po.reg with ridge
# Compute CV MSE
# Find optimal lambda

nlambdas = 100
lambdas = np.logspace(-3, 5, nlambdas)

def ridge_kfold(k):
    kfold = KFold(n_splits=k, shuffle=True, random_state=2026)
    poly = PolynomialFeatures(degree=6)
    score_KFold = np.zeros((nlambdas, k))

    for i, lmb in enumerate(lambdas):
        for j, (train_inds, test_inds) in enumerate(kfold.split(x)):
            xtrain, ytrain = x[train_inds], y[train_inds]
            xtest, ytest = x[test_inds], y[test_inds]

            Xtrain = poly.fit_transform(xtrain[:, np.newaxis])
            Xtest = poly.transform(xtest[:, np.newaxis])
            scaler = StandardScaler().fit(Xtrain) # fitted on training folds only

            ridge = Ridge(alpha=lmb)
            ridge.fit(scaler.transform(Xtrain), ytrain)
            ypred = ridge.predict(scaler.transform(Xtest))
            score_KFold[i, j] = np.mean((ypred - ytest)**2)
        mse_KFold = np.mean(score_KFold, axis = 1)
    return mse_KFold, score_KFold

mse_KFold_5, score_KFold_5 = ridge_kfold(5)
mse_KFold_10, score_KFold_10 = ridge_kfold(10)
#mse_KFold_n, score_KFold_n = ridge_kfold(n)

best1 = np.argmin(mse_KFold_5)
best2 = np.argmin(mse_KFold_10)
#best3 = np.argmin(mse_KFold_n)
print(f"k = 5; best lambda {lambdas[best1]:.4g}, MSE KFold {mse_KFold_5[best1]:.4f}")
print(f"k = 10; best lambda {lambdas[best2]:.4g}, MSE KFold {mse_KFold_10[best2]:.4f}")
#print(f"K = n, leave one out; best lambda {lambdas[best3]:.4g}, MSE KFold {mse_KFold_n[best3]:.4f}")

"Ser på k = 10"
std_KFold = np.std(score_KFold_10, axis=1, ddof=1)
standard_error = std_KFold / np.sqrt(10)
"Standardavvik viser hvor mye MSE varierer mellom folds"
"Standardfeil viser usikkerheten i gjennomsnittlig MSE"


plt.errorbar(lambdas,mse_KFold_10,yerr=std_KFold,marker="o",capsize=4)
plt.xscale("log")
plt.xlabel("Lambda")
plt.ylabel("Cross-validated MSE")
plt.show()

