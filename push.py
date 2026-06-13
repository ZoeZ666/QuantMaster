import subprocess

def git_sync(commit_message):
    try:
        # 添加所有改动
        subprocess.run(["git", "add", "."], check=True)
        # 提交改动
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # 推送至云端
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ 提交并推送成功！")
    except subprocess.CalledProcessError as e:
        print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    msg = input("请输入本次提交的备注信息: ")
    git_sync(msg)