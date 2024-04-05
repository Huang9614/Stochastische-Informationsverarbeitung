# Lecture 03 Wonham Filter

## 基础
- Bayes law in standard form
- Bayes law with extended conditioning
- 条件概率
- 扩展条件概率
- conditional independence
- Notation of system matrices and measurement matrices
- 状态估计的目标：基于输入输出重建HMM中的状态量

## 预测
- 预测系统状态：只需要time-homogeneous系统矩阵/传递矩阵和初始状态概率分布
  - P(x_3) = A^T * A^T * A^T * P(x_0)
  - 两种推导方式
- 预测测量信号：只需要time-homogeneous测量矩阵和状态分布
  - P(y_3) = sigma_x3 B(x3,y3) * ξ3(x3)
- 在实际预测中，假设目前在第m步，要预测第k步的状态量的分布
  - 从m+1步开始，仅有控制信号的更新，无测量信号的情况下，如何预测系统状态
  - ξ_k|1:m = A^T * ξ_k-1|1:m -> one-step transition matrix A^T -> one-step prediction
  - ξ_m+K|1:m = (A^K)^T * ξ_m|1:m -> K-step transition matrix -> K-step prediction

## 滤波
- 假设目前在第k步，为了能够滤波，应该也有k个测量以及k-1个控制信号
- Idea：在有了y1:k-1 和 u0:k-1 的基础上，进行了one-step prediction，得到了（Prior） P(xk = i|y1:k-1,u0:k-1)；现在，又有了新的测量信号（Likelihood） yk = j：P(yk = j|xk = i)，从而可以得到滤波后的状态分布（Posterior）：P(xk = i|y1:k, u0:k-1)；也就是说，当我们在 xk = i 的基础上，测量得到了值为 j 的yk时，我们可以更新 xk = i 的概率； yk = j 是来自于测量， 而xk = i是来自于上一步；当我们想要更新 xk 时，就得对其可取的所有数值都进行更新，也就是如果有N个值，那么我们只要做N次测量，得到 P(yk = j | xk = 1) ... P(yk = j | xk = N)，而所有的j都取决于当时所在的状态 xk的取值，以及测量矩阵，因此，yk的取值是随机的，不需要loop over yk的所有可选值
  - `Q: `是否需要作N次测量？ Wann kann man mit 1D-Messung auch auf einen 3D-Zustand schliessen? 
- 


