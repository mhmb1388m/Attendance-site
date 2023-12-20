file_name = r'C:\Users\USER\Desktop\test.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"محتوای فایل '{file_name}':")
        print(content)
except FileNotFoundError:
    print(f"خطا: فایل '{file_name}' یافت نشد.")
except Exception as e:
    print(f"خطای ناشناخته: {e}")
