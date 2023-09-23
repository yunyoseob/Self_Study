# 파일 읽고 쓰기
# 파일 경로 설정해주기
input_file_name = "C:/Users/rwk/Desktop/github/Self_Study/Python/file/a.txt";
input_file = open(input_file_name, "r", encoding="utf-8-sig")
output_file_name = "C:/Users/rwk/Desktop/github/Self_Study/Python/file/b.txt";
output_file = open(output_file_name, "a+", encoding="utf-8-sig")

for line in input_file:
    # line = line.strip()
    print(line)
    output_file.writelines(line)