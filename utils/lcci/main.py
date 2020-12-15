import json
import os
from urllib.parse import quote

import requests


if __name__ == '__main__':
    # 抓取leetcode题目
    # spider = Spider()
    # spider.run()

    # 生成题目
    with open('./README_TEMPLATE.md', 'r', encoding='utf-8') as f:
        readme_cn = f.read()
    with open('./README_TEMPLATE_EN.md', 'r', encoding='utf-8') as f:
        readme_en = f.read()

    with open('./lcci.json', 'r', encoding='utf-8') as f:
        result = json.load(f)
        for item in result['lcci']:
            question_id = item['frontend_id']
            question_id = item['frontend_id'][question_id.find(" ")+1:]
            title_cn = item['title']

            path = f'../../lcci/{question_id}.{title_cn}'
            path = path.replace(":", " ")
            if os.path.isdir(path):
                continue
            os.makedirs(path)

            with open(f'{path}/README.md', 'w', encoding='utf-8') as f1:
                f1.write(readme_cn.format(item['frontend_id'],
                                         item["title_cn"],
                                         item['url_cn'],
                                         item['path'],
                                         item['content_cn']))

            with open(f'{path}/README_EN.md', 'w', encoding='utf-8') as f2:
                f2.write(readme_en.format(item['frontend_id'],
                                         item["title"],
                                         item['url'],
                                         item['path_cn'],
                                         item['content']))

            print(path)

        # for item in sorted(result, key=lambda x: x["frontend_question_id"]):
        #     no = int(item['frontend_question_id']) // 100
        #
        #     path = f'./{number_mapper.get(str(no))}/{item["frontend_question_id"]}.{item["title_en"]}'
        #     path = path.replace(":", " ")
        #     print(f'- [{int(item["frontend_question_id"])}. {item["title_en"]}]({item["relative_path_en"]})')


