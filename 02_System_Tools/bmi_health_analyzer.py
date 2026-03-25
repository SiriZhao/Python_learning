def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
    """
    计算 BMI（身体质量指数）

    参数:
        weight_kg (float) : 体重（千克）
        height_cm (float) : 身高（厘米）

    返回值:
        包含 bmi 数值和健康分类的字典
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("体重和身高必须为正数")

    bmi = weight_kg / (height_cm / 100) ** 2  

    if bmi < 18.5:
        category = "偏瘦"
    elif bmi < 24.0:
        category = "正常"
    elif bmi < 28.0:
        category = "超重"
    else:
        category = "肥胖"

    return {"bmi": round(bmi, 2), "category": category}


if __name__ == "__main__":
    try:
        weight = float(input("请输入体重（千克）："))
        height = float(input("请输入身高（厘米）："))

        result = calculate_bmi(weight_kg=weight, height_cm=height)  
        print(f"\nBMI：{result['bmi']}  → {result['category']}")
    except ValueError:
        print("输入有误，请输入有效的数字！")
