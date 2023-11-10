import json
import os
import requests
import openpyxl


# 通讯模块
def get_qq_info(qq_number):
    global name, sign, age, gender, country, province, city, clike, level, email
    # 构造URL
    url = f"https://api.kit9.cn/api/qq_material/api.php?qq={qq_number}"

    # 发送GET请求
    response = requests.get(url)

    # 检查响应状态码，确保请求成功
    if response.status_code == 200:
        # 解析响应数据（如果需要）
        getdata = response.json()
        # 在这里处理数据...
        # 直接访问字典中的数据
        name = getdata['data']['name']
        sign = getdata['data']['sign']
        age = getdata['data']['age']
        gender = getdata['data']['gender']
        country = getdata['data']['country']
        province = getdata['data']['province']
        city = getdata['data']['city']
        clike = getdata['data']['clike']
        level = getdata['data']['level']
        email = getdata['data']['email']
        imgurl = getdata['data']['imgurl']
        qzoneimgurl = getdata['data']['qzoneimgurl']

        # 返回结果
        return {
            'name': name,
            'sign': sign,
            'age': age,
            'gender': gender,
            'country': country,
            'province': province,
            'city': city,
            'clike': clike,
            'level': level,
            'email': email,
            'imgurl': imgurl,
            'qzoneimgurl': qzoneimgurl,
        }
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None

# 通讯模块TXT模块
def findtext():
    # 设定你想要检查的目录路径
    directory_path = os.getcwd()
    # 检查是否有名为"qq.txt"的文件
    file_name = "qq.txt"
    file_path = os.path.join(directory_path, file_name)
    if os.path.exists(file_path):
        print(f"找到文件 {file_name}")
    else:
        print(f"没有找到文件 {file_name}, 现在创建一个新的。")
        with open(file_path, 'w') as f:
            f.write('1919103034')

# 表格模块
def findexcel():
    filename = "example.xlsx"

    if os.path.exists(filename):
        print("表格文件存在")
        # 加载现有的工作簿
        workbook = openpyxl.load_workbook('example.xlsx')
        # 选择活动工作表
        sheet = workbook.active
        print(name)

        # 添加新的数据行
        sheet.append([selected_line,name, sign, age, gender, country, province, city, clike, level, email])

        # 保存工作簿到文件，这时不会覆盖现有数据，而是将新数据添加到工作簿中
        workbook.save("example.xlsx")

    else:
        print("表格文件不存在")
        # 创建一个新的工作簿
        workbook = openpyxl.Workbook()
        # 选择活动工作表
        sheet = workbook.active

        # 添加标题行
        sheet.append(["账户", "名字", "签名","年龄","性别","国家","省份","城市","点赞","等级","邮件"])

        # 保存工作簿到文件
        workbook.save("example.xlsx")


def readline():
    global selected_line
    n = 1  # 指定要读取的行数
    total_lines = sum(1 for _ in open('qq.txt', 'r'))  # 获取文件总行数

    with open('qq.txt', 'r') as file:
        while n <= 1000:
            # 获取指定行数的文本内容
            selected_line = file.readline()
            get_qq_info(selected_line)
            findexcel()
            print(selected_line)
            n += 1

findtext()
readline()
