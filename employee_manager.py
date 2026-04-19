# 【一】定义功能菜单
menu = '''
************** 功能菜单 ************** 
              1.用户注册
              2.用户登陆
              3.添加用户
              4.查看所有用户
              5.查看指定用户
              6.删除指定用户
              7.删除所有用户
              8.修改指定用户信息
              9.退出
************** 功能菜单 ************** 
'''

# 【二】分析流程
# 每一个工作的流程和主流程
# 【1】声明数据存储方式
# 【2】起整体逻辑
# 【3】分化每一个功能

# 以字典存储用户数据
'''
{
    "username": {
        "username": "username",
        "password": "password",
        "role": "role",
        "age": "age",
        "gender": "gender",
        "hobby": "hobby",
    }
}
'''
user_data = {
    "dream_01": {
        "username": "dream",
        "password": "521",
        "role": "admin",
        "user_id": "00001",
        "age": 18,
        "gender": "male",
        "hobby": ["music", "run"],
    }
}
login_dict = {
    "username": None,
    "role": None
}
while True:
    # 【1】打印功能菜单
    print(menu)
    # 【2】让用户输入功能ID
    func_id = input("请输入功能ID :>>>> ").strip()
    if not func_id.isdigit():
        print(f"当前功能ID非法!")
        continue
    func_id = int(func_id)
    if func_id not in list(range(1, 10)):
        print(f"当前功能ID不存在!")
        continue

    # 【3】分化功能
    if func_id == 1:
        print(f"欢迎来到注册功能!")
        # （1）让用户输入用户名和密码
        username = input("请输入用户名 :>>>> ").strip()
        password = input("请输入密码 :>>>> ").strip()
        if username in user_data:
            print(f"当前用户已存在,请先登录!")
            continue
        # （2）用户不存在则继续注册
        if username == "dream" and password == "521":
            role = "admin"
        else:
            role = "user"
        user_data[username] = {
            "username": username,
            "password": password,
            "role": role,
            "user_id": None,
            "age": None,
            "gender": None,
            "hobby": [],
        }
        print(f"当前用户 {username} 注册成功!")
    elif func_id == 2:
        print(f"欢迎来到登陆功能!")
        # （1）让用户输入用户名和密码
        username = input("请输入用户名 :>>>> ").strip()
        password = input("请输入密码 :>>>> ").strip()
        user_detail = user_data.get(username)
        if not user_detail:
            print(f"当前用户不存在,请先注册!")
            continue
        # （2）用户存在则继续登陆
        if password != user_detail.get("password"):
            print(f"当前密码错误,请重新输入!")
            continue
        login_dict["username"] = username
        login_dict["role"] = user_detail.get("role")
        if user_detail.get("role") == "admin":
            role = "管理员"
        else:
            role = "用户"
        print(f"欢迎当前 {role} 用户 {username} 登陆成功!")
    elif func_id == 3:
        print(f"欢迎来到添加用户功能!")
        # 先校验当前用户是够是管理员
        if login_dict.get("role") != "admin":
            print("当前用户不是管理员,没有权限访问该功能!")
            continue
        # 管理员才能添加用户信息
        while True:
            # 实时更新当前用户ID列表
            user_id_list = []
            for username, user_detail in user_data.items():
                user_id = user_detail.get("user_id")
                user_id_list.append(user_id)
            username = input("请输入用户名 :>>>> ").strip()
            if username in user_data:
                print("当前用户名已存在,请重新输入!")
                continue
            password = input("请输入密码 :>>>> ").strip()
            role = input("请输入用户角色(1 admin / 0 user) :>>>> ").strip()
            if role == "1":
                role = "admin"
            elif role == "0":
                role = "user"
            else:
                print("当前角色输入错误,请重新输入!")
            age = input("请输入用户年龄 :>>>>").strip()
            if not age.isdigit():
                print(f"当前年龄非法")
                continue
            age = int(age)
            if age < 0 or age > 120:
                print(f"当前年龄非法，不能是非人类!")
                continue
            user_id = input("请输入用户ID :>>>>").strip()
            user_id = user_id.zfill(5)
            if user_id in user_id_list:
                print(f"当前用户ID {user_id} 已经被使用，请重新输入!")
                continue
            gender = input("请输入用户性别(0 女 / 1 男) :>>>>").strip()
            if gender == "0":
                gender = "女"
            elif gender == "1":
                gender = "男"
            else:
                print(f"不合法的性别!重新输入！")
                continue
            hobby_list = []
            while True:
                hobby = input("请输入用户爱好(输入q退出) :>>>>").strip()
                if hobby == "q":
                    break
                else:
                    if hobby in hobby_list:
                        print(f"当前爱好已存在,请重新输入!")
                        continue
                    else:
                        hobby_list.append(hobby)
            user_data[username] = {
                "username": username,
                "password": password,
                "role": role,
                "user_id": user_id,
                "age": age,
                "gender": gender,
                "hobby": hobby_list,
            }
            print(f"当前用户 {username} 信息添加成功!")
            continue_choice = input("请选择是否继续添加用户信息(y/n) :>>>> ")
            if continue_choice == "y":
                continue
            else:
                print(f"当前功能已退出！")
                break
    elif func_id == 4:
        print(f"欢迎来到查看所有用户功能!")
        for username, user_info in user_data.items():
            role = user_info.get("role")
            if role == "admin":
                role = "管理员"
            else:
                role = "普通用户"
            print(f"""
        ################# 当前用户 {username} 信息如下 ################# 
                            用户名 :>>>> {username}
                            用户ID :>>>> {user_info.get("user_id")}
                            权限   :>>>> {role}
                            年龄   :>>>> {user_info.get("age")}
                            性别   :>>>> {user_info.get("gender")}
                            爱好   :>>>> {', '.join(user_info.get("hobby"))}
        ################# 当前用户 {username} 信息如上 ################# 
            """)
    elif func_id == 5:
        print(f"欢迎来到查看指定用户功能!")
        # 实时更新当前用户ID列表
        user_id_dict = {}
        for username, user_detail in user_data.items():
            user_id = user_detail.get("user_id")
            print(f"当前用户ID :>>>> {user_id} 用户名 :>>>> {username}")
            user_id_dict[user_id] = username
        user_id_input = input("请输入查看用户的指定ID :>>>> ").strip()
        if user_id_input not in user_id_dict.keys():
            print(f"当前用户ID不存在!")
            continue
        username = user_id_dict[user_id_input]
        user_info = user_data.get(username)
        role = user_info.get("role")
        if role == "admin":
            role = "管理员"
        else:
            role = "普通用户"
        print(f"""
        ################# 当前用户 {username} 信息如下 ################# 
                            用户名 :>>>> {username}
                            用户ID :>>>> {user_info.get("user_id")}
                            权限   :>>>> {role}
                            年龄   :>>>> {user_info.get("age")}
                            性别   :>>>> {user_info.get("gender")}
                            爱好   :>>>> {', '.join(user_info.get("hobby"))}
        ################# 当前用户 {username} 信息如上 ################# 
            """)

    elif func_id == 6:
        print(f"欢迎来到删除指定用户功能!")
        # 实时更新当前用户ID列表
        user_id_dict = {}
        for username, user_detail in user_data.items():
            user_id = user_detail.get("user_id")
            print(f"当前用户ID :>>>> {user_id} 用户名 :>>>> {username}")
            user_id_dict[user_id] = username
        user_id_input = input("请输入查看用户的指定ID :>>>> ").strip()
        if user_id_input not in user_id_dict.keys():
            print(f"当前用户ID不存在!")
            continue
        username = user_id_dict[user_id_input]
        user_info = user_data.pop(username)
    elif func_id == 7:
        print(f"欢迎来到删除所有用户功能!")
        user_data.clear()
    elif func_id == 8:
        print(f"欢迎来到修改指定用户信息功能!")
        user_id_dict = {}
        for username, user_detail in user_data.items():
            user_id = user_detail.get("user_id")
            print(f"当前用户ID :>>>> {user_id} 用户名 :>>>> {username}")
            user_id_dict[user_id] = username
        user_id_input = input("请输入查看用户的指定ID :>>>> ").strip()
        if user_id_input not in user_id_dict.keys():
            print(f"当前用户ID不存在!")
            continue
        username = user_id_dict[user_id_input]
        user_info = user_data[username]
        password = input("请输入密码 :>>>> ").strip()
        role = input("请输入用户角色(1 admin / 0 user) :>>>> ").strip()
        if not role:
            role = user_info.get("role")
        if role == "1":
            role = "admin"
        elif role == "0":
            role = "user"
        else:
            print("当前角色输入错误,请重新输入!")
        age = input(f"请输入用户年龄{user_info.get('age')} :>>>>").strip()
        if not age.isdigit():
            print(f"当前年龄非法")
            continue
        age = int(age)
        if age < 0 or age > 120:
            print(f"当前年龄非法，不能是非人类!")
            continue
        user_id = input("请输入用户ID :>>>>").strip()
        user_id = user_id.zfill(5)
        if user_id in user_id_dict.keys():
            print(f"当前用户ID {user_id} 已经被使用，请重新输入!")
            continue
        gender = input("请输入用户性别(0 女 / 1 男) :>>>>").strip()
        if gender == "0":
            gender = "女"
        elif gender == "1":
            gender = "男"
        else:
            print(f"不合法的性别!重新输入！")
            continue
        hobby_list = []
        while True:
            hobby = input("请输入用户爱好(输入q退出) :>>>>").strip()
            if hobby == "q":
                break
            else:
                if hobby in hobby_list:
                    print(f"当前爱好已存在,请重新输入!")
                    continue
                else:
                    hobby_list.append(hobby)
        user_data[username] = {
            "username": username,
            "password": password,
            "role": role,
            "user_id": user_id,
            "age": age,
            "gender": gender,
            "hobby": hobby_list,
        }
        print(f"当前用户 {username} 信息添加成功!")
    elif func_id == 9:
        print(f"欢迎下次使用!")
        break
