import subprocess

# 执行一个简单的命令
result = subprocess.run(['./biliup', 'login'], stdout=subprocess.PIPE)

# 输出命令的结果
print(result.stdout.decode('utf-8'))
