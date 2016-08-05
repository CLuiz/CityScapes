
library(ggplot2)

# reads in a dense data set and outputs a dendrogram
data <- data.frame(read.csv('data/dense_test_set.csv'))
cluster_data <- colnames(data[-1])
cluster_matrix <- scale(data[,cluster_data])
cluster_center <- attr(cluster_matrix, "scaled:center")
cluster_scale <- attr(cluster_matrix, 'scaled:scale')
d <- dist(cluster_matrix, method ='euclidean')
cfit <-hclust(d, method='ward') 
plot(cfit, labels=data$city)
rect.hclust(cfit, k=8)

# pca via singular value decomposition
groups <- cutree(cfit, k=5)
princ <- prcomp(cluster_matrix)
nComp <- 2
project <- predict(princ, newdata=cluster_matrix)[,1:nComp]

pca_clusters <- cbind(as.data.frame(project),
                     cluster=as.factor(groups),
                      city=data$city)
ggplot(pca_clusters, aes(x=PC1, y=PC2)) +
  geom_point(aes(shape=cluster)) +
  geom_text(aes(label=city,),
            hjust=0, vjust=1) +
  xlim(c(-.2, .5)) +
  ylim(c(-.125, .6))

