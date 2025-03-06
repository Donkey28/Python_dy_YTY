import re

n = int(input())
for _ in range(n):
    s = input()
    # 匹配tag及其内容
    tag_pattern = r'<([^>]+)>(.*?)</\1>'
    tags = re.findall(tag_pattern, s)
    valid_tags = []
    for tag_name, tag_content in tags:
        # 匹配电话号码的区号
        area_code_pattern = r'\((\d+)\)-'
        area_codes = re.findall(area_code_pattern, tag_content)
        if area_codes:
            area_codes_str = ','.join(area_codes)
            valid_tags.append(f"<{tag_name}>{area_codes_str}</{tag_name}>")
    if valid_tags:
        for tag in valid_tags:
            print(tag)
    else:
        print("NONE")

