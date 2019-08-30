# -*- coding:utf-8 -*-
import urllib.request
import json
import os
import time

os.makedirs('result', exist_ok=True)

search_term = ""
sort_key = 'newest'
# technology category
category_list = [16, 331, 332, 333, 334, 335, 336, 337, 52, 362, 338, 51, 339, 340, 341, 342]
query_base = "https://www.kickstarter.com/projects/search.json?term=%s&category_id=%d&page=%d&sort=%s"

for category_id in category_list:
    for page_id in range(1, 201):
        try:
            query = query_base % (
                search_term, category_id, page_id, sort_key
            )
            print(query)
            data = urllib.request.urlopen(query).read().decode("utf-8")
            response_json = json.loads(data)
        except:
            break
    
        # 1ページあたり20件の結果が返ってくるので、1件ずつ保存する
        for project in response_json["projects"]:
            filepath = "result/{}.json".format(project["id"])
            fp = open(filepath, "w")
            fp.write(json.dumps(project, sort_keys=True, indent=2))
            fp.close()
    
        # 1アクセスごとに1秒のウェイトを入れることで、過剰アクセスを防止
        time.sleep(1)