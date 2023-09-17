import numpy as np

def add_noise(data, epsilon, sensitivity):
    """
    使用差分隐私向数据添加噪声
    Args:
        data: 原始数据
        epsilon: 隐私预算，控制噪声的强度
        sensitivity: 数据的灵敏度，即数据在单个记录上的最大改变量
    Returns:
        加噪后的数据
    """
    # 计算噪声参数
    beta = sensitivity / epsilon
    
    # 对每个数据点添加拉普拉斯噪声
    noisy_data = np.random.laplace(0, beta, len(data)) + data
    
    return noisy_data

# 示例数据
data = np.array([1.2, 3.4, 2.1, 5.6, 4.3])

# 添加噪声
epsilon = 1.0  # 隐私预算
sensitivity = 1.0  # 数据灵敏度
noisy_data = add_noise(data, epsilon, sensitivity)

# 打印原始数据和加噪后的数据
print("原始数据:", data)
print("加噪后的数据:", noisy_data)