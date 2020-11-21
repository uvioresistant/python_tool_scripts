import os
import requests
from time import time, sleep
from multiprocessing.pool import ThreadPool


# 发请求，写入jpg到本地
def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)


start = time()

if __name__ == '__main__':
    path = []
    for count in range(1, 55):
        path.append('G:\\J\\p2018.10.6_zero\\For_bro\\chapter_7\\粉体技术与工程' + str(count) + '.jpg')
    origin_url = "http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/245ef5d4-73d5-425e-aab1-712d125c7ecb_page-0,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/7c070ff8-bbe6-41e9-b7af-253f171b732f_page-1,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/58174fc7-05e8-452f-a31c-e6f0fdb2560f_page-2,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/c0d9602f-009c-436d-b3dd-05023c05ec1b_page-3,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/337eead9-bb90-4ca2-8222-0210a6f765b4_page-4,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a7f5874a-11e7-438e-9988-7e08492e047e_page-5,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/74706502-2acb-407a-a8f0-bb3be730e0ad_page-6,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/5a56cb23-520e-4f31-b272-2955d8d1f281_page-7,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/efe75be7-512b-432f-a772-acd0b27ecfb2_page-8,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/e83c8107-e5f0-439c-98bd-53b8dd4151f6_page-9,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/68f1d794-337e-49d4-ba5e-18517d1ca884_page-10,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/cdcde5f0-c96b-4bbd-bede-bc61626dc327_page-11,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/7a2c35c9-f2aa-4e41-aff8-f17e24eb5bde_page-12,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a1850526-3cf3-4586-8476-51592bd5fdf6_page-13,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/c5d2795f-e677-4a82-819d-ca31ef5ddd7f_page-14,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/6d21580a-69a8-4cee-9447-b19c589734e1_page-15,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/9ef168c3-6c4c-4f9a-ba36-0c09dd2a0419_page-16,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/eafbb3fe-9e7f-4e6a-840f-c32c0472a156_page-17,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/8b5c844f-fd80-43cc-8b2a-178fb0920a50_page-18,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/2606828b-d748-428b-a8e4-9843fc57786a_page-19,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/38109ef7-8ab6-4c1c-8b99-0bdfa8224c13_page-20,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a1f007be-1025-4605-8650-071269621848_page-21,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/9dd15db1-a39c-41a1-aac0-53cb7504bd3e_page-22,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/c0836422-0090-4e4e-be8e-09188d52dfdd_page-23,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/93f9379b-07e3-4d50-a02d-1305e5e8004d_page-24,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/17f6dc02-d295-48b7-94e9-b00a04a420ec_page-25,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/281908f0-a12d-46d7-82e3-723447842b36_page-26,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/2dc2bf2e-6a1d-4435-8b3e-bd04f13d9aa3_page-27,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/24eb9cfb-0239-4790-9c40-9ed4caebd7ee_page-28,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/df8d1628-6987-454f-a9ce-96ae34bbda6f_page-29,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/048423c6-956e-4e20-af2c-e3246afb85aa_page-30,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/7014d5e9-db3a-460c-82da-9ddb075bf58b_page-31,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/81ff23f3-3924-43d6-b3c0-888008818fa0_page-32,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/c58e13a8-430f-431b-82b1-98eee5d4da65_page-33,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/2daa477f-c409-4f30-aef6-a40427db647e_page-34,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/51ee30ea-64e7-4f71-ab5a-65f3298f3abf_page-35,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/3dc8e404-131c-497e-8daf-8ffd31da4426_page-36,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/703db686-ecea-4dd2-a315-04949da120bc_page-37,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/1176f9df-45b4-4ce6-8c6c-e80fba7a221f_page-38,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/551c6db3-2fb8-42a1-8e54-e2115bd874a0_page-39,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/bb609e95-4a99-44bf-b7d0-751140f20665_page-40,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/d02c91e7-a15b-4f20-9cf4-bea3ce0c1540_page-41,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/418e8d58-5dd0-4f31-a63a-e21935556437_page-42,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/9321613a-5743-46fc-b1fb-0516c82f73f9_page-43,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/8e207131-7c9a-43ca-8a77-646d542a2190_page-44,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a6a81ede-09ed-4e22-becf-e436a05195f6_page-45,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/beaa18f1-d893-47c7-90f8-a24363ffef79_page-46,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a6bd98f2-e6d7-4d47-a888-623f4b4eda4f_page-47,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/a10b2f86-d90a-4969-aa56-8c3ddd1f072d_page-48,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/161faab5-44b1-41e6-8a3e-c3b070dc6c54_page-49,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/13442f6b-d93c-42a6-bbc3-5138f72035d3_page-50,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/2da67a84-da12-45b0-959b-5e6ad0391185_page-51,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/2f475124-d0df-4bdf-9f0c-b093db44e448_page-52,http://met2.fzu.edu.cn/meol/data/convert/2020/10/12/31c31630-8c0d-459e-9593-9ce6fee6f2b8_page-53"
    url = origin_url.split(',')
    urls = list(zip(path, url))
    for x in urls:
        sleep(5)
        url_response(x)
    # pool = ThreadPool(9).imap_unordered(url_response, urls) # 暂时别用这句代码，没找到sleep方法，可能就是这句代码，把网站给跑崩的
    print(f"Time to download: {time() - start}")








