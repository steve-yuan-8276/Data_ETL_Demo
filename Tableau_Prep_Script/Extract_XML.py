import pandas as pd
import xml.etree.ElementTree as ET

def parse_reference(DataFrame):
    """
    解析XML数据并提取reference值。
    
    参数:
    DataFrame: pandas DataFrame, 包含XML数据的DataFrame
    
    返回:
    pandas DataFrame, 包含解析出的reference值
    """
    references = []
    
    for xml_str in DataFrame['customer_OuterXML']:
        try:
            root = ET.fromstring(xml_str)
            ref = root.find('reference')
            references.append(ref.text if ref is not None else '')
        except:
            references.append('')
    
    return pd.DataFrame({
        'reference': references
    })

def get_output_schema():       
    """
    定义输出的 Schema 格式。
    
    返回:
    pandas DataFrame, 指定输出列的数据类型
    """
    return pd.DataFrame({
        'reference': prep_string()
    })