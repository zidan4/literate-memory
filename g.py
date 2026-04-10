from sklearn.tree import export_graphviz

export_graphviz(
  tree_clf,
  out_file="iris_tree.dot",
  feature_names=["petal length (cm)", "petal width (cm)"],
  class_names=iris.target_names,
  rounded=True,
  filled=True
)
