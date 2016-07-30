import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# get  a dense matrix rolling:

'''
lets cluster on only data from 2013!!!
'''
dense_2013 = master_merger_df[master_merger_df['pop'].notnull() ==True]
cols = [u'city',u'pop', u'total members',u'members (% of pop)',u'% growth 2013',u'members of largest group',u'cost_of_living_index_2013', u'rent_index_2013', u'groceries_index_2013', u'restaurant_price_index_2013', u'local_purchasing_power_index_2013']

dense_2013 = dense_2013[cols]
dense_2013= dense_2013[dense_2013['pop'].notnull()]
dense_2013.set_index('city', inplace=True)
#dense_test_df.drop('bea_2013', axis=1, inplace=True)
dense_2013.drop('boulder', axis=0, inplace=True)

'''
lets cluster on only data from 2014!!!
'''
dense_2014 = master_merger_df[master_merger_df['pop'].notnull() ==True]
cols = [u'city',u'pop', u'total members',u'members (% of pop)',u'% growth 2013',u'members of largest group',u'cost_of_living_index_2014', u'rent_index_2014', u'groceries_index_2014', u'restaurant_price_index_2014', u'local_purchasing_power_index_2014']

dense_2014 = dense_2014[cols]
dense_2014= dense_2014[dense_2014['pop'].notnull()]
dense_2014.set_index('city', inplace=True)
#dense_test_df.drop('bea_2013', axis=1, inplace=True)
#dense_2014.drop('boulder', axis=0, inplace=True)


X_2014 = dense_test_df.values
X_2014 = StandardScaler().fit_transform(X_2013)







mods = {'km3': KMeans(n_clusters=3, random_state=6, n_jobs =-2),
        'km4': KMeans(n_clusters=4,random_state=6, n_jobs =-2),
        'km5': KMeans(n_clusters=5,random_state=6, n_jobs =-2),
        'km6': KMeans(n_clusters=6, random_state=6, n_jobs =-2),
        'km7': KMeans(n_clusters=7,random_state=6, n_jobs =-2),
        'km8': KMeans(n_clusters=8, random_state=6, n_jobs =-2)
        }



X_2013 = dense_test_df.values
X_2013 = StandardScaler().fit_transform(X_2013)

pred_list = []
for name, mod in mods.items():
    temp_pred = mod.fit_predict(X_2013)
    pred_list.append(temp_pred)












#
# def plotter(results):
#     indices = np.arange(len(results))
#     print(results)
#     results = [[x[i] for x in results] for i in range(6)]
#     clf_names, score, recall, precision, training_time, test_time = results
#     training_time = np.array(training_time) / np.max(training_time)
#     test_time = np.array(test_time) / np.max(test_time)
#
#     plt.figure(figsize=(12, 8))
#     plt.title("Model Comparison")
#     plt.barh(indices + .1, precision, .1, label="precision", color='r')
#     #plt.barh(indices + .1, score, .1, label="accuracy", color='r')
#     plt.barh(indices, recall, .1, label="recall", color='g')
#     plt.barh(indices + .6, training_time, .1, label="training time", color='y')
#     plt.barh(indices + .6, test_time, .1, label="test time", color='b')
#     plt.yticks(())
#     plt.legend(loc='best')
#     plt.subplots_adjust(left=.25)
#     plt.subplots_adjust(top=.95)
#     plt.subplots_adjust(bottom=.05)
#
#     for i, c in zip(indices, clf_names):
#         plt.text(-.3, i, c)
#
# def benchmark(clf):
#     print('_' * 80)
#     print("Training: ")
#     print(clf)
#     t0 = time()
#     clf.fit(X_train, y_train)
#     train_time = time() - t0
#     print("train time: %0.3fs" % train_time)
#
#     t0 = time()
#     y_pred = clf.predict(X_test)
#     test_time = time() - t0
#     print("test time: %0.3fs" % test_time)
#
#     accuracy = metrics.accuracy_score(y_test, y_pred)
#     recall = metrics.recall_score(y_test, y_pred)
#     precision = metrics.precision_score(y_test, y_pred)
#     print("accuracy:   %0.3f" % accuracy)
#     print("recall: %0.3f" % recall)
#     print("precision: %0.3f" % precision)
#
#     if hasattr(clf, 'coef_'):
#         print("dimensionality: %d" % clf.coef_.shape[1])
#         print("density: %f" % density(clf.coef_))
#
#     print()
#     clf_descr = str(clf).split('(')[0]
#     return clf_descr, accuracy, recall, precision, train_time, test_time
#
# results = []
# for clf, name in (
#         #(RidgeClassifier(tol=1e-2, solver="lsqr"), "Ridge Classifier"),
#         #(Perceptron(n_iter=50), "Perceptron"),
#         #(PassiveAggressiveClassifier(n_iter=50), "Passive-Aggressive"),
#         #(KNeighborsClassifier(n_neighbors=10), "kNN"),
#         (RandomForestClassifier(n_estimators=5000), "Random forest"),
#         #(SGDClassifier(alpha=.0001, n_iter=50, penalty="elasticnet"), "SGDClassifier w/ elasticnet"),
#         #(NearestCentroid(), "NearestCentroid (aka Rocchio classifier)"),
#         #(MultinomialNB(alpha=.01), "Naive Bayes - Multinomial"),
#         #(BernoulliNB(alpha=.01), "Naive Bayes - Bernoulli")):
#         #(GradientBoostingClassifier(init=None, learning_rate=0.1, loss='deviance',
#           max_depth=3, max_features=None, max_leaf_nodes=None,
#           min_samples_leaf=1, min_samples_split=2,
#           min_weight_fraction_leaf=0.0, n_estimators=5000,
#           presort='auto', random_state=None, subsample=1.0, verbose=0,
#           warm_start=False), "GradientBoostingClassifier"),
#         #(AdaBoostClassifier(n_estimators=5000), "AdaBoostClassifier")):
#     print('=' * 80)
#     print(name)
#     results.append(benchmark(clf))
# plotter(results)
