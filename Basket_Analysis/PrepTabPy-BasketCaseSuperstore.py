import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def createtable(DataFrame):
    """
    生成频繁项集并计算关联规则。
    
    参数:
    DataFrame: pandas DataFrame, one-hot 编码格式的事务数据
    
    返回:
    pandas DataFrame, 包含关联规则的前件、后件、提升度（lift）、置信度（confidence）、支持度（support）
    """
    # 确保数据是布尔类型，避免 DeprecationWarning
    DataFrame = DataFrame.astype(bool)

    # 计算频繁项集
    frequent_itemsets = apriori(DataFrame, min_support=0.10, use_colnames=True)

    # 计算关联规则
    rules = association_rules(frequent_itemsets, metric='lift')

    # 格式化规则的前件和后件
    rules["antecedents"] = rules["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
    rules["consequents"] = rules["consequents"].apply(lambda x: ', '.join(list(x))).astype("unicode")

    return rules[["antecedents", "consequents", "lift", "confidence", "support"]]

def get_output_schema():       
    """
    定义输出的 Schema 格式。
    
    返回:
    pandas DataFrame, 指定每列的数据类型
    """
    return pd.DataFrame({
        'antecedents': prep_string(),
        'consequents': prep_string(),
        'lift': prep_decimal(),
        'confidence': prep_decimal(),
        'support': prep_decimal(),
    })
